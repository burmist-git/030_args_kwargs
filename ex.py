import numba
import numpy as np
import math
import matplotlib.pyplot as plt

def gogo_test(function, *args, **kwargs):
    nn=10
    for i in range(nn):
        y = function(*args,**kwargs)

def gogo_test2(function, x, mean, sigma):
    nn=10
    for i in range(nn):
        y = function(x, mean, sigma)

def printfunc(*args, **kwargs):
    print('printfunc',kwargs['x'])

def printfunckw(*args, **kwargs):
    print('printfunckw')
    print(type(kwargs))
    #for key, value in kwargs.items():
    #    print ("%s == %s" %(key, value))
    print("printfunckw x = %d , mean = %d, sigma = %d"
          %(kwargs['x'][0],kwargs['mean'],kwargs['sigma']))

def printfunckw2(x, mean, sigma, *args, **kwargs):
    print("printfunckw2 x = %d , mean = %d, sigma = %d"
          %(len(x),mean,sigma))
    
if __name__ == "__main__":
    x=[1,2,3,4,5,6]
    mean=0.0
    sigma=1.0
    gogo_test(printfunc, x=x, mean=mean, sigma=sigma)
    print('')
    gogo_test(printfunckw, x=x, mean=mean, sigma=sigma)
    print('')
    printfunckw2(x=x, mean=mean, sigma=sigma)
    print('')
    gogo_test2(printfunckw2, x, mean, sigma)
