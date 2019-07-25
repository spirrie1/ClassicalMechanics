#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur Jul 25 19:40:25 2019

@author: scott
"""

# This program similates a particle being thrown from a height y0
# with no air resistance.  The user must input:
#     - the initial height (y0)
#     - the initial velocity (v0)
# The simulation runs up to 60 seconds or until the particle hits the ground.


# load the required packages
import numpy as np
import matplotlib.pyplot as plt


# Set the initial conditions

x0 = 0
y0 = 10
v0 = 100
g = -9.8


# Run the simulation

# Set up the plot
fig, ax = plt.subplots()
# Simulated particle plot
ax.set_ylim(0,y0)
ax.set_xlim(0,150)
ax.set_ylabel("Height (m)")


# plot the first point in the simulated y axis
points = ax.plot(x0, y0, marker='o', linestyle='--')[0]


for t in np.arange(0,60,0.01):
    
    # Equations of motion 
    v_x_t = v0 # update the velocity in the x direction of the particle at time t
    v_y_t = g*t # update the velocity in the y direction of the particle at time t. Notice that the initial velocity is 0 in the y direction
    x_t = x0 + v0*t # update the x coordinate of the particle at time t
    y_t = y0 + ((v_y_t**2)/(2*g))  # update the y coordinate of the particle at time t
                                   # notice that the initial velocity in this direction is 0
    
    # Print out the time elapsed and the speed
    #time_passed.set_text("Time Elapsed (s): {0}".format(np.round(t,2)))
    #speed.set_text("Speed (m/s): {0}".format(np.abs(np.round(v_t,2))))
    
    if y_t >= 0:
        # update the point with the new position
        points.set_data(x_t, y_t)
       
    else:
        # exit the loop if the particle hits the ground at 0
        points.set_data(x_t, 0)
        break
    plt.pause(0.001)

plt.draw()


    







