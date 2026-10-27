---
name: doc — project overview
description: Structure, purpose, and contents of the doc repository
type: project
originSessionId: 45cfbfa5-7418-452b-a11a-8582e7a276db
---
Central documentation repo for all Ran# projects. GitHub: https://github.com/Ran-n/doc

## Files
- `README.md` — top-level index; sections: License, Donations
- `LICENSE` — PayBack License (PBL) v2.0 (current active license)
- `donations.md` — donation addresses (Bitcoin, Monero, Wownero); has metadatos header
- `licenses/pbl_v1.0.md` — archived copy of PBL v1.0

## CHANGELOG format
Date-only headers (`## [YYYY-MM-DD]`); no semver, no `[Unreleased]` section. Multiple versioned files in the repo make semver ambiguous.

**How to apply:** When updating CHANGELOG.md for this project, use date headers only — never add an `[Unreleased]` block or version numbers.

## License policy
All Ran# projects use the PayBack License (PBL) v2.0 (latest): free for personal/non-commercial use; commercial use requires a revenue-share agreement (contact ran.hash@proton.me).

**How to apply:** When adding a new license version, archive the old one in `licenses/` (no metadatos header per feedback rule).

## Donation addresses
- Bitcoin: `bc1q79vja8jzr27dxaf3ylu7e49ady8zq0jsm5qfk6`
- Monero: `88Rezd6ZQzaCb1s7K1tRCiCaDzuHrfYsn4q348jJuePpLs84JNsWEghMAZZgzpDPrqD4PBxk7hwMkSdNQ4CLqFHyPVLdX1D`
- Wownero: `WW2RheTNrq8goAi42Dz5AKUj1qLSaTSSgiH7sHR2qRqojg238EXP3MM3xuUgswriET7UrpkEoYaCkecBhnU49oxM1dZyYoSmm`
