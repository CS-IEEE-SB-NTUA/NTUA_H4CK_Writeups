import random
import numpy as np

a = np.empty(225)

def fa():
    v = np.where(a.sum(axis=1) == 15, 1,0)
    h = np.where(a.sum(axis=0) == 15, 1,0)
    d = np.where(np.sum(np.trace(a,dtype=int)) == 15,1,0)
    sd = np.where(np.sum(np.diag(np.fliplr(a))) == 15, 1,0)
    if(v.any() or h.any() or d.any() or sd.any()):
        return  1
    return 0

def fb():
    global a
    a.shape = (15,15)
    if fa():
        return 0
    v = np.where(a.sum(axis=1) == 14, 1,0)
    h = np.where(a.sum(axis=0) == 14, 1,0)
    d = np.where(np.sum(np.trace(a,dtype=int)) == 14,1,0)
    sd = np.where(np.sum(np.diag(np.fliplr(a))) == 14, 1,0)
    if(v.any() or h.any() or d.any() or sd.any()):
        return 1
    return 0
    


def fc():
    global a
    while True:
        a.shape = 225
        a.fill(0)
        for i in range(14*14):
            a[random.randint(0,224)] = 1
        if (fb()):
            a.shape = 225
            print(a)
            return

def fd(m):
    global a
    a[m] = 1
    a.shape = (15,15)
    return fa()

for i in range(20):
    fc()
    r = []
    m = int(input())
    if (m > 224):
        exit()
    if(not(fd(m))):
        exit()
    r.append(m)

f = open("flag.txt","r").read()
print(f)