#write a pgm to copy odd lines of the file stud.txt to odd.txt and copy the even lines of the file to even.txt
f_file=open("stud.txt","r")
o_file=open("odd.txt","w")
e_file=open("even.txt","w")
content=f_file.readlines()
o_content=[x.strip() for x in content]
print("The contents of the file are")
print(o_content)
for i in range(len(o_content)):
 if(i%2==0):
  e_file.write(o_content[i])
 else:
  o_file.write(o_content[i]) 
f_file.close()
o_file.close()
e_file.close() 
odd=open("odd.txt","r")  
odd_content=odd.readlines()
print("Odd line of the file are")  
print(odd_content)  




