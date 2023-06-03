import Palindrome_Class as sk

class Main:
    def __init__(self):
        number=int(input("Enter a number to check ::>> \n "))
        obj=sk.Palindrome()
        if obj.logic(number):
            print("The number {} is a Palindrome number ".format(number))
        else:
            print("The number {} is NOT a Palindrome number ".format(number))

user_object=Main()

    