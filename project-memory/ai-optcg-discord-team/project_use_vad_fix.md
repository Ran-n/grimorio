---
name: project-use-vad-fix
description: USE_VAD permission was missing from all voice channels — fix applied 2026-06-26
metadata: 
  node_type: memory
  type: project
  originSessionId: 3b07ec36-664b-43c4-9c7c-c3d5b7dcbc52
---

All voice channels were missing the `USE_VAD` permission (bit `33554432`), forcing all members into Push-to-Talk. Fixed on 2026-06-26 by adding USE_VAD to channel overwrites for Membro, Lider, Convidado, and Mod on all 10 voice channels (EQUIPO + PARTIDAS).

**Why:** Membro/Lider/Convidado have zero guild-level permissions and rely entirely on channel overwrites, so missing USE_VAD in overwrites = forced PTT. Admin bypasses this via ADMINISTRATOR. Mod already had it at guild level but was also added explicitly to channel overwrites.

**How to apply:** Any future voice channel created must include USE_VAD in the allow overwrites for the relevant roles. Current allow values already updated in server_config.md.
