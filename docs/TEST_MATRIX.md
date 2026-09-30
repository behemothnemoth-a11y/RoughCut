# RoughCut Test Matrix — v0.2

## Required test wall
Build one compact test scene containing:
- 5×5 stone, cobblestone, deepslate, dirt, grass, oak plank walls;
- oak logs both vertical and horizontal;
- iron, copper, cut copper;
- glass looking into both bright sky and a dark room;
- redstone, diamond, iron, and gold ore in a cave wall;
- crafting table, furnace, and barrel beside each other.

## Review passes
### Pass A — no shaders
- Daylight
- Torch-lit interior
- Cave
- Rain/overcast if convenient

### Pass B — distance
- 1–3 blocks
- 10–20 blocks
- 40+ blocks

### Pass C — repetition
Look specifically for:
- checkerboard ink;
- obvious repeated crack positions;
- accidental stripes;
- over-dark mipmaps;
- materials becoming indistinguishable.

## Screenshot checklist
Capture:
1. natural terrain;
2. wood/utility station;
3. industrial material wall;
4. ore cave;
5. glass against bright/dark backgrounds.

## Decision labels
- **KEEP** — language is working.
- **TUNE** — right idea, wrong density/value/palette.
- **REDRAW** — material identity or tiling fails.
