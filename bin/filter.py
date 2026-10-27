#!/usr/bin/env python3
"""
Authors: Ran# <ran.hash@proton.me>
Created: 2026/10/27 19:06:40.565537
Revised: 2026/10/27 19:06:40.565537
"""

# Git filter "grimorio" (long-running process protocol, configured by bin/setup.py).
#   clean   (working tree -> repo): the profile folder name becomes {USER}; each block between a line
#           `<!-- private -->` and a line `<!-- /private -->` is GPG-encrypted
#   smudge  (repo -> working tree): the reverse, so files on disk read normally
# Encryption isn't deterministic, so the ciphertext of every block is cached by the hash of its plaintext
# (.git/grimorio-cache.json, never committed): an unchanged block encrypts to the same bytes and git sees no change.
# Smudge fills the cache too, so a fresh clone re-cleans to identical blobs. Without the key, blocks stay encrypted.
# This file is excluded from the filter in .gitattributes: it holds the literal placeholder and markers.

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".git" / "grimorio-cache.json"
RECIPIENT = "AA4C66BE276AA0D8D95F003D11705FC643951387"  # Ran# <ran.hash@proton.me>
USER = Path.home().name.encode()
PLACEHOLDER = b"{USER}"
BLOCK = re.compile(rb"(^<!-- private -->\r?\n)(.*?)(^<!-- /private -->\r?$)", re.M | re.S)
ARMOR = b"-----BEGIN PGP MESSAGE-----"

try:
    cache = json.loads(CACHE.read_text())
except (OSError, ValueError):
    cache = {}
cache_dirty = False


def gpg(args: list[str], data: bytes) -> bytes | None:
    r = subprocess.run(["gpg", "--batch", "--quiet", *args], input=data, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def encrypt(inner: bytes) -> bytes:
    global cache_dirty
    if inner.startswith(ARMOR):  # already encrypted (checked out without the key)
        return inner
    key = hashlib.sha256(inner).hexdigest()
    if key not in cache:
        armored = gpg(["--armor", "--encrypt", "--recipient", RECIPIENT], inner)
        if armored is None:
            raise RuntimeError("gpg could not encrypt a private block")
        cache[key] = armored.decode().replace("\r\n", "\n")
        cache_dirty = True
    return cache[key].encode()


def decrypt(inner: bytes) -> bytes:
    global cache_dirty
    if not inner.startswith(ARMOR):
        return inner
    plain = gpg(["--decrypt"], inner)
    if plain is None:
        return inner  # no key here: leave it encrypted
    key = hashlib.sha256(plain).hexdigest()
    armored = inner.decode().replace("\r\n", "\n")
    if cache.get(key) != armored:
        cache[key] = armored
        cache_dirty = True
    return plain


def transform(data: bytes, block_fn, text_fn) -> bytes:
    out, pos = [], 0
    for m in BLOCK.finditer(data):
        out += [text_fn(data[pos : m.start()]), m.group(1), block_fn(m.group(2)), m.group(3)]
        pos = m.end()
    out.append(text_fn(data[pos:]))
    return b"".join(out)


def clean(data: bytes) -> bytes:
    return transform(data, encrypt, lambda t: t.replace(USER, PLACEHOLDER))


def smudge(data: bytes) -> bytes:
    return transform(data, decrypt, lambda t: t.replace(PLACEHOLDER, USER))


# --- git long-running filter protocol (pkt-line) ---

def read_pkt() -> bytes | None:
    size = sys.stdin.buffer.read(4)
    if not size:
        raise EOFError
    n = int(size, 16)
    return None if n == 0 else sys.stdin.buffer.read(n - 4)


def read_text_list() -> list[str]:
    items = []
    while (p := read_pkt()) is not None:
        items.append(p.decode().rstrip("\n"))
    return items


def read_content() -> bytes:
    chunks = []
    while (p := read_pkt()) is not None:
        chunks.append(p)
    return b"".join(chunks)


def write_pkt(data: bytes | None) -> None:
    out = sys.stdout.buffer
    if data is None:
        out.write(b"0000")
    else:
        for i in range(0, max(len(data), 1), 65516):
            chunk = data[i : i + 65516]
            out.write(b"%04x" % (len(chunk) + 4) + chunk)
    out.flush()


def write_text(*lines: str) -> None:
    for line in lines:
        write_pkt((line + "\n").encode())
    write_pkt(None)


def main() -> None:
    global cache_dirty
    if read_text_list() != ["git-filter-client", "version=2"]:
        sys.exit("unexpected filter handshake")
    write_text("git-filter-server", "version=2")
    read_text_list()  # capabilities offered by git
    write_text("capability=clean", "capability=smudge")
    while True:
        try:
            headers = dict(h.split("=", 1) for h in read_text_list())
        except EOFError:
            break
        data = read_content()
        try:
            result = clean(data) if headers.get("command") == "clean" else smudge(data)
        except Exception as e:
            print(f"grimorio filter: {headers.get('pathname')}: {e}", file=sys.stderr)
            write_text("status=error")
            continue
        write_text("status=success")
        if result:
            write_pkt(result)
        write_pkt(None)
        write_pkt(None)  # keep status=success
        if cache_dirty:
            CACHE.write_text(json.dumps(cache, indent=0))
            cache_dirty = False


if __name__ == "__main__":
    main()
