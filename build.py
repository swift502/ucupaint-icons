import json
from logging import error
from PIL import Image

# Data
icons = json.load(open('./data/icons.json'))
overlays = json.load(open('./data/overlays.json'))
disabled = json.load(open('./data/disabled.json'))
img = Image.open('./svg/sheet.png')

def crop_tile(index):
    col = index % 10
    row = index // 10

    tile_size = img.width / 10
    target_size = 32
    centerX = col * tile_size + tile_size / 2
    centerY = row * tile_size + tile_size / 2

    top = centerY - target_size / 2
    bottom = centerY + target_size / 2
    left = centerX - target_size / 2
    right = centerX + target_size / 2

    coords = (left, top, right, bottom)
    return img.crop(coords)

# Regular
def process_regular():
    for i in range(len(icons)):
        tile = crop_tile(i)
        tile.save(f"./png/{icons[i]}.png")

# Overlays
def process_overlays():
    for o, (overlay_name, overlay_tiles) in enumerate(overlays.items()):
        # Read overlays from last row of the icon sheet
        overlay = crop_tile(90 + o)

        for i in overlay_tiles:
            if i >= len(icons):
                error(f"Overlay {overlay_name} is defined for an image index that's out of icon name range ({i}). Skipping.")
                continue

            tile = crop_tile(i)
            tile.paste(overlay, (0, 0), overlay)
            tile.save(f"./png/{overlay_name}_{icons[i]}.png")

# Disabled
def process_disabled():
    for d in range(len(disabled)):
        i = disabled[d]
        tile = crop_tile(i)
        alpha = tile.split()[-1]
        alpha = alpha.point(lambda x: int(x * 0.5))
        tile.putalpha(alpha)
        tile.save(f"./png/disabled_{icons[i]}.png")

process_regular()
process_overlays()
process_disabled()