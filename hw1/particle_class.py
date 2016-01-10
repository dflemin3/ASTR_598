"""
David Fleming 2016

Module for HW1
"""

import numpy as np

class Position(object):
    """
    Class for 3D cartersian position
    default units in meters
    """
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return ("(%lf,%lf,%lf)" % (self.x,self.y,self.z))
    
        
class Velocity(object):
    """
    Class for 3D cartesian velocity
    default units in m/s
    """
    def __init__(self, vx = 0.0, vy = 0.0, vz = 0.0):
        self.vx = vx
        self.vy = vy
        self.vz = vy
    def __repr__(self):
        # Function to print self
        return ("(%lf,%lf,%lf)" % (self.vx,self.vy,self.vz))
        
class Particle(object):
    """
    class for a particle that has a mass, Position, and
    Velocity
    """
    def __init__(self, mass = 1.0, pos = Position(), vel = Velocity()):
        self.mass = mass # in kg
        self.pos = pos # in m
        self.vel = vel # in m/s
        
    @staticmethod
    def force(p1, p2):
        """
        Compute the gravitational force between two particles
        using Newton's inverse square law where p1, p2 are
        Particle class objects
        """
        G = 6.67408e-11 # Universal gravitational constant in mks
        r_squared = (p1.pos.x - p2.pos.x)**2. + (p1.pos.y - p2.pos.y)**2. + (p1.pos.z - p2.pos.z)**2.
        
        # If particles are on top of each other
        if r_squared == 0.0:
            return np.inf
        
        return G*p1.mass*p2.mass/r_squared