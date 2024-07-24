def decimal_to_binary(n):
    '''function that converts a decimal number to binary number'''
    if n<=0:
        print("Please enter value above than 0")
        exit
    int_part=int(n)
    int_part2=int_part
    decimal_part=str(abs(n-int_part))

    binary_int=''
    binary_decimal=''
    
    while int_part2>0:
        binary_int+=str(int_part2%2)
        int_part2=int_part2//2
    ans_1=binary_int[::-1]

    for i in range(len(decimal_part)-2):
        decimal_part=float(decimal_part)
        a=float(decimal_part)*2
        if a >=1.0:
            binary_decimal+='1'
        else:
            binary_decimal+='0'
        decimal_part=abs(a-1)
    print(f"Binary Value for {int(n)}: ",ans_1)
    print(f"Binary Value for {str(abs(n-int_part))[2:]}: ",binary_decimal)
    print()
    print(f"Binary Value for {n}: ",float(binary_int+'.'+binary_decimal))
