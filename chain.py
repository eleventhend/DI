from decimal import *
import random
from random import shuffle

import numpy as np

def chainer(sub, bag, N):
    chain = [False]*(N+2)
    for i in xrange(0, N-1):
        j = bag[i]
        chain[j] = True
        if not (chain[j-1] or chain[j+1]):
            sub+=1
    return sub

def sampler(N):
    sample = np.empty(10000000)
    for i in xrange(0, 10000000):
        draw = range(1, (N+1))
        random.shuffle(draw)
        sample[i] = chainer(0, draw, N)
    return sample

m8 = np.mean(sampler(8), dtype=np.float64)
m16 = np.mean(sampler(16), dtype=np.float64)
m32 = np.mean(sampler(32), dtype=np.float64)
s8 = np.std(sampler(8))
s16 = np.std(sampler(16))
s32 = np.std(sampler(32))

print "Mean of M for N=8: %(m)s" %{"m": Decimal(m8)}
print "Mean of M for N=16: %(m)s" %{"m": Decimal(m16)}
print "Mean of M for N=32: %(m)s" %{"m": Decimal(m32)}
print "Standard Deviation of M for N=8: %(s)s" %{"s": s8}
print "Standard Deviation of M for N=16: %(s)s" %{"s": s16}
print "Standard Deviation of M for N=32: %(s)s" %{"s": s32}
