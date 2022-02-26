#syntax of dictonory 
dictonory={"velocity":"having direction as well as  speed ",
"value":"amount",
"a":[23,43,12]
}
print(dictonory["velocity"])
print(dictonory["value"])
print(dictonory["a"])
dictonory["a"]=[45,56]
print(dictonory["a"]) 
#dictonory methods
mydictonary={"velocity":"having direction as well as  speed ",
"value":"amount",
"a":[23,43,12]
}
print(mydictonary.keys())
print(mydictonary.values())
print(mydictonary.items())
updatedict={
 "physics":"subject",
  "maths":"subject",
 "a":[90]
  
}
dictonory.update(updatedict)
print(dictonory)
print(mydictonary.get("velocity"))#it does not throws the eroor prints none
print(mydictonary["velocity"])#it does the throw eroor
#sets
b={23,56}
print(type(b))
#syntax for empty sets
z=set()
z.add(5)
z.add(45)
z.add(56)
z.add(56)
z.add(56)
#z.add([46,34])in sets we cannot add list as well as dictonory
z.add((45,64,56))
print(type(z))
print(z) 
#operation in sets
s={2,3,6,8,4}
print(len(s)) 
s.remove(2)
#s.pop()
#s.clear()
s.union({54,23,54,32,2,3,4,6,8})
s.intersection({54,23,54,32,2,3,4,6,8})
print(s)
 