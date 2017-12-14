# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:34:03 2017

@author: 28414
"""

import matplotlib.pyplot as plt

days=[1,2,3,4,5]
sleeping=[7,8,6,10,7]
eating=[2,3,4,1,2]
working=[9,8,10,11,8]
playing=[6,5,4,2,7]

plt.plot([],[],color="g",label="sleeping",linewidth=5)
plt.plot([],[],color="b",label="eating",linewidth=5)
plt.plot([],[],color="r",label="working",linewidth=5)
plt.plot([],[],color="y",label="playing",linewidth=5)
plt.stackplot(days,sleeping,eating,working,playing,colors=["g","b","r","y"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("graph")
plt.legend()