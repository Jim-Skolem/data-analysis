# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:37:10 2017

@author: 28414
"""
import matplotlib.pyplot as plt

def laplaEigen(dataMat,k,t):
    m,n=shape(dataMat)
    W=mat(zeros([m,m]))
    D=mat(zeros([m,m]))
    for i in range(m):
        k_index=knn(dataMat[i,:],dataMat,k)
        for j in range(k):
            sqDiffVector = dataMat[i,:]-dataMat[k_index[j],:]
            sqDiffVector=array(sqDiffVector)**2
            sqDistances = sqDiffVector.sum()
            W[i,k_index[j]]=math.exp(-sqDistances/t)
            D[i,i]+=W[i,k_index[j]]
    L=D-W
    Dinv=np.linalg.inv(D)
    X=np.dot(D.I,L)
    lamda,f=np.linalg.eig(X)
return lamda,f
def knn(inX, dataSet, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = array(diffMat)**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()    
return sortedDistIndicies[0:k]
dataMat, color = make_swiss_roll(n_samples=2000)
lamda,f=laplaEigen(dataMat,11,5.0)
fm,fn =shape(f)
print('fm,fn:',fm,fn)
lamdaIndicies = argsort(lamda)
first=0
second=0
print(lamdaIndicies[0], lamdaIndicies[1])
for i in range(fm):
    if lamda[lamdaIndicies[i]].real>1e-5:
        print(lamda[lamdaIndicies[i]])
        first=lamdaIndicies[i]
        second=lamdaIndicies[i+1]
        break
print(first, second)
redEigVects = f[:,lamdaIndicies]
fig=plt.figure('origin')
ax1 = fig.add_subplot(111, projection='3d')
ax1.scatter(dataMat[:, 0], dataMat[:, 1], dataMat[:, 2], c=color,cmap=plt.cm.Spectral)
fig=plt.figure('lowdata')
ax2 = fig.add_subplot(111)
ax2.scatter(f[:,first], f[:,second], c=color, cmap=plt.cm.Spectral)
plt.show()