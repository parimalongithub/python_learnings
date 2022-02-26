from lib2to3.pgen2.driver import Driver


class C2dvec:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        print(f"{self.i}i+{self.j}j")
class C3dvec:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        print(f"{self.i}i+{self.j}j+{self.k}k")
a=C2dvec(1,3)
b=C3dvec(1,4,7)

class animals:
    pass
class pet(animals):
    pass
class dog(pet):
    def bark(self):
        print("the dog is barking")
a=dog()
a.bark()

class employe:
    salary=16000
    increment=1.5
    
    @property
    def totalsalary(self):
       
        print(self.salary*self.increment)
    @totalsalary.setter
    def salaryafterincrement(self,a):
        self.increment=a/self.salary
a=employe()
a.totalsalary
a.salaryafterincrement=30000
print(a.increment)

class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c):
        return f"{self.r+c.r}+{self.i+c.i}i"
    def __mul__(self,d):
        return f"{self.r*d.r - self.i*d.i}+{self.r*d.i+self.i*d.r}i"
a=complex(3,2)
b=complex(1,7,)
print(a*b)
class vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        return f"{self.vec[0]}i+ {self.vec[1]}j+ {self.vec[2]}k"
a=vector([1,2,3])
print(a)




    


        

    







        




        
