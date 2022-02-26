from traceback import print_tb


def game():
    return 105
score=game()
with open("high.txt") as f:
    highscore=(f.read()) 

    if (highscore==""): 
        with open("high.txt","w") as f:

           f.write( (str(score)))
    elif (int(highscore)<score) :
         with open("high.txt","w") as f:

           f.write( (str(score)))
with open ("k.txt") as f:
    with open("k.txt",)as f:
       m= f.read()
       if "donkey"in m:
           m=m.replace("donkey","d$%@*y")
           with open ("k.txt","w") as f:
            f.write(m)
words=["pagal","mota","favda"]    
with open ("k2.txt")as f :
    content=f.read()      
    for  word in words :
        content=content.replace(word,"@@")
        with open ("k2.txt","w")as f :
            f.write(content)
with open ('this.txt') as f:
    content=f.read()
    
with open ("copy.txt","w") as f:
    copy=f.write(content)
with open ("sample.txt","w") as f:
    f.write("")
 
           





        

