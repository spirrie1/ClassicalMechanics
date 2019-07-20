#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:49:27 2019

@author: scott
"""

# This program similates a particle moving in one dimension under gravity
# with no air resistance.  The user must input:
#     - the initial height (y0)
#     - the initial velocity (v0)
# The simulation runs up to 60 seconds or until the particle hits the ground.


# load the required packages
import numpy as np
import matplotlib.pyplot as plt


# Set the initial conditions

y0 = 1.0
x0 = 0.0
v0 = 20.0
g = -9.8

# how high with the ball go?
# it will reach it's peak at -v0/g

t_max = -v0/g

y_max = 0.5*g*t_max**2 + v0*t_max + y0

y_lim = y_max*1.1


# Run the simulation

# Set up the plot
fig, ax = plt.subplots()
ax.set_ylim(-y_max*0.1,y_lim)

# plot the first point
points = ax.plot(x0, y0, marker='o', linestyle='--')[0]
time_passed = ax.text(0.01,y_max*0.1,"Time Elapsed (s): 0")
speed = ax.text(0.01,0, "Velocity (m/s): {0}".format(v0))

for t in np.arange(0,60,0.01):
    
    # Equations of motion 
    v_t = g*t + v0 # update the velocity of the particle at point time t
    y_t = y0 + (v_t**2-v0**2)/(2*g) #update the position of the particle at time t
    
    # Print out the time elapsed and the speed
    time_passed.set_text("Time Elapsed (s): {0}".format(np.round(t,2)))
    speed.set_text("Speed (m/s): {0}".format(np.abs(np.round(v_t,2))))
    
    if y_t >= 0:
        # update the point with the new position
        points.set_data(x0, y_t)
    else:
        # exit the loop if the particle hits the ground at 0
        points.set_data(x0, 0)
        break
    plt.pause(0.00001)

plt.draw()


    







