import numpy as np
import math

class suvat:
    def __init__(self,v,theta,h):
        self.g = 9.81
        self.v = v
        self.h = h
        self.theta = theta
        self.rads = theta*(np.pi/180)
        self.v0y = v * np.cos(self.rads)
        self.v0x = v * np.sin(self.rads) 
        if h ==0:
            self.maxt = (2*self.v0y)/self.g
        else:
            self.maxt = (math.sqrt(2*self.g*self.h+(self.v0y**2))+self.v0y)/self.g

        self.timearray = np.linspace(0,self.maxt,1000)[:,None] # array from 0 to t, 100 increments.

    def projectile_x(self):
        return (self.timearray*self.v0x) # horizontal displacement x=HorizS

    def projectile_y(self):
        return (self.timearray*self.v0y)-((self.g/2)*(self.timearray**2))+self.h # suvat equation moment, verticle displacement, y=vertS






