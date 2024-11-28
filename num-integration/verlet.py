t = 0.0
dt = 0.01
sim_length = 10

# velocity = 0.0
old_position = 0.0
position = 0.0
force = 10.0
mass = 1.0

while t <= sim_length:
    velocity = position - old_position
    old_position = position
    position += velocity + (force / mass) * dt ** 2

    t += dt
