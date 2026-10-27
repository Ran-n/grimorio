import sys
from datetime import datetime
from pathlib import Path


def save_file(fname, content):
    Path(fname).parent.mkdir(parents=True, exist_ok=True)
    with open(fname, "w", encoding="utf-8") as f:
        f.writelines(line + "\n" for line in content)


def load_file(fname):
    if not Path(fname).is_file():
        raise FileNotFoundError("File " + fname + " does not exist")
    with open(fname, encoding="utf-8") as f:
        return f.read().splitlines()


def format_now():
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")


file_type_map = {
    ".py":   {"comment": None, "shebang": "#!/usr/bin/env python3"},
    ".pyw":  {"comment": None, "shebang": "#!/usr/bin/env python3"},
    ".sh":   {"comment": "#",          "shebang": "#! /bin/sh"},
    ".bash": {"comment": "#",          "shebang": "#! /bin/bash"},
    ".rs":   {"comment": "//",         "shebang": None},
    ".md":   {"comment": "[//]: # (", "shebang": None, "end": " )"},
}
DEFAULT_FT = {"comment": "#"}
STYLE = {
    "author":        "Ran# <ran.hash@proton.me>",
    "indicator":     "+",
    "label_author":  "Authors",
    "label_created": "Created",
    "label_revised": "Revised",
}


def get_ft(file):
    ext = "." + file.rsplit(".", 1)[-1]
    return file_type_map.get(ext, DEFAULT_FT), ext


def is_py_field(line):
    return line.startswith(tuple(STYLE[k] + ":" for k in ("label_author", "label_created", "label_revised")))


def show(file):
    ft, ext = get_ft(file)
    lines = load_file(file)
    if ext in (".py", ".pyw"):
        # only the header fields, so a plain module docstring doesn't count as a header
        for line in lines:
            if is_py_field(line):
                print(line.rstrip())
    else:
        c = ft["comment"]
        for line in lines:
            if line.rstrip().startswith(c + STYLE["indicator"]):
                print(line.rstrip())


def edit(file):
    ft, ext = get_ft(file)
    content = load_file(file)
    now = format_now()
    if ext in (".py", ".pyw"):
        for i, line in enumerate(content):
            if line.startswith(STYLE["label_revised"] + ":"):
                content[i] = STYLE["label_revised"] + ": " + now
    else:
        c = ft["comment"]
        e = ft.get("end", "")
        prefix = c + STYLE["indicator"] + " " + STYLE["label_revised"] + ":"
        for i, line in enumerate(content):
            if line.startswith(prefix):
                content[i] = c + STYLE["indicator"] + " " + STYLE["label_revised"] + ": \t" + now + e
    save_file(file, content)


def create(file):
    ft, ext = get_ft(file)
    content = load_file(file)
    now = format_now()
    if ext in (".py", ".pyw"):
        to_insert = [
            "#!/usr/bin/env python3",
            '"""',
            STYLE["label_author"] + ": " + STYLE["author"],
            STYLE["label_created"] + ": " + now,
            STYLE["label_revised"] + ": " + now,
            '"""',
            "",
        ]
    else:
        c = ft["comment"]
        ind = STYLE["indicator"]
        e = ft.get("end", "")
        sep = c + " " + "-" * (79 - len(c)) + e
        to_insert = [
            sep,
            c + ind + " " + STYLE["label_author"] + ": \t" + STYLE["author"] + e,
            c + ind + " " + STYLE["label_created"] + ": \t" + now + e,
            c + ind + " " + STYLE["label_revised"] + ": \t" + now + e,
            sep,
            "",
        ]
        if ft.get("shebang"):
            to_insert.insert(0, ft["shebang"])
    if content and len(content) >= len(to_insert) and content[: len(to_insert)] == to_insert:
        content = to_insert + content[len(to_insert):]
    else:
        content = to_insert + content
    save_file(file, content)


def remove(file):
    ft, ext = get_ft(file)
    lines = load_file(file)
    if ext in (".py", ".pyw"):
        # drop the header fields, then the docstring they leave empty; other docstrings stay
        content = [l for l in lines if not is_py_field(l)]
        for i in range(len(content) - 1):
            if content[i].strip() == '"""' and content[i + 1].strip() == '"""':
                del content[i : i + 2]
                if i < len(content) and content[i] == "":
                    del content[i]
                break
    else:
        c = ft["comment"]
        content = [l for l in lines if not l.startswith(c + STYLE["indicator"])]
    save_file(file, content)


def help(_=None):
    print()
    print("Help   -----------------------------")
    print("?/-h\t-> Show this message")
    print("-v file\t-> View metadata")
    print("-m file\t-> Modify metadata")
    print("-c file\t-> Create metadata")
    print("-d file\t-> Delete metadata")
    print("------------------------------------")
    print("Supported file types:", ", ".join(file_type_map))
    print()


actions = {"show": show, "edit": edit, "create": create, "remove": remove, "help": help}
actions[sys.argv[1]](sys.argv[2] if len(sys.argv) > 2 else None)
