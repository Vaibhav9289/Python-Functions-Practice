def divisors(n):
    '''Returns divisors of a number'''
    ans=[]
    for i in range(1,n):
        if n%i==0:
            ans.append(i)
    return ans


def amicable(n1,n2):
    '''Two different numbers are called amicable numbers if the sum of the
    proper divisors of each is equal to the other number.'''
    d1=divisors(n1)
    d2=divisors(n2)
    if sum(d1)==n2 and sum(d2)==n1:
        return True
    else:
        return False
