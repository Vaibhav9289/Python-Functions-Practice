def isprime(n):
    '''If two consecutive odd numbers are
    both prime then they are known as twin primes'''
    factors=[]
    for i in range(2,n):
        if n%i==0:
            factors.append(i)
    if len(factors)>0:
        return False
    else:
        return True
for i in range(3,1000,2):
    if isprime(i) and isprime(i-2):
        print(f"{i} and {i-2} are twin primes")
