from pathlib import Path
from PIL import Image
import json, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
letters="abcd"
families=["stone","cobblestone","mossy_cobblestone","deepslate","stone_bricks","cracked_stone_bricks","dirt","coarse_dirt","rooted_dirt","gravel"]
vdir=ROOT/"assets/minecraft/textures/block/roughcut_variants"
mdir=ROOT/"assets/minecraft/models/block/roughcut/variants"
sdir=ROOT/"assets/minecraft/blockstates"
for f in families:
    for l in letters:
        p=vdir/f"{f}_{l}.png"
        if not p.exists(): errors.append(f"missing variant texture {p.name}")
        else:
            with Image.open(p) as im:
                if im.size!=(32,32): errors.append(f"{p.name}: {im.size}")
        if not (mdir/f"{f}_{l}.json").exists(): errors.append(f"missing model {f}_{l}.json")
    if not (sdir/f"{f}.json").exists(): errors.append(f"missing blockstate {f}.json")
for stem in ["grass_block_top","grass_block_side","grass_block_side_overlay"]:
    for l in letters:
        p=vdir/f"{stem}_{l}.png"
        if not p.exists(): errors.append(f"missing grass variant {p.name}")
        elif Image.open(p).size!=(32,32): errors.append(f"{p.name}: wrong size")
for l in letters:
    if not (mdir/f"grass_block_{l}.json").exists(): errors.append(f"missing grass model {l}")
if not (sdir/"grass_block.json").exists(): errors.append("missing grass blockstate")
for p in list(mdir.glob("*.json"))+list(sdir.glob("*.json")):
    try: json.loads(p.read_text(encoding="utf-8"))
    except Exception as e: errors.append(f"invalid JSON {p.name}: {e}")
print("=== RoughCut Variation Validator ===")
print("Variant PNGs:", len(list(vdir.glob("*.png"))))
print("Variant models:", len(list(mdir.glob("*.json"))))
print("Weighted blockstates:", len([p for p in sdir.glob("*.json") if p.stem in families+["grass_block"]]))
if errors:
    [print("ERROR:",e) for e in errors]
    sys.exit(1)
print("PASS")
