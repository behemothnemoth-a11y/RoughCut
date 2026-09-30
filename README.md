# RoughCut

**RoughCut** is an original Minecraft: Java Edition resource pack built around a dirty, hand-inked graphic-novel aesthetic: uneven line work, large painted value shapes, selective hatching, exaggerated material features, and controlled grime.

The art direction is inspired by the *kind* of illustrated/cel-ink visual language associated with games such as Borderlands, but RoughCut does **not** copy Borderlands textures, logos, characters, UI, symbols, or other game assets.

## Target

- Minecraft: Java Edition **26.2**
- Resource Pack format **88.0**
- Base texture resolution: **32×32**
- Current milestone: **DROP_0001 / v0.1 — Visual Foundation**

## What is in Drop 0001

The first vertical slice replaces a deliberately small group of materials so the style can be tested in real gameplay before hundreds of textures are produced:

- Stone
- Dirt
- Grass top / side / biome-tinted side overlay
- Oak planks
- Iron block
- Glass
- Redstone ore
- Diamond ore

Also included:

- `docs/ART_DIRECTION.md` — the visual source of truth
- `docs/PALETTE.md` — starter color system
- `docs/TEXTURE_RULES.md` — repeatable production rules
- `docs/TEST_MATRIX.md` — how each batch should be reviewed in Minecraft
- `docs/ROADMAP.md` — staged expansion plan
- `reference/style-tests/roughcut_drop_0001_styleboard.png` — quick visual board
- `tools/validate_pack.py` — dependency-free structure/PNG validator
- `tools/package_release.ps1` — Windows release packager

## Install for testing

1. Zip `pack.mcmeta`, `pack.png`, and the `assets` directory so they are at the **root** of the zip.
2. Put the zip in your Minecraft `resourcepacks` folder.
3. Launch Minecraft Java 26.2.
4. Enable RoughCut in Resource Packs.
5. Test with shaders disabled first.

You can also run `tools/package_release.ps1`; it creates a clean pack-only zip under `release/`.

## Art principle

RoughCut should not look like Minecraft with a uniform black grid drawn over it. Ink is **selective**. Adjacent blocks must still read as surfaces rather than isolated outlined cubes. Stronger silhouette rendering belongs to a future optional rendering/mod layer.

## Repository layout

```text
RoughCut/
├─ pack.mcmeta
├─ pack.png
├─ assets/minecraft/
│  ├─ textures/
│  │  ├─ block/
│  │  ├─ item/
│  │  ├─ gui/
│  │  ├─ entity/
│  │  └─ particle/
│  └─ font/
├─ docs/
├─ reference/style-tests/
├─ tools/
└─ release/
```

## Status

Drop 0001 is a **style prototype**, not a finished texture pack. The textures are intentionally meant to answer one question: does the RoughCut visual language hold together in-world?
