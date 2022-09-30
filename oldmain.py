import numpy as np
import matplotlib.pyplot as plt
plt.figure()
 
#initialise variables
#velocity, gravity, theta
 
############################
 
v = 20
v2 = 20
 
 
theta = 40
theta2 = 80
 
############################
 
 
g=9.81
rads = theta*(np.pi/180)
 
v0x = v * np.cos(rads) #horizontal v component at t=0.
v0y = v * np.sin(rads) #vertical v component at t=0. idrk why numpy wanted rads.
 
maxt=(2*v0y)/g #find the flight time t in simple 2d motion equation.
 
timearray = np.linspace(0,maxt,100)[:,None] # array from 0 to t, 100 increments.
 
x= (timearray*v0x) # vertical displacement
y= (timearray*v0y)-((g/2)*(timearray**2)) # suvat equation moment. Horizontal displacement, y=s

 
####################################################
 
 
rads2 = theta2*(np.pi/180)
 
v0x2 = v2 * np.cos(rads2) #horizontal v componant at t=0.
v0y2 = v2 * np.sin(rads2) #vertical v component at t=0. idrk why numpy wanted rads.
 
maxt2=(2*v0y2)/g #find the flight time t in simple 2d motion equation.
 
 
timearray2 = np.linspace(0,maxt2,100)[:,None] # array from 0 to t, 100 increments.
 
x2= (timearray2*v0x2) # vertical displacement
y2= (timearray2*v0y2)-((g/2)*(timearray2**2)) # suvat equation moment. Horizontal displacement, y=s
 
####################################################
 
print('horizontal displacement:', max(x))
print('vertical displacement:', max(y))
print('timetaken: ',maxt)
 
 
 
plt.plot(x,y)
plt.plot(x2,y2)
#plt.ylim([0,35])
plt.show()
 
r=input()
exit()
