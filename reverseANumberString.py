#here using the negative index of string i am reversing a number

number=input("Enter a number to reverse ::>> \n")
length=len(str(number))
print(length)
for i in range(length-1,-1,-1):
    print(number[i],end='')