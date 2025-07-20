class Person():
    def __init__(self,firstn,lastn):
        self.firstn=firstn
        self.lastn=lastn
    def fullname (self):
        print("Full name: ",self.firstn  ,self.lastn)
ex_name = Person(str(input("Enter first name: ")),str(input("Enter last name: ")))
ex_name.fullname()