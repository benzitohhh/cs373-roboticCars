from math import *

def f(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5 * (x-mu)** 2 / sigma2)
    
def update(mean1, var1, mean2, var2):
    new_mean =  (var2*mean1 + var1*mean2) / (var1+var2)
    new_var = 1 / ((1/var1) + (1/var2))
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]
    
measurements = [5., 6., 7., 9., 10.]    # as means (of gaussians)
motion = [1., 1., 2., 1., 1.]           # as distances (between guassian means)
measurement_sig = 4     # the variance for ALL measurements
motion_sig = 2          # the variance for ALL motion convolutions
mu = 0.
sig = 0.000000001

for n in range(len(measurements)):
    [mu, sig] = update(mu, sig, measurements[n], measurement_sig)
    print 'update:  ', [mu, sig]
    [mu, sig] = predict(mu, sig, motion[n], motion_sig)
    print 'predict:  ', [mu, sig]
    
print p
    
