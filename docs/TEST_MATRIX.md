# RoughCut Test Matrix — DROP 0003

Test with shaders **off first**. Use normal mipmaps, then repeat any suspicious case at alternate mipmap settings.

| Test | Build / context | Pass condition |
|---|---|---|
| Stone repeat | 7×7+ stone wall | no obvious single stamped crack dominates |
| Cobble repeat | 7×7+ wall/floor | stones read individually without checkerboarding |
| Deepslate distance | cave wall at 3 / 15 / 40 blocks | retains planes; does not collapse to black |
| Brick repeat | long stone-brick corridor | masonry rhythm is strong but not mechanically sterile |
| Cracked brick mix | 70/30 normal/cracked wall | cracked variant reads as damage, not a different material |
| Dirt repeat | broad dirt floor | clods remain organic; no obvious seams |
| Grass top | plains + forest + swamp + dry/warm biome | biome tint works and ink remains visible |
| Grass side | slopes and stacked grass blocks | fringe joins top cleanly; dirt remains readable |
| Coarse/rooted dirt | mixed patch | variants identify at a glance |
| Gravel | 7×7 floor | granular without shimmering visual noise |
| Mossy cobble | wall near foliage/water | moss reads clearly without overpowering stone |
| Mixed terrain | stone + dirt + grass + gravel | shared ink/value language feels coherent |

Capture screenshots of failures before editing. Prefer targeted corrections over global noise or blanket contrast changes.
