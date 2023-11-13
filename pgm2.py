#write a pgm to copy odd lines of the file stud.txt to odd.txt and copy the even lines of the file to even.txt
f_file=open("stud.txt","r")
o_file=open("odd.txt","w")
e_file=open("even.txt","w")
content=f_file.readlines()
print("The contents of the file are")
main=[x.strip() for x in content]
print(main)
for i in range(len(content)):
 if(i%2==0):
  o_file.write(content[i])
 else:
  e_file.write(content[i]) 
f_file.close()
o_file.close()
e_file.close() 
odd=open("odd.txt","r")  
odd_content=odd.readlines()
print("Odd line of the file are")  
oc=[x.strip() for x in odd_content]
print(oc)  
even=open("even.txt","r")  
even_content=even.readlines()
print("Even line of the file are") 
ec=[x.strip() for x in even_content]
print(ec)  
  




