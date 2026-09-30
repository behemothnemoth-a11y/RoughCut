from pathlib import Path
from PIL import Image
import json, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

mcmeta = ROOT / "pack.mcmeta"
if not mcmeta.exists():
    errors.append("missing pack.mcmeta")
else:
    try:
        data = json.loads(mcmeta.read_text(encoding="utf-8"))
        pack = data.get("pack", {})
        if pack.get("min_format") != [88, 0] or pack.get("max_format") != [88, 0]:
            errors.append("pack.mcmeta is not locked to resource-pack format 88.0")
    except Exception as e:
        errors.append(f"invalid pack.mcmeta: {e}")

if not (ROOT/"pack.png").exists():
    errors.append("missing pack.png")

block = ROOT/"assets/minecraft/textures/block"
if not block.exists():
    errors.append("missing block texture folder")
else:
    for p in sorted(block.glob("*.png")):
        try:
            im = Image.open(p)
            im.verify()
            with Image.open(p) as im2:
                if im2.size != (32,32):
                    errors.append(f"{p.name}: expected 32x32, got {im2.size}")
        except Exception as e:
            errors.append(f"{p.name}: invalid PNG ({e})")

required = [
    "stone.png","cobblestone.png","deepslate.png","dirt.png",
    "grass_block_top.png","grass_block_side.png","grass_block_side_overlay.png",
    "oak_planks.png","oak_log.png","oak_log_top.png",
    "iron_block.png","copper_block.png","cut_copper.png","glass.png",
    "redstone_ore.png","diamond_ore.png","iron_ore.png","gold_ore.png",
    "crafting_table_top.png","crafting_table_side.png","crafting_table_front.png",
    "furnace_top.png","furnace_side.png","furnace_front.png",
    "barrel_side.png","barrel_top.png","barrel_bottom.png",
]
for name in required:
    if not (block/name).exists():
        errors.append(f"missing expected texture: {name}")

print("=== RoughCut Validator ===")
print(f"Root: {ROOT}")
print(f"Block PNGs: {len(list(block.glob('*.png'))) if block.exists() else 0}")
if warnings:
    for w in warnings:
        print("WARNING:",w)
if errors:
    for e in errors:
        print("ERROR:",e)
    sys.exit(1)
print("PASS")
