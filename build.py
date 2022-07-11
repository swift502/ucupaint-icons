import json
from PIL import Image

# Icon names left to right, top to bottom.
icons = json.load(open('./data/icons.json'))

# Last row contains overlays
overlays = json.load(open('./data/icons.json'))

img = Image.open('./svg/grid.png')

tile = img.width / 10

# Regular
for i in range(len(icons)):
    col = i % 10
    row = i // 10

    left = col * tile
    top = row * tile
    right = left + tile
    bottom = top + tile

    coords = (left, top, right, bottom)
    crop = img.crop(coords)
    crop.save(f"./png/{icons[i]}.png")

    # Overlays
    # Disabled