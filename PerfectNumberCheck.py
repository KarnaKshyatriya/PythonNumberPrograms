class PerfectNumberProgram:
    def logic(self,number):
        sum_of_factors=0
        for i in range(1,number):
            if number%i == 0:
             sum_of_factors+=i
        if sum_of_factors == number:
                return True
        return False
   
            