# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 15:48:11 2016

@author: dflemin3
"""

import particle_class
from particle_class import Position, Velocity

p1 = particle_class.Particle(1.0,Position)

p1 = particle_class.Particle(1.0,Position(1,2,3),Velocity(1,2,3))
p2 = particle_class.Particle(2.0,Position(3,2,1),Velocity(3,2,1))

print(particle_class.Particle.force(p1,p2),"N")