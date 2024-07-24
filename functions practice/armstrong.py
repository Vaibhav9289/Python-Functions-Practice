def armstrong(n):
    '''accepts an integer and returns true if the sum of the cubes of
    individual digits of that number is equal to the actual number'''
    n2=str(n)
    ans=0
    for i in n2:
        ans+=int(i)**len(n2)
    if int(n2)==ans:
        return True
    else:
        return False
    
