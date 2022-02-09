import numpy #importing numpy library
from collections import Counter

#mean= It actually represents the average of the given collection of data.
values = [9, 11,22, 34, 17, 22, 34, 22, 40] 
mean = numpy.mean(values) 
print(mean)

#medain =Generally median represents the mid-value of the given set of data when arranged in a particular order.
median = numpy.median(values) 
print(median)

#mode= The most frequent number occurring in the data set is known as the mode.
from scipy import stats
mode = stats.mode(values) 
print(mode)

# Suppose the values included another 34. What problem might occur?

#mean
values = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34] 
mean = numpy.mean(values) 
print(mean) 

#meadian
median = numpy.median(values) 
print(median) 

#mode
n=len(values)
data=Counter(values)
mode=dict(data)
m=[k for k, v in mode.items() if v== max(list(data.values()))]
if len(m) == n:
    mode= "no mode found"
else:
    mode = "Mode:"+",".join(map(str,m))
print(mode)
