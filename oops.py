class Employee:#this how class has been called
    company="Google"
    salary= 100
parimal=Employee()#this is  how object has been called
harsh=Employee()
#creating the instance atrribute
parimal.salary=400
print(parimal.salary)

print(harsh.salary)

#print(parimal.address) this line will throw the error beacuse there address is not present in instance or class
#use of self paramenter
class Employee():
    company="Microsoft"
    def salary(self):
        print("salary is 10k")
    #use of stactic method
    @staticmethod
    def greet():
        print('good morning, sir!')
    

parimal=Employee()
parimal.salary() 
#the above line is equivalent to Employee.salary(harry) thas's why we use self
#use of static function
parimal.greet()
class Employee():
    def __init__(self):
        print("employee has been created!")
parimal=Employee()

