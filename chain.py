from decimal import *

import numpy as np

class memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

def draw_chain(N):
    N_array = range(1, (N+1))
    draw = np.random.choice(N_array, size=N, replace=False)
    return draw

def chainer(sub, bag, chain):
    chap = chain.append
    for i in range(0, len(bag)):
        chap(bag[i])
        if ((bag[i]-1) not in chain) and ((bag[i]+1) not in chain) :
            sub += 1
    return sub

def sampler(N):
    sample = np.empty(10000000)
    for i in range(0, 10000000):
        subchain_count = 0
        chain = []
        draw = draw_chain(N)
        draw = draw.tolist()
        sample[i] = chainer(subchain_count, draw, chain)
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

