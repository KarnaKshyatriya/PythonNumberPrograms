import math

#taking input from user
number=int(input("Enter a Number to check ::> \n"))

digitcount=int(math.log10(number)+1)

temp=number

#this outer loop continues until the number is broken down to unit digit
while(digitcount>1):

    sumofdigits=0

#this loop adds the digits of the number to itself
    while(temp>0):
        digit=temp%10
        sumofdigits+=digit
        temp=temp//10
    
    digitcount=int(math.log10(sumofdigits)+1)
    temp=sumofdigits

if sumofdigits==1:
    print("The number {} is a Magic Number".format(number))
else:
    print("The number {} is NOT a Magic Number".format(number))