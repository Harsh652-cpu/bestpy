#Program to enter a decimal number.Calculate and display the binary equivalent of this number.
decimal_num=int(input("Enter the decimal number which will be converted into binary number:"))
binary_num=0
i=0
while(decimal_num!=0):
    remainder=decimal_num%2
    binary_num=binary_num+remainder*(10**i)
    decimal_num=decimal_num/2#Here value of binary_num will be in decreasing order and that's why at some point it will be 0 which will result it into termination of the while loop
    i=i+1
print("The binary equivalent of "+str(decimal_num)+" is "+str(binary_num))
#Here on line 7 there is an overflow condition which is too large to get converted into float.A different logic is appreciable for checking which number is an armstrong number and which one is not an armstrong number.