#a=int(input("please enter the value 1 number\n"))
#
#b=int(input("please enter the value 2 number\n"))
#
#c=int(input("please enter the value 3 number\n"))
#
#d=int(input("please enter the value 4 number\n"))
#if(a>b and a>c and a>d):
#    print("gratest number in four numbers",A)
#elif(b>a and b>c and b>d):
#    print(" gratest number in four numbers",b)
#elif(c>a and c>b and c>d):
#   print(" greatest number in four numbers",c)
#elif(d>a and d>b and d>c):
#   print("  greatest number in four numbers",d)
#another way to write  same the program
a=int(input("please enter the value 1 number\n"))
b=int(input("please enter the value 2 number\n"))
c=int(input("please enter the value 3 number\n"))
d=int(input("please enter the value 4 number\n"))
if(a>b):
    f1= a
else:
    f1=b
if(c>d):
    f2=b
else:
    f2=d
if(f1>f2):
    print((f1), " is greatest")
else:
    print((f2), "is the greatest")
subject1=int(input("Enter the marks of 1 subject\n"))
subject2=int(input("Enter the marks of 2 subject\n"))
subject3=int(input("Enter the marks of 3 subject\n"))
a=subject1/100
b=subject2/100
c=subject3/100
d=(subject1+subject2+subject3)/100
if(a>33/100 and b>33/100 and c>33/100 and d>40/100):
    print("congratulations you are pass the examination!")
else:
    print("sorry you are fail in examination but dont give a hope try next time")
comment=input("please enter the comment\n")
if("make a lot of money "in comment):
    print("this comment is spam")
elif("buy now"in comment):
    print("this comment is spam ")
elif("subscribe this "in comment):
    print("this comment is spam")
elif("click this "in comment):
    print("this comment is spam")
else:
    print("this comment does not contain spam")

username=input("please enter the user name\n")
b=len(username)
if(b<10):
    print("username must be contain more than 10 charactors")
else:
    print("ok")
a=["parimal","gautami","siddhika"]
b=input("please enter the text\n")
if(b in a):
    print("the following list contain your text")
else:
    print("enterd text is not in comment")



marks=int(input("please enter your marks\n"))
if(marks>=90):
    grade=("EX")
elif(marks>=80):
    grade="A"
elif(marks>=70):
    grade="B"
elif(marks>=60):
    grade="c"
elif(marks>=50):
    grade="d"
elif(marks<50):
    grade="f"
print("your grade is " + grade)



