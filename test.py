#n1=int(input())
#n2=int(input())
#n3=int(input())
#tuple=(n1,
#       n2, n3)
#print(tuple)
#



#N=int(input())
#for a in range (N):
#     a={(input()):[list((input()))]}
#     print(a)
#     
#
#query_name=(a.get((input())))
#print(query_name)
#
#b=((query_name)[0]+(query_name)[1]+(query_name)[2])/3
#print(b) 
#



#n = int(input("Enter"))
#data_dict={}
#for i in range(n):
#    data=input("enter The data ")
#    data=data.split()
#    print(data)
#    k=data[1:]
#    data_dict[data[0]]=[int(i) for i in k]
#    print(data_dict)
#n=int(input())
#for i in range(1,n+1):
#
#   print(i,end=" ")
#
#n=int(input("length of list"))
#s=set()
#
#for a in range(n):
#   a=int(input())
#   s.add(a)
#print(s)
#N=int(input('number of commands'))
#for b in range(N):
#   b=int(input())
#   try:   
#        s.remove(b)
#   except:
#        print("keyerror:",b)
#else: 
#    print("none")
#    print(s)
#
#for d in range(N):
#    d=s.discard(int(input()))
#    print("none")
#    print(s)
#
#for g in range(N):
#
#    try:
#    
#       g= s.pop()
#    except:
#        print("KeyError: pop from an empty set",s)
#
#

    
#n=int(input())
#for a in range (n):
#    print(a*a)
#
#lst=[]
#num=int(input("how many numbers:"))
#for i in range (num):
#   numbers=int(input("enter the number"))
#   lst.append(numbers)
#sm=sum(lst)
#avg=sm/num
#print("max number is ",max(lst),"\n min number is ",min(lst),"\n avg of numbers",avg
#
#)
#
#""" Rock Paper Scissors
#----------------------------------------
#"""
#import random
#import os
#import re
#os.system('cls' if os.name=='nt' else 'clear')
#while (1 < 2):
#    print ("\n")
#    print ("Rock, Paper, Scissors - Shoot!")
#    userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
#    if not re.match("[SsRrPp]", userChoice):
#        print ("Please choose a letter:")
#        print ("Rock, Scissors or Paper.")
#        continue
#    #Echo the user's choice
#    print ("You chose: ", (userChoice))
#    choices = ['R', 'P', 'S']
#    opponenetChoice = random.choice(choices)
#    print ("I chose: ", opponenetChoice)
#    if opponenetChoice == str.upper(userChoice):
#        print ("Tie! ")
#
#    elif opponenetChoice == 'R' and userChoice.upper() == 'S':      
#        print ("Scissors beats rock, I win! ")
#        continue
#    elif opponenetChoice == 'S' and userChoice.upper() == 'P':      
#        print ("Scissors beats paper! I win! ")
#        continue
#    elif opponenetChoice == 'P' and userChoice.upper() == 'R':      
#        print ("Paper beat rock, I win! ")
#        continue
#    else:       
#        print ("You win!")

#print("-----------.|.------------")
#print("---------.|..|..|.---------") 
#print("------.|..|..|..|..|.------")
#print("---.|..|..|..|..|..|..|.---")
#print("----------WELCOME----------")
#print("---.|..|..|..|..|..|..|.---")
#print("------.|..|..|..|..|.------")
#print("---------.|..|..|.---------")
#print("------------.|.------------")
#
#s=set()
#n=int(input())
#for i in range(n):
#    i=s.add(input())
# 
#print(len(s))
#
#import random
#rannum=random.randint(1,3)
#if(rannum==1):
#    x="R"
#elif(rannum==2):
#    x="P"
#elif(rannum==3):
#    x="S"
#print("computer chooses",x)
#a=input("please choose between Rock[R],Paper[P]and Seassior[S]")
#def game(a,x):
#
#    if(a==x):
#            return "T"
#    elif(x=="S"):
#        if(a=="R"):
#
#            return ("W")
#    elif(x=="S"):
#        if(a=="P"):
#
#            return("L")
#    elif(x=="R"):
#        if(a=="P"):
#            return("W")
#    elif(x=="R"):
#        if(a=="S"):
#             return("L")
#    elif(x=="P"):
#        if(a=="S"):
#            return("W")
#    elif(x=="P"):
#        if(a=="R"):
#            return("L")
#b=game(a,x)
#print(b)  
#
#
#if (b==True):
#    print("you win the game!")
#elif(b==False):
#    print("you lose the game!")
#elif (b==None):
#    print("the game is tie")

#import random
#ran=random.randint(1,6)
#a=(input("please enter to roll the dice"))
#print(ran)
#from itertools import product
#l1=[]
#n = int(input())
#for i in range (n):
#    i=int(input())
#    l1.append(i)
#print(l1)
#l2=[]
#for m in range (n):
#    m=int(input())
#    l2.append(m)
#print(l2)
#b=print(list(product(l1,l2)))
#import itertools import product

#A = [int(x) for x in input().split()]
#B = (int(y) for y in input().split())
#
#a= (tuple(product(A,B)))
#print(a[0],a[1],a[2],a[3])
#a=(input().split())
#print("parimal")
#def split_and_join(line):
#    
#     input().split()
#  
#    
#    
#
#if __name__ == '__main__':
#    line = input()
#    result = split_and_join(line)
#    print(result)
#
#def count_substring(string, sub_string):
#    for sub_string in string:
#        print (tuple(sub_string))
#        
#
#
#if __name__ == '__main__':
#    string = input().strip()
#    sub_string = input().strip()
#    
#    count = count_substring(string, sub_string)
#    print(count)
#n=int(input())
#A=[]
#for i in range (n):
#    b=int(input())
#    A.append(b)
#a=max(A)
#while(max(A)==a):
#
#   A.remove(a)
#print("the maximum number is",max(A))
##a=(input().split())
#print(a)
#n=int(input())
#A=(input().split())
#print(A)
#a=max(A)
#while(max(A)==a):
#
#   A.remove(a)
#print(max(A)
#    int(i)
#def mutate_string(s,i,c):
#    a=list(s)
#    a[i]=(c)
#    p=("".join(a))
#    return p
#if __name__ == '__main__':
#    s = input()
#    i, c = input().split()
#    s_new = mutate_string(s, int(i), c)
#    print(s_new)





    







