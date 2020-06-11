bound = 2^5 
while True: 
    p = random_prime(bound-1, lbound = bound >> 1) 
    q = random_prime(bound-1, lbound = bound >> 1) 
    if p != q: 
        break

phi = (p-1)*(q-1) 
N = p*q

print ("p = {} = 0x{:x}".format(p,p)) 
print ("q = {} = 0x{:x}".format(q,q)) 
print ("N = {} = 0x{:x}".format(N,N)) 
print ("phi = {} = 0x{:x}".format(phi,phi))

while True: 
    e = ZZ.random_element(2,phi)
    if 1 == gcd(e,phi): 
        d = (e.xgcd(phi)[1])%phi 
        if e != d: 
            break

print ("e = {} = 0x{:x}".format(e,e)) 
print ("d = {} = 0x{:x}".format(d,d))

dp, dq = d%(p-1), d%(q-1) 
q_inv = (q.xgcd(p)[1])%p

print ("dp = {} = 0x{:x}".format(dp,dp)) 
print ("dq = {} = 0x{:x}".format(dq,dq)) 
print ("q_inv = {} = 0x{:x}".format(q_inv,q_inv))

for m in [0..N-1]: 
    c = (m^e)%N 
    mp, mq = m%p, m%q 
    m1 = crt([mp,mq], [p,q]) 
    if m == c: 
        print ("0x{:03x} -> 0x{:03x} -> 0x{:03x} : {}(*)" .format(m, c, m1, m == m1)) 
    else: 
        print ("0x{:03x} -> 0x{:03x} -> 0x{:03x} : {}" .format(m, c, m1, m == m1))