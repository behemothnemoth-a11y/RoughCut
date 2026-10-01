# RoughCut

**RoughCut** is an original Minecraft: Java Edition resource pack built around a dirty, hand-inked graphic-novel aesthetic: uneven line work, large painted value shapes, selective hatching, exaggerated material features, and controlled grime.

The project studies broad illustrated/cel-ink techniques without copying proprietary textures, logos, characters, UI layouts, symbols, or other game assets.

## Target
- Minecraft: Java Edition **26.2**
- Resource Pack format **88.0**
- Base block texture resolution: **32×32**
- Current milestone: **DROP_0004 / v0.4 — World Variation System**

## Drop 0004
Drop 0003 converts the approved stone/earth image-generation exploration into real 32×32 Minecraft textures. It replaces the earlier natural-material prototypes and adds several missing world-foundation materials.

### Stone family
- Stone
- Cobblestone
- Deepslate
- Stone bricks
- Cracked stone bricks
- Gravel
- Mossy cobblestone

### Earth family
- Dirt
- Coarse dirt
- Rooted dirt
- Grass block top
- Grass block side + biome-tinted overlay

The earlier wood, industrial, utility, glass, and ore prototypes remain present for comparison, but **stone + earth are the approved focus of this drop**.

## Principle
RoughCut should not look like Minecraft with a uniform black grid drawn over it. Ink is selective and explains form. Global silhouettes belong to a future optional rendering/mod layer.

## References
- `reference/style-tests/roughcut_drop_0003_stone_earth_reference.png` — approved material reference grid
- `reference/style-tests/roughcut_drop_0003_implementation_preview.png` — the actual 32×32 pack textures enlarged with nearest-neighbor scaling

## Testing
See `docs/TEST_MATRIX.md` and `docs/STONE_EARTH_PASS.md`. Test without shaders first. Review repeated walls/floors, mipmaps, biome tint, natural transitions, and whether the stronger ink stays readable at normal play distance.


## Vanilla variation system
Drop 0004 adds weighted blockstate/model variation for the approved stone + earth families.
The hero texture remains the most common (weight 4), followed by alternates at weights 3, 2, and 1.
No OptiFine or Continuity dependency is required for these supported blocks.
Deepslate axis behavior and snowy grass behavior are preserved.

See docs/VARIATION_SYSTEM.md and docs/IN_GAME_REVIEW_DROP_0003.md.
