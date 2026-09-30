# RoughCut Texture Rules — v0.1

## Canvas
- Standard: **32×32 px**.
- Work at native resolution; upscale previews with nearest-neighbor only.
- Do not use soft blur.
- Semi-transparent pixels are normally reserved for materials that genuinely need alpha, such as glass.

## Value structure
Every texture should survive a grayscale check. Aim for:
1. one dominant midtone;
2. one broad shadow family;
3. one smaller highlight family;
4. near-black ink accents.

## Ink density
- Typical coverage target: roughly 5–14% dark ink-like pixels.
- Ores/tech may exceed this locally.
- Quiet areas are mandatory.
- Avoid full-frame borders.

## Line vocabulary
Allowed line families:
- broken contour;
- fracture;
- short parallel hatching;
- gouge/scratch;
- panel seam;
- small cross mark at stress points.

Avoid:
- perfectly uniform outlines;
- identical crack motifs repeated across the tile;
- random one-pixel salt-and-pepper noise;
- dense hatching across the entire face.

## Tiling
Before approval, inspect each texture in at least a 5×5 repeat. No accidental vertical/horizontal stripe may dominate at normal play distance. Intentional structures such as planks are exceptions.

## Minecraft readability
A texture must still communicate the vanilla material at a glance. Stylization can exaggerate; it should not destroy gameplay recognition.

## Biome tint
Grass/foliage textures must be checked in at least plains, forest, swamp, and dry/warm conditions before final approval. The first prototype only establishes the structure.

## Mipmaps and distance
Review at close range, 10–20 blocks, and 40+ blocks. If all ink collapses into black mud in mipmaps, reduce density or increase shape size.

## Material-specific rules
### Stone
Use chunky planes and angular fractures. Avoid pebble noise.

### Dirt
Use irregular clods and compressed dark pockets. Keep some larger calm brown fields.

### Wood
Board seams may be strong; grain should be broad and irregular. Avoid photorealistic wood grain.

### Metal
Use hard value transitions, scuffs, dents, and sparse directional scratches.

### Glass
Transparency dominates. Reflection marks should be bold enough to read but sparse enough to see through.

### Ore
Ore should occupy cracks, cavities, or geometric mineral clusters. Use near-black around bright deposits to increase graphic separation.

## Batch approval checklist
- [ ] 32×32 source
- [ ] Vanilla material still readable
- [ ] No accidental full border
- [ ] Repeats cleanly
- [ ] Ink remains legible with mipmaps
- [ ] Palette matches family
- [ ] No copied proprietary art/symbols
- [ ] Screenshot captured in test matrix
