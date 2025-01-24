# This program is written for getting near field heat flux 
# of some standard objects

import meep as mp
import numpy as np
import matplotlib.pyplot as plt

a = 1e-6
c = 2.998e8  # speed of light in vacuum

r = 0.1
pad = 4
dpml = 2

sxy = 2*(dpml + r + pad)
resolution = 56

cell_size = mp.Vector3(sxy, sxy)

