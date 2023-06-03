class Palindrome:
    def logic(self,number):
        #number=int(input("Enter a number to reverse ::>> \n"))
        reverse=0
        copy=number
        while(number>0):
           digit=number%10
           reverse=reverse*10+digit
           number=number//10
        if(copy==reverse):
            return True
        return False

         