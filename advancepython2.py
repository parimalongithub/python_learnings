#lambda function(just another way to write function)
square=lambda x:x*x
a=square(9)
print(a)




#join function
p=["camara","hard disk","laptop","tripod"]
x=" and ".join(p)
print(x)
print(type(x))




#fromat function
a="hello my name is {} iam from {}".format("parimal","india")
print (a)
#we can also interchange  the words by using indexing
a="hello my name is {1} iam from {0}".format("parimal","india")
print (a)


#map

def cube(num):
    return num*num*num
l1=[2,1,3]
print (list(map(cube,l1)))


#filter (in this method we can directly use function and  print the list with out calling them)
greter_THAN_5=lambda num:num>5
l5=[1,2,3,4,1.2,34,12,34,12,10]
print(list(filter(greter_THAN_5,l5)))

#reduce 
from functools import reduce
sum=lambda a,b:a+b
l10=[1,2,3,4,5]
val=reduce(sum,l10)
print(val)

