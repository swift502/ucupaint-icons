from PIL import Image

# Icon names left to right, top to bottom.
icons = [
    "background_icon",
    "bake_icon",
    "blend_icon",
    "clean_icon",
    "close_icon",
    "color_icon",
    "group_icon",
    "hemi_icon",
    "image_icon",
    "input_icon",
    "mask_icon",
    "modifier_icon",
    "nodetree_icon",
    "object_index_icon",
    "open_image_icon",
    "rename_icon",
    "texture_icon"
    # "channels_icon",
    # "rgb_channel_icon",
    # "value_channel_icon",
    # "vector_channel_icon"
]

# Last row contains overlays
overlays = [
    "collapsed",
    "uncollapsed"
    # "add"
]

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