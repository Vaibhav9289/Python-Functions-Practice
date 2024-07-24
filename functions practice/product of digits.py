
'''If all digits of a number n are multiplied by each other repeating with the
product, the one
digit number obtained at last is called the multiplicative digital root of n.
The number of times digits need to be multiplied to reach one digit is called
the multiplicative persistance of n.
Example: 86 -> 48 -> 32 -> 6 (MDR 6, MPersistence 3)
 341 -> 12->2 (MDR 2, MPersistence 2)'''

def prodDigits(n):
    '''Returns product of digits of the input number'''
    ans=1
    for i in str(n):
        ans*=int(i)
    return ans

def MDR(n):
    ans=None
    while True:
        ans=prodDigits(n)
        n=prodDigits(n)
        if ans<10:
            return ans
            break
        
def MPersistence(n):
    per=0
    ans=None
    while True:
        ans=prodDigits(n)
        n=prodDigits(n)
        per+=1
        if ans<10:
            return per
            break
