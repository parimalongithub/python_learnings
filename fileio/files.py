f=open("sample.txt","r")
#f=open("sample.txt") by default it is read mode 
#data=f.read(5) we can also read specific charactors
data=f.read()
print(data)
f.close( ) 
 #writing the file
x=open('another.txt','w')
x.write("I am writing this file")
x.close()
#appending the file
x=open("another.txt","a")
x.write("I am writing this file,iam appending this file")
x.close()
#over writing the file
x=open('another.txt','w') 
x.write("overwriting")
x.write("overwriting")
x.write("overwriting")
x.write("overwriting")
x.write("overwriting")
x.close()
#with statment
with open("sample.txt") as f:
    a=f.read()
print(a)
#in with statment we can also write the file
#and in with statment we dont need to close the file