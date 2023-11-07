#this is the file for the ackermann model
import matplotlib.pyplot as plt
import numpy as np

#initial conditions
x = 0
y = 0
theta = 0

# set up lists for position
xList = [x]
yList = [y]

# parameters
L = 10.67 # m
v = 8 #m/s
delta = .5 # steering angle
dt = 0.1 # time step
steps = 200

for t in range(steps):
    x += v * np.cos(theta) * dt
    y += v * np.sin(theta) * dt

    if (t == 10):
        delta += .5
    if (t == 20):
        delta -= .15
    if (t == 30):
        delta -= .15
    if (t == 40):
        delta -= .15

    theta += (v / L) * np.tan(delta) * dt
    xList.append(x)
    yList.append(y)


#create circle boundary
angle = np.linspace(0, 2*np.pi, 100)
radius = 18
x1 = radius * np.cos(angle)
y1 = radius * np.sin(angle)


#plot everything
plt.figure(figsize=(8, 6))
plt.plot(x1, y1, label='Boundary')
plt.plot(xList, yList, marker='o', linestyle='-', markersize=4, label='bus path')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()