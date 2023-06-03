number=int(input("Enter a number to check ::>> \n"))
sumOfFactors=0
for i in range(1,number):
    if number%i==0:
        sumOfFactors+=i

if sumOfFactors == number:
    print("The number {} is a Perfect Number".format(number))
else:
    print("The number {} is NOT a Perfect Number".format(number))