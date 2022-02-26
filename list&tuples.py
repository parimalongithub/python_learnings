#we can create list using []
pr=["apple","ok",1,2,3]#in list we can use differnt data types
print(pr)
#we can acecees index using[]
a=(pr[2])
print(a)
#we also do slicing in list like strings
schoolfreind=["yash","shivam","atharva"]
print(schoolfreind[0:2])
print(schoolfreind[-3:-1])
#list functions :
l1=[2,6,4,7,3,9,  ]
l1.sort()#this function will sort the list in assending order
l1.reverse()
l1.append(9)#add 9 at the end of the lsit
l1.insert(0,4) 
l1.pop(7)
l1.remove(9)
print(l1)
#tuples
Tuple=(3,4,6,8,2,3,56,7,46,43)
print(Tuple)
#the major differnce between the tuple and the list that tuple are NOT mutable(cannot be changed) and list are mutable(can changed)
#P=(1)#wrong way to declare singal element in  the tuple
Q=()#empty tuple
P=(1,)#correct way to decalre tuple
print(P)
#methods in tuples
t=(2,46,46,78,23,86,23,645)
print(t.count(46))
print(t.index(46))