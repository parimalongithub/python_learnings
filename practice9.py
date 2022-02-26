class programmer:
    company="microsoft"
    def __init__(self,name,product  ):
        self.name=name
        self.product=product
        print(f"The name of company is {self.company}  and the name of  the programmer is {self.name}the product is {self.product}")
a=programmer("parimal","git")
class calculator:
    def __init__(self,number):
        self.number=number
    def square(self):
        print("the sqaure of 9 is ",(self.number**2))
    def cube(self):
        print('the cube of the 9 is ',(self.number**3))
    def squareroot(self):
        print("the sqaureroot of the 9 is ",(self.number**0.5))
    @staticmethod     
    def greet():
        print("************ welocome to the best calculator of Earth ************")   
a=calculator(2)
a.greet()
a.square()
a.cube()
a.squareroot()
 
        
        
