number=int(input("Enter a number to check ::> "))

# type conversion to integer since input method takes
# input in the form of string

square=number**2

length=len(str(number))

digit=square%pow(10,length)

# modulus operator returns the last digits based on 10 raised to the power.
# 76 square = 5776. To return the last two digits raise 10 to the power of input that is 76

if digit==number:
    print("The number {} is a Automorphic Number".format(number))
else:
    print("The number {} is NOT a Automorphic Number".format(number))