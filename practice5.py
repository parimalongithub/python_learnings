dictnory={ "koan":"who",
"ghadi":"watch",
"chai":"tea"
}
a=input("please type the word for translation in english\n")
print("you translation is\n",dictnory[a])

a=input("please enter first   number\n")
b=input("please enter second  number\n")
c=input("please enter third   number\n")
d=input("please enter fourth  number\n")
e=input("please enter fifth   number\n")
f=input("please enter sixth   number\n")
g=input("please enter seventh number\n")
h=input("please enter eighth  number\n")
set={a,b,c,d,e,f,g,h}
print(set)
b={18,"18",18.1}
print(b)
#yes we can add strings as we all as integer as well as float in set
s={}
s.add(20)
s=set()
s.add(20.0)
s.add("20")
print(len(s))
favlanguage={}
a=input("enter your favourite language harsh\n")
b=input("enter your favourite language sujay\n")
c=input("enter your favourite language jay\n")
d=input("enter your favourite language sai\n")
favlanguage["harsh"]=a
favlanguage["sujay"]=b
favlanguage["jay"]=c
favlanguage["sai"]=d
print(favlanguage)



