class StudentDetails:
    Ins = "IGIT"
    def __init__(self,roll,name,branch):
        self.RollNo = roll
        self.Name = name
        self.Branch = branch
    def StDt(self):
        print()
        print("Name of the institute",self.Ins)
        print()
        print("Roll number of the student:",self.RollNo)
        print("Name of the student:",self.Name)
        print("Name of the branch:",self.Branch)

sd1 = StudentDetails(1,"Lucky","CSE")
sd1.StDt()
sd2 = StudentDetails(2,"Samir","Chem")
sd2.StDt()
sd3 = StudentDetails(3,"Manish","Prod")
sd3.StDt()