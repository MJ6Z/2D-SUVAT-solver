import numpy as np
import math

class suvat:
    def __init__(self,v,theta,h):
        self.g = 9.81 
        self.v = v
        self.h = h
        self.theta = theta # from the verticle
        self.rads = theta*(np.pi/180) # putting theta in rads for numpy

        #verticle and horizontal componants of v at t=0.
        self.v0y = v * np.cos(self.rads)
        self.v0x = v * np.sin(self.rads) 

        #flight time
        if h ==0:
            self.maxt = (2*self.v0y)/self.g
        else:
            self.maxt = (math.sqrt(2*self.g*self.h+(self.v0y**2))+self.v0y)/self.g 

        # array from 0 to t, 2000 increments, used to calculate
        self.timearray = np.linspace(0,self.maxt,2000)[:,None]



    def projectile_x(self):
        x=(self.timearray*self.v0x) # horizontal displacement for the x axis
        x=x.flatten()  # formatting for the graphing engine
        return x.tolist()


    def projectile_y(self):
        y=(self.timearray*self.v0y)-((self.g/2)*(self.timearray**2))+self.h # verticle displacement for the y axis
        y=y.flatten()   # formatting for the graphing engine
        return y.tolist()
    





