import numpy as np

def runge_kutta_4_system(f, t0, state0, t_end, h):
    """
    RK4 for a system of two first-order ODEs.

    f: function returning [dx/dt, dv/dt].
    t0: initial time.
    state0: initial state [x0, v0].
    t_end: final time.
    h: time step.
    """
    t = t0
    state = state0
    trajectory = []  # To store time, position, and velocity

    while t <= t_end:
        trajectory.append((t, *state))
        
        # Compute RK4 terms
        k1 = h * f(t, state)
        k2 = h * f(t + h/2, state + k1/2)
        k3 = h * f(t + h/2, state + k2/2)
        k4 = h * f(t + h, state + k3)
        
        # Update state and time
        state = state + (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
    
    return trajectory


# Define the system of ODEs for position and velocity
def derivatives(t, state):
    """
    Returns the derivatives [dx/dt, dv/dt].
    state = [x, v] where x is position and v is velocity.
    """
    x, v = state
    a = 10  # Constant acceleration
    dxdt = v
    dvdt = a
    return np.array([dxdt, dvdt])

# Initial conditions and simulation parameters
x0 = 0     # Initial position (m)
v0 = 0     # Initial velocity (m/s)
t0 = 0     # Initial time (s)
t_end = 10 # Final time (s)
h = 0.1    # Time step (s)

# Initial state [position, velocity]
state0 = np.array([x0, v0])

# Integrate using RK4
trajectory = runge_kutta_4_system(derivatives, t0, state0, t_end, h)

# Print results
for t, x, v in trajectory:
    print(f"t = {t:.2f}, x = {x:.2f}, v = {v:.2f}")