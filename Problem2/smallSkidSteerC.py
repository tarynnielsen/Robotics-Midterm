# here is the code for problem 2c
import matplotlib.pyplot as plt
import numpy as np


# Create an array of angles from 0 to 2*pi (360 degrees)
theta = np.linspace(0, 2*np.pi, 100)

# equation for the boundary circle with a radius of 18m
boundary = 9.0
x1 = boundary * np.cos(theta)
y1 = boundary * np.sin(theta)


"""
skid steer equations
x(t)=x(0)+sum(0-t)(Vcos(theta(tau)))
y(t)=x(0)+sum(0-t)(Vsin(theta(tau)))
"""

dt = 0.1 # time step
velocity = 8 # m/s
angVelocity = 0.9 # m/s
steps = 100
x = []
y = []
direction = []

xStart = 9
yStart = 0
directionStart = 1.62

for t in range(steps):
    x.append(xStart)
    y.append(yStart)
    direction.append(directionStart)

    # if (t==10):
    #     angVelocity -= 0.6
    # if (t==25):
    #     angVelocity -= 0.25
    # if (t==50):
    #     angVelocity -= 0.17
    
    xStart += velocity * np.cos(directionStart) * dt
    yStart += velocity * np.sin(directionStart) * dt
    directionStart += angVelocity * dt




# Plot the circles
plt.figure(figsize=(8, 6))
plt.plot(x1, y1, label='Boundary')
plt.plot(x, y, marker='o', linestyle='-', markersize=5, label='bus path')


# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')  # Equal scaling to maintain circular shape
plt.grid(True)
plt.legend()
plt.show()
