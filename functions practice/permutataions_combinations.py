
#Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!. Number of
#combinations of n objects taken r at a time is: c(n, r) = n! / (r!*(n-r)!) 

while True:
    choice=input("Permutations or Combinations or Exit (P / C / E): ")
    if choice.lower()=='e':
        print("Good bye")
        break
    n=int(input("Enter value of N: "))
    r=int(input("Enter value of R: "))

    ans=0

    def factorial(n):
        ans=1
        for i in range(1,n+1,1):
            ans=ans*i
        return ans

    if choice.lower()=='p':
        print("Permutations: ", factorial(n)/factorial(n-r))
    elif choice.lower()=='c':
        print("Combinations: ",(factorial(n)/factorial(n-r))/factorial(r))
    else:
        print("Invalid Input")
        break
    
    
