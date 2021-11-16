#program to enter a binary number and convert it into decimal number
binary_num=int(input("Enter the binary number:"))
decimal_num=0
temp=binary_num#Stores binary number in a temporary variable and that temporary variable is used in output to show the user which number he typed to double check once again even if user haven't  done.
i=0
while(binary_num!=0):
    remainder=binary_num%10
    decimal_num=decimal_num+remainder*(2**i)
    binary_num=binary_num/10
    i=i+1
print("The decimal equivalent of "+str(temp)+" is "+"%.2f"%decimal_num)
#bad operand type for unary +: 'str'.That is why we don't use 'str' when we want only specific decimal number values after the decimal.
