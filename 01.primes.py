import time
import statistics

def primes(n): 
    if n==2:
        return [2]
    elif n<2:
        return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

def benchmark():
	results = []
	gstart = time.time()
	for _ in xrange(5):
		start = time.time()
		count = len(primes(1000000))
		end = time.time()
		results.append(end-start)
	gend = time.time()
	mean = statistics.mean(results)
	stdev = statistics.stdev(results)
	perc = (stdev * 100)/ mean
	print "Benchmark duration: %r seconds" % (gend-gstart)
	print "Mean duration: %r seconds" % mean
	print "Standard deviation: %r (%r %%)" % (stdev, perc)

benchmark()
