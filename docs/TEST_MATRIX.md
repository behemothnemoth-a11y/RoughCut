# RoughCut Test Matrix

Use the same test world/locations for every major texture batch so changes can be compared.

| Scene | What to place/check | Primary failure to catch |
|---|---|---|
| Daylight material wall | 5×5+ fields of each block | tiling, palette, over-inking |
| Mixed starter house | stone/dirt/grass/oak/glass/iron | cross-material cohesion |
| Shallow cave | stone + redstone + diamond | ore readability and dark-value collapse |
| Night exterior | same starter house | black crush and silhouette readability |
| Rain | natural + glass surfaces | contrast under darker lighting |
| Plains grass | grass top/side | default biome tint |
| Forest grass | grass top/side | green-range behavior |
| Swamp grass | grass top/side | tint mud/contrast behavior |
| 40+ block distance | repeated wall/terrain | mipmap noise |

## Review order
1. Test with shaders **off**.
2. Check nearest surfaces.
3. Back away and inspect mipmaps.
4. Look for repeating lines/grids.
5. Compare all current RoughCut materials in one frame.
6. Only then test optional shaders.

## Drop 0001 questions
- Is the ink too dense or too timid?
- Does 32× feel like the right base resolution?
- Do stone and dirt feel illustrated rather than noisy?
- Does glass belong to the same art direction?
- Do redstone and diamond pop without looking pasted on?
- Does the style survive from close-up to normal building distance?
