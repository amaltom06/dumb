import csv
with open("demo.csv","r") as e_file:
 data=csv.reader(e_file)
 for i in data:
  print(i) 
