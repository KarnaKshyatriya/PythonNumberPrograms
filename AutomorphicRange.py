import LogicAutomorphicRange as o

class AutomorphicRange:
    def userRangeInput(self):
        high,low=[int(x) for x in input("Enter the upper and lower limit  ::>>  ").split()]
        obj=o.Automorphic()
        for x in range(high,low):
            if obj.logic(x):
                print(x,end=' ')
    
object=AutomorphicRange()
object.userRangeInput()