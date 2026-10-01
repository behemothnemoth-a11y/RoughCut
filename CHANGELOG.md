# Changelog

## DROP 0004 — v0.4 World Variation System
- Added four weighted visual variants for stone, cobblestone, mossy cobblestone, deepslate, stone bricks, cracked stone bricks, dirt, coarse dirt, rooted dirt, gravel, and grass.
- Added vanilla weighted blockstate/model randomization; no external CTM/random-texture mod is required for these blocks.
- Preserved deepslate axis placement and snowy grass behavior.
- Added 52 variation texture PNGs and 44 custom block models.
- Added docs/VARIATION_SYSTEM.md and docs/IN_GAME_REVIEW_DROP_0003.md.
- Added a validator dedicated to weighted variants and a preview built from the real 32×32 implementation.
- Kept hero textures as the most common variant using a 4:3:2:1 weighting.
- Variation alternates are an early anti-repetition pass and remain candidates for later hand-painted replacement.

## DROP 0003 — v0.3 Stone + Earth Foundation
- Promoted the approved image-generated stone/earth exploration into playable 32×32 textures.
- Rebuilt stone, cobblestone, deepslate, dirt, grass top, and grass side around the stronger approved visual direction.
- Added stone bricks and cracked stone bricks.
- Added coarse dirt, rooted dirt, gravel, and mossy cobblestone.
- Preserved biome tinting by separating the grass-side fringe into a grayscale alpha overlay.
- Added the approved material reference grid and an implementation preview generated from the actual pack PNGs.
- Added `docs/STONE_EARTH_PASS.md` with in-game review criteria and known limitations.
- Updated the validator and release packager for Drop 0003.

## DROP 0002 — v0.2 Material Language
- Redrew the original vertical-slice materials around larger value shapes and more selective ink.
- Added cobblestone and deepslate.
- Added oak log side/top.
- Added copper block and cut copper.
- Added iron ore and gold ore to the ore language test.
- Added crafting table, furnace, and barrel texture sets.
- Reworked glass to avoid a perimeter-grid effect.
- Added `MATERIAL_LANGUAGE.md`.
- Updated art direction, texture rules, test matrix, roadmap, README, and pack metadata.
- Added a hardened bootstrap workflow and validator.
- Moved safety backups outside the Git repository.
- Added preflight clean-tree checking before a drop can modify the repository.

## DROP 0001 — v0.1 Visual Foundation
- Established RoughCut project structure.
- Established 32×32 base resolution.
- Added initial style bible, palette, texture rules, test matrix, and roadmap.
- Added the first small material vertical slice.
