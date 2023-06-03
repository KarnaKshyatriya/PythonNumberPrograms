import PerfectNumberCheck as o

class Main:
    def __init__(self):
        high,low=[int(x) for x in input("Enter upper and lower limit \n to find out perfect number in a range :: >> \n").split()]
        obj=o.PerfectNumberProgram()
        for x in range(high,low):
            if obj.logic(x):
                print(x,end=' ')

main_object=Main()


       