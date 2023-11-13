f=open("demo.txt","r")
f1=open("demo3.txt,"w")


l=f.readline()

while l:
   f1.write(l)
   
f1=open("demo3.txt","r")
print(f1.read())   


