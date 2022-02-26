def percent(marks):
    return (marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/500*100

marks=[45,42,32,45,90]
a=(marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/500*100

marks2=[67,80,70,88,71]
b=percent(marks2)
print(b)
#quiz
def ok(name):
    print("good day "+name) 
ok("parimal")
def greet(name):
    ok="harry"+ name
    return
    
a=greet()
#recuressive
def fact_reccursive(n):
    if n==1 or n==0:
        return 1   
    else:
        return n * fact_reccursive(n-1)

    

b=fact_reccursive(3)

print(b)




