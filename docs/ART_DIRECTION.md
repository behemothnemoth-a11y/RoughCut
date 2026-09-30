# RoughCut Art Direction — v0.2

## Core statement
RoughCut should look like Minecraft was illustrated by hand with an ink pen, broad digital paint, and a dirty print process — while remaining immediately readable as Minecraft.

## v0.2 refinement
Drop 0002 moves away from the first-pass procedural/noise feel and toward authored, readable shapes.

### Selective ink
- Never outline a block face simply because an edge exists.
- Ink should describe fractures, panel seams, cavities, bark cuts, plank seams, mineral pockets, or wear.
- Thick dark marks are focal accents; most line work stays one pixel at 32×32.
- Repetition is more damaging than low detail. A quiet tile is preferable to a tile full of repeated marks.

### Large value breaks
- Each texture should read in 3–5 major value regions before small marks are added.
- Shadow shapes should be angular and intentional rather than evenly distributed noise.
- Highlights belong on planes and material features, not every outer edge.

### Hatching
- Use short groups, usually 2–4 strokes.
- Hatching should reinforce a local shadow or roughness change.
- Do not hatch every material equally. Glass should have almost none; deepslate can carry more.

### Material identity
- Stone: slab-like planes, fractures, cool dirty gray.
- Cobble: individual stones with broken dark mortar, not uniform black grout.
- Deepslate: flatter, darker plates with restrained directional hatch.
- Dirt: warm clods, calm midtone fields, root/scratch accents.
- Grass: grouped blades and torn transitions, not dense leaf noise.
- Oak: strong plank/bark rhythm, knots, broad grain.
- Iron: cold plate values, scuffs, hard highlights.
- Copper: warm plate values with sparse oxidized marks.
- Glass: transparency first; only a few strong reflections.
- Ores: bright mineral clusters embedded in dark cavities.

## Color discipline
Bright chroma remains scarce. Natural/building materials are muted so redstone, diamond, gold, future UI signals, and eventual loot systems can carry stronger saturation.

## No copied game assets
RoughCut studies broad cel-ink/comic rendering principles only. Do not trace or reproduce Borderlands textures, logos, characters, UI layouts, manufacturer symbols, or weapon skins.

## Future rendering layer
The resource pack establishes surface language. Global silhouettes, dynamic rim lines, damage numbers, loot beams, procedural weapon rendering, animated UI, and similar effects belong to a later optional Fabric/rendering layer.
