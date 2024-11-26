import math
from PIL import Image

INPUT_FILE = "clapping-hands"
RESOLUTION = (4096, 4096)
MARGIN = (32, 32)

im_source = Image.open("input/" + INPUT_FILE + ".png")
im_output = Image.new("RGBA", RESOLUTION)

steps_x = math.ceil(RESOLUTION[0] / im_source.size[0])
steps_y = math.ceil(RESOLUTION[1] / im_source.size[1])

actual_size = (im_source.size[0] + MARGIN[0], im_source.size[1] + MARGIN[1])
stagger = math.ceil(actual_size[0] / 2)

for x in range(steps_x):
    for y in range(steps_y):
        corner = (
            actual_size[0] * x - stagger * (y % 2),
            actual_size[1] * y
        )

        box = (
            corner[0], corner[1],
            corner[0] + im_source.size[0],
            corner[1] + im_source.size[1],
        )

        im_output.paste(im_source, box, im_source)

im_output.save("output/" + INPUT_FILE + "-bg.png")
