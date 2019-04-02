import numpy as np
from scipy import stats

dataset= [1,1,2,3,4,6,18]

#mean value
mean= np.mean(dataset)

#median value
median = np.median(dataset)

#mode value
mode= stats.mode(dataset)

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)

Mean:  5.0
Median:  3.0
Mode:  ModeResult(mode=array([1]), count=array([2]))
