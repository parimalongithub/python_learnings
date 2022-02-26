#single inheritance
class employee:
    company="google"
    def showdetails(self):

     print("this is an employee")
class programmer(employee):
    language="pyhton"
    def getlaunguage(self):
        print("the language is ",{self.language})
    #def showdetails(self):

    # print("this is an programmer")  this is overwriting   
a=employee()
a.showdetails()
p=programmer()
p.showdetails()
print(p.company)

#multiple inheritance
class employee:
    company="microsoft"
    uniqueid="1243"
class freelancer:
    comapny="fiveer"
    level=0
class programmer(employee,freelancer):
     name="harsh"
a=programmer()
print(a.level)
print(a.company)#in this line the microsoft will print as as comapny because we have first called employee

#multilevel inheritance
class person:
    country="india"
    def haveatea(self):
        print("iam having  tea")

class employee(person):
    company="honda"
    def getsalary(self):
        print("the salary of employee is"(self.salary))
    def haveatea(self):
        print("iam employee and iam having  tea")

class programmer(employee):
    company="fiver"
    def getsalary(self):
          print("the salary of programmer is"(self.salary))
    def haveatea(self):
           print("iam programmer and iam having  tea")
a=person()
a.haveatea()
#a.company()this line will throw eroor because there no company in person
e=employee()
e.haveatea()
print(e.company)
pr=programmer()
pr.haveatea()
print(pr.country)

#********************supermethod*******************************
class person:
    country="india"
    def haveatea(self):
        
        print("iam having  tea")

class employee(person):
    company="honda"
    def getsalary(self):
        print("the salary of employee is"(self.salary))
    def haveatea(self):
        super().haveatea()

        print("iam employee and iam having  tea")

class programmer(employee):
    company="fiver"
    def getsalary(self):
          print("the salary of programmer is"(self.salary))
    def haveatea(self):
           super().haveatea()#this how we call supermethod
           print("iam programmer and iam having  tea")
p=person()

c=employee()
c.haveatea()

pr=programmer()
pr.haveatea()

#*****************************class method*********************************
class comapny():
    salary=1500
    @classmethod
    def changesalry(self,newsalary):
        self.salary=newsalary
a=comapny()
print(a.salary)
a.changesalry(1550)
print(a.salary)
#************************propertydecorator*******************      
class employee:
    company="dell"
    salary=15000
    salarybounus=1000
    @property
    def totalsalary(self):
        return self.salary + self.salarybounus
    @totalsalary.setter
    def totalsalary(self,amount):
        self.salarybounus=amount-self.salary
a=employee()
print(a.totalsalary)
a.totalsalary=15500
print(a.salary)
print(a.salarybounus)

#******************operator overloading (dunder method)**********************************
class number:#look at practice set example for better understanding
    def __init__(self,num1):
       self.num=num1
    def __add__(self,s):
        
        return self.num+s.num
n1=number(21)
n2=number(12)
sum=n1+n2
print(sum)
















