# RoughCut Variation System — DROP 0004

## Purpose
DROP 0004 attacks the biggest issue revealed by the first in-game test: repeated 32×32 hero textures become visible stamps across large terrain and walls.

## Implementation
RoughCut now overrides selected vanilla blockstate JSON files with weighted model arrays. Each supported family has A/B/C/D textures. A is the approved hero texture and is intentionally the most common.

Weights are 4 : 3 : 2 : 1.

Supported families:
- stone
- cobblestone
- mossy cobblestone
- deepslate
- stone bricks
- cracked stone bricks
- dirt
- coarse dirt
- rooted dirt
- gravel
- grass block

## Compatibility behavior
This uses vanilla resource-pack blockstates and models. It does not require OptiFine, Continuity, or a mod.
Deepslate keeps its axis-dependent placement. Grass keeps the vanilla snowy state and uses weighted variants only for normal grass.

## Art status
B/C/D are production alternates derived from the approved hero textures to break repetition. They are not the final bespoke hand-painted variant set. Future passes can replace individual alternates without changing the blockstate system.

## Test protocol
Build at least:
- 16×16 grass/dirt ground
- 12×8 stone wall
- 12×8 cobblestone wall
- mixed stone-brick ruin
- deepslate tunnel
- gravel patch

Look for visible rows, checkerboards, sudden brightness jumps, orientation errors, broken snowy grass, and deepslate end/side mistakes.
