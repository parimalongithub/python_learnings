#exception handling (handling the eroor)
try:

  a=int(input("please enter the numrator\n"))
  b=int(input("please enter the denominator\n"))  
  z=a/b
  print("the divison is",z)


except ZeroDivisionError as e:
   print("you can't divide with zero ")
except ValueError as e:
   print("please enter proper number")


#raising the exception
def increment(num):
   try:
      return num+1
   except:
      raise ValueError("please enter proper number for increment")
   

a=increment(12)
print(a)
#try with else
f=int(input())
try:
   print(f+1)

except Exception as e:
   print(e)
else:#if prgram does not come in except then else statment execuated
   print("the program was succesfully exicuated")


#try with finallly
try:

 a=int(input())
 print(a+2)
except Exception as e:
   print(e)
   exit()
finally:#inspite of whatever happn this code of line excecaute
   print("code run succesfully")

#global and local variable
a=45#global
def fun():
    global a
    print(a)

    a=8#if we did not used global varible then this will act as local and it will act as independent varible
    print(a)
fun()
print(a)

#enummerate function
list1=[12,34,45,"parimal",12.12]
for item,index in enumerate (list1):
   print(index,item)



#list comprehansion
x=[12,21,345,24,345,445,6,345]
b=[ item for item in x if item>100]
print(b)

 
    





