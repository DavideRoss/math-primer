import random

SAMPLES = 10000
hits = 0

for i in range(SAMPLES):
    pt = (random.uniform(-1, 1), random.uniform(-1, 1))

    # Euclidean distance
    # We can omit x_1 because it's (0, 0)
    # We can omit sqrt since distance = 1
    distance = pt[0] ** 2 + pt[1] ** 2
    if distance < 1:
        hits += 1

print(hits / SAMPLES * 4)