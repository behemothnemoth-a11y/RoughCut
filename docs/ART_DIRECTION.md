# RoughCut Art Direction — v0.1

## Core statement

RoughCut should look like Minecraft was illustrated by hand with an ink pen, broad digital paint, and a dirty print process — while remaining immediately readable as Minecraft.

## Four pillars

### 1. Aggressive, imperfect ink
- Use near-black rather than pure black for most line work.
- Lines should vary in length, thickness, and direction.
- Favor broken seams, cracks, scratches, and material contours over full rectangular borders.
- A texture should never look vector-perfect.

### 2. Big value shapes
- Prefer a few strong light/mid/shadow regions over uniform pixel noise.
- Shadows may be exaggerated to give a cel-painted/comic impression.
- Highlights should describe the material, not simply trace every edge.

### 3. Material personality
- Stone: angular fractures, slabs, sparse hatch marks.
- Dirt: clods, cuts, small roots/scratches, compressed shadow pockets.
- Grass: chunky blade groups and torn silhouette transitions.
- Wood: inked seams, knots, gouges, broad grain sweeps.
- Metal: hard value breaks, scuffs, panel marks, cold highlights.
- Glass: empty space first; only enough ink/reflection to read the plane.
- Ores: deposits should feel embedded in cracks/cavities rather than pasted dots.

### 4. Controlled dirt
- Grime is a compositional tool, not a noise filter.
- Put dirt where it explains wear, creases, cavities, and contact.
- Every surface should still have quiet areas.

## Base resolution

32×32 is the standard production resolution. It gives enough room for ink rhythm and hatching while preserving Minecraft's pixel character. Higher-resolution exceptions should be deliberate and documented.

## Ink behavior

Do **not** draw a continuous dark perimeter around every block texture. Repeated blocks would become a distracting checkerboard. Instead:

- place short dark edge accents irregularly;
- draw internal cracks and material seams;
- allow lines to terminate abruptly;
- use neighboring value contrast to imply form;
- reserve eventual global silhouettes for the future rendering/mod layer.

## Hatching

Hatching should be sparse. Use it to reinforce a shadow plane or rough material, not as wallpaper. Typical groups are 2–5 short parallel strokes with imperfect spacing.

## Color

RoughCut uses a restrained palette per texture. A normal block should generally stay within roughly 6–10 purposeful colors before biome tinting/transparency. Saturation is reserved for signals, ores, magic, UI accents, and future loot systems.

## Originality rule

The project may study broad comic/cel-ink techniques, but it must not trace, extract, recolor, or reproduce Borderlands textures, logos, manufacturer marks, UI layouts, character art, weapon skins, or proprietary symbols. RoughCut needs its own visual identity.

## Future mod compatibility

The resource pack establishes the visual grammar. A later RoughCut mod can add features that a resource pack cannot reliably provide alone: dynamic silhouettes, stylized damage numbers, loot beams, rarity treatments, animated UI, procedural weapons, custom entities, and world systems.
