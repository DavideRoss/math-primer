from pathlib import Path
from PIL import Image

PADDING = 64

for path in Path('../manim-project/media/images/text').rglob('*.png'):
    print(f'Cropping {path.name}...')
    img = Image.open(path)
    img = img.crop(img.getbbox())
    width, height = img.size

    img_cropped = Image.new(img.mode, (width + PADDING * 2, height + PADDING * 2))
    img_cropped.paste(img, (PADDING, PADDING))
    img_cropped.save('output/' + path.name)