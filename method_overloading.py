#If we are trying to declare "multiple methods" with same name and different number of arguments,then python will always consider "last method".
class Computations():
    def Add(self, a, b):
        return (a+b)
    def Add(self, a, b, c):
        return (a+b-c)
    def Add(self, a, b, c, d):
        return (a+b-c+d)
cc = Computations()
#print(cc.Add(1,2))
#print(cc.Add(1,2,3))
print(cc.Add(1,2,3,4))