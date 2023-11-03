import csv

file="carsales.csv"

fields=[]
rows=[]
temp=[]
with open(file,"r") as csvfile:

    reader=csv.reader(csvfile)
    '''fields = next(reader)
 
    # extracting each data row one by one
    for row in reader:
        rows.append(row)'''
        
    for row in reader:
        temp.append(row)
        
    for i in range(0,len(temp),2):
        fields.append(temp[i])
        rows.append(temp[i+1])
 
    
print (fields)

for i in range(len(rows)):
    rows[i]=list(map(int,rows[i]))
    
#print(rows)

totalByYear=0
#totalByBrand=0
for i in range(len(rows[0])):
    totalForMonth=0
    for r in (rows):
        totalForMonth+=r[i]
        
    print(f"month {i} made {totalForMonth} across all brands")
    totalByYear+=totalForMonth
    

print("\n\nthe year sales so far is ", totalByYear,"\n\n")

for i in range(len(rows)):
    brand =str(fields[i][0]).replace("\t","")
    print(f"the total sales for the brand {brand} is {sum(rows[i])}")