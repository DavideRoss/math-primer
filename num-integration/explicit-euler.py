t = 0.0
dt = 1.0
sim_length = 10

velocity = 0.0
position = 0.0
force = 10.0
mass = 1.0

while t <= sim_length:
    print("Time: {0:<8.3f}     Position: {1:<8.2f}     Velocity: {2:.2f}".format(t, position, velocity))

    position += velocity * dt
    velocity += (force / mass) * dt

    t += dt