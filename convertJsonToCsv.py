import json
import csv

f = open("test.json");
employee_parsed  = json.load(f);
emp_data = employee_parsed['employee_details']

#open a file for writing
employ_data = open('test.csv','w')

#create the csv writer object
csvwriter = csv.writer(employ_data)

count = 0

for emp in emp_data:
    if (count==0):
        header = emp.keys()
        csvwriter.writerow(header)
        count+=1
    csvwriter.writerow(emp.values())

#close the file
employ_data.close()