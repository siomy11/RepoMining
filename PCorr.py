#Pearson Correlation Function (python)

import math

def mean(alist):
	mean = sum(alist) / len(alist)
	return mean

def standardDev (alist):
    mean = getMean(alist)
    runningSum = 0

    for item in alist:
        holder = item - mean
        holder = holder ** 2
        runningSum = runningSum + holder

    if len(alist) < 1:
        stdDev = math.sqrt(runningSum / (len(alist) - 1))
    else:
        stdDev = 0
    return stdDev

def correlation(xlist, ylist):
	xbar = mean(xlist)
	ybar = mean(ylist)
	xstd = standardDev(xlist)
	ystd = standardDev(ylist)
	num = 0.0
	
	for i in range(len(xlist)):
		num = num + (xlist[i]-xbar) * (ylist[i]-ybar)
	
	corr = num / ((len(xlist)-1) * xstd * ystd
	return corr
	
