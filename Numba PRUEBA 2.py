import numpy as np
from numba import jit
from numpy import arange

arr=np.array([
    [1,2],
    [3,4]
])

@jit
def suma_numpy(arr):
    return np.sum(arr)
def suma_python(arr):
    result=0.0
    M,N=arr.shape
    for ii in range(M):
        for jj in range(N):
            result += arr[ii,jj]
    return(result)

a=np.random.rand(1000,1000)

print(suma_python(a))
print(suma_numpy(a))
