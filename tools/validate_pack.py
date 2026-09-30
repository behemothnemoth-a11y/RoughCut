#!/usr/bin/env python3
from pathlib import Path
import json, struct, sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [
    'stone.png', 'dirt.png', 'grass_block_top.png', 'grass_block_side.png',
    'grass_block_side_overlay.png', 'oak_planks.png', 'iron_block.png',
    'glass.png', 'redstone_ore.png', 'diamond_ore.png'
]
BLOCK = ROOT / 'assets/minecraft/textures/block'

def png_size(path):
    with path.open('rb') as f:
        sig = f.read(8)
        if sig != b'\x89PNG\r\n\x1a\n':
            raise ValueError('bad PNG signature')
        length = struct.unpack('>I', f.read(4))[0]
        typ = f.read(4)
        if typ != b'IHDR' or length < 8:
            raise ValueError('missing IHDR')
        return struct.unpack('>II', f.read(8))

errors = []
meta = ROOT / 'pack.mcmeta'
if not meta.exists():
    errors.append('missing pack.mcmeta')
else:
    try:
        data = json.loads(meta.read_text(encoding='utf-8'))
        p = data['pack']
        if p.get('min_format') != [88, 0] or p.get('max_format') != [88, 0]:
            errors.append('pack format is not locked to 88.0')
    except Exception as e:
        errors.append(f'pack.mcmeta invalid: {e}')

if not (ROOT/'pack.png').exists():
    errors.append('missing pack.png')

for name in EXPECTED:
    path = BLOCK / name
    if not path.exists():
        errors.append(f'missing texture: {name}')
        continue
    try:
        w, h = png_size(path)
        if (w, h) != (32, 32):
            errors.append(f'{name}: expected 32x32, got {w}x{h}')
    except Exception as e:
        errors.append(f'{name}: {e}')

if errors:
    print('ROUGH CUT VALIDATION: FAIL')
    for e in errors:
        print(' -', e)
    sys.exit(1)

print('ROUGH CUT VALIDATION: PASS')
print('Target: Minecraft Java 26.2 / Resource Pack 88.0')
print(f'Prototype textures: {len(EXPECTED)}')
