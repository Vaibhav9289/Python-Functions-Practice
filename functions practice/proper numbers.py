def divisors(n):
    ''' Gives proper divisors of a number'''
    ans=[]
    for i in range(1,n):
        if n%i==0:
            ans.append(i)
    return ans


def propernumber(stop):
    '''A number is called perfect if the sum of proper divisors of that number
    is equal to the number'''
     proper=[]
     for i in range(stop):
         d=divisors(i)
         if sum(d)==i:
             proper.append(i)
     return proper
