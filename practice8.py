


def maximum(num1,num2,num3 ):

     if (num1>num2  and num1>num3):
         return (num1)
           
     elif(num2>num1 and num2>num3 ):
        return(num2)
     elif(num3>num1 and num3>num2):
         return(num3)
a=90,43,89
print("the maximum number is ",maximum(90,43,89 ))
#degre to farnhite conversion program
def  far(cel):
    return (cel * 9/5) + 32
c=38
print(far(c))
#print new line at the end
print("my",end=" ")
print("is",end=" ")
print("parimal",end=" ") 
#sum of n numbers using recurssive function
def sum(n):
    
    
    if(n==0):
        print("0")
    
    
    else:
        return (n-1)+n 
print(sum(6))
#print the pattern
N=6
for i in range (N):
    print("*" * (N-i))
def con(cm):
    return (cm*2.54)
print(con(6))
def string(string,word):
     newstring=string.replace(word,"")
     return newstring.strip()
p="     my name is parimal    "
x=string(p , "parimal")
print(x)
#printing table using function
def table(n): 
    for x in range (11):
        op=print(x*n)
    return op
print (table(5))


    
    

        

    
    
print(table(2))