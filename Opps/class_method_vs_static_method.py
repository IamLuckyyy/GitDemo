#class method
class Banker():
    cust = 10000
    @classmethod
    def service(cls,name):
        print("Welcome to class methods")
        print("{} has {} customers...".format(name,cls.cust))
#calling through class name
Banker.service("SBI")
Banker.service("MBA")


#static method
class Bank():
    @staticmethod
    def mymethod(attr):
        print("Welcome to static methods")
        print("Instance through both class and object")
        print("Passed argument is:",attr)
#calling through object
bb = Bank()
bb.mymethod("Python")
#calling through class name
Bank.mymethod("Django")