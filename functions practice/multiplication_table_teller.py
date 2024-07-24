import time
print("Multiplication Table Teller")
x=int(input("Enter a Number"))
for i in range(1,11):
    print(f"{x} X {i} = {x*i}")
    time.sleep(0.1)
