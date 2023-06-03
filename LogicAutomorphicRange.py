
class Automorphic:
    def logic(self,number):
        square=number**2
        length=len(str(number))
        digit=square%pow(10,length)
        if number == digit:
            return True
            
    

