# RoughCut Texture Rules — v0.2

## Canvas
- Standard block texture: **32×32 px**.
- Nearest-neighbor scaling only for previews.
- No blur or photographic filtering.
- Alpha is reserved for materials that need it.

## Approval order
1. Silhouette/material recognition.
2. Major light/mid/shadow regions.
3. Selective ink.
4. Material marks.
5. Hatching/grime.
6. 5×5 tiling test.
7. In-game mipmap/distance test.

## Ink
- Typical coverage: 4–12% of pixels.
- Avoid continuous frame borders.
- Use broken contours, fractures, seams, gouges, scratches, and short hatch groups.
- One strong mark is better than ten random marks.

## Tiling
- Every standard block must survive a 5×5 repeat preview.
- Do not let a unique crack land in the same visually dominant location on every tile.
- Intentional horizontal/vertical rhythms such as planks are allowed but should include variation.

## Value
Every texture should remain readable in grayscale:
- dominant midtone;
- broad shadow family;
- limited highlight family;
- near-black accents.

## Distance
Review at:
- 1–3 blocks;
- 10–20 blocks;
- 40+ blocks with normal mipmapping.

If the texture becomes dark mud at distance, reduce ink or enlarge shapes.

## Biome-tinted assets
Grass/foliage structure should remain readable in plains, forest, swamp, and warm/dry biomes. Do not bake a strong green hue into an overlay that Minecraft will tint again.

## Transparent materials
Glass should remain mostly empty. Do not create a black grid around every glass block.

## Originality
Do not copy proprietary textures, symbols, logos, UI arrangements, or characters from other games.

## Drop 0002 batch
The v0.2 vertical slice covers natural terrain, wood, industrial blocks, core workstations, glass, and four ore families to test one coherent visual language across very different materials.
