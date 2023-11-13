import csv
import pandas as pd
field=['rollno','name','age']
sdict=[{'rollno':7,'name':"amal",'age':37},
       {'rollno':10,'name':"tom",'age':34}]
with open("vpt.csv",'w')as dfile:
     writer=csv.DictWriter(dfile,fieldnames=field)
     writer.writeheader()
     writer.writerows(sdict)
data=pd.read_csv("vpt.csv")   
print(data)  
   
     

