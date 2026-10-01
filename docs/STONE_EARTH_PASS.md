# Stone + Earth Pass — DROP 0003

## Status
This is the first RoughCut batch whose playable textures are derived from an approved image-generation material board rather than from the earlier procedural placeholder language. Treat these assets as the new visual baseline for natural world materials.

## Implementation mapping
| Approved concept | Minecraft texture | Notes |
|---|---|---|
| stone | `stone.png` | large fractured planes |
| cobblestone | `cobblestone.png` | rounded/chunky individual stones |
| deepslate | `deepslate.png` | blue-charcoal, lower-value stone |
| stone bricks | `stone_bricks.png` | strong masonry seams |
| cracked stone bricks | `cracked_stone_bricks.png` | fractures interrupt brick rhythm |
| dirt | `dirt.png` | clods, pockets, embedded stones |
| grass top | `grass_block_top.png` | grayscale source for biome tint |
| grass side | `grass_block_side.png` + overlay | dirt base + tintable ragged fringe |
| coarse dirt | `coarse_dirt.png` | heavier debris/clods |
| rooted dirt | `rooted_dirt.png` | pale roots as main identifier |
| gravel | `gravel.png` | smaller angular aggregate |
| mossy stone concept | `mossy_cobblestone.png` | mapped to vanilla mossy cobble |

## Review in Minecraft
Build a small test area using at least a 7×7 wall/floor patch of every texture. Review at 1–3 blocks, 10–20 blocks, and 40+ blocks.

Check specifically:
- Do repeated stone faces create obvious diagonal or circular stamps?
- Does cobblestone remain distinct from stone bricks at distance?
- Does deepslate keep enough internal information without becoming black mud?
- Does grass biome tint remain readable in plains, forest, swamp, and a dry/warm biome?
- Does the grass-side fringe connect naturally to the top texture?
- Are rooted/coarse dirt immediately distinguishable from normal dirt?
- Does gravel look granular without becoming high-frequency visual static?

## Known limitation
The approved concept board was generated as an art-direction reference, not as a mathematically seamless source atlas. DROP 0003 performs a light edge reconciliation when reducing the concepts to 32×32, but the real verdict must come from in-game repeated surfaces. Any obvious tiling stamps should be corrected by hand in the next refinement drop rather than hidden with procedural noise.

## DROP 0004 follow-up
The approved DROP 0003 hero textures remain the source of truth. DROP 0004 adds vanilla weighted alternates to reduce the world-scale repetition observed in the first live test. Variants should be judged as a surface system, not as isolated thumbnails.
