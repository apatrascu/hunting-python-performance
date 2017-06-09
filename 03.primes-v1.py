import time


def primes(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = []
    for i in range(3, n+1):
        if i % 2 != 0:
            s.append(i)
    mroot = n ** 0.5
    half = (n + 1) / 2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3) / 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    l = [2]
    for x in s:
        if x:
            l.append(x)
    return l

	
def benchmark():
	start = time.time()
	for _ in xrange(40):
		count = len(primes(1000000))
	end = time.time()
	print "Benchmark duration: %r seconds" % (end-start)

	
benchmark()