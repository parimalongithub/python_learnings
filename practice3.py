A=input("Enter your name\n ")
print("Good Afternoon,"+A) 
letter=('''Dear <|name|>
            you are selected!
           Date:  <|date|>    ''')
name=input("Enter your name\n")

date=input("Enter date\n")

letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)

z=("This is the string with  doubelspaces")
m=(z.find("  "))
m=(z.replace("  "," "))
print(m)