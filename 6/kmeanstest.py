#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 23:20:15 2018

@author: jim
"""

from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
w=kmeans.labels_

z=kmeans.predict([[0, 0], [4, 4]])

y=kmeans.cluster_centers_