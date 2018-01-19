import random as rd
from math import gcd

def fermat_test(p,n=1):
    if p==2:
        return True
    elif p%2==0:
        return False
    for i in range(n):
        while True:
            a=random.randrange(1,p)
            if gcd(a,p)==1:
                break;
        if pow(a,p-1,p)!=1:
            return False
    return True

def miller_rabin(n, k=40):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def carmichael_slow(p):
    Coprimes=[]
    for i in range(p):
        if gcd(p,i)==1:
            Coprimes.append(i)
    n=1
    while True:
        for i in Coprimes:
            if pow(i,n,p)!=1:
                n+=1
                continue
        break;
    return n;

def carmichael(p,q,Test=False):
    if Test==True:
        if not miller_rabin(p) or not miller_rabin(q):
            return 0
    return abs((p-1)*(q-1))/gcd((p-1)*(q-1));

def modinv(a, m):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def key_generator(p,q=0,Test=False,h=0):
    if q==0:
        n=p
        carm=carmichael_slow(p)
    elif Test==True:
        if not miller_rabin(p) and not miller_rabin(q):
            return 0,0,0
    else:
        n=p*q
        carm=carmichael(p,q)
    if h==0:
        while True:
            h=random.randrange(2,carm)
            if gcd(h,carm)==1:
                break;
    d=modinv(h,carm)
    return n,h,d

def auto_key(b_len=2048):
    while True:
        p=random.randrange(2,pow(2,b_len//2))
        if miller_rabin(p):
            break;
    while True:
        q=random.randrange(2,pow(2,b_len//2))
        if miller_rabin(p):
            break;
    return key_generator(p,q)

def number_cryption(n,p,m):
    In=[]
    Out=[]
    if type(m) is int:
        In.append(m)
    else:
        In=m
    for i in In:
        Out.append(pow(i,p,n))
    return Out
