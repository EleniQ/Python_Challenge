import os
import csv
#setting variables as I go
monthcount=[]
pl=[]
totalpl=0
changeofpl=[]
totalchangeofpl=0

csv_file=os.path.join(os.getcwd(),'Instructions','PyBank', 'Resources','budget_data.csv')
out_file= os.path.join(os.getcwd(),'Instructions','PyBank','Analysis','out_budget_data.txt')
#used a generator expression to print mounthcount, monthcount is just the number of rows without the header, so skip header
with open(csv_file) as file:
    csv_reader = csv.reader(file, delimiter=","),
    csv_header = next(file)
    monthcount=sum(1 for i in file)
    #print(monthcount) 
    #print(csv_header)--> header has been stored with variable csv_header 
#loop through the data and add to attain total profit 
totalprofit= 0
with open(csv_file) as file:
    csv_reader = csv.reader(file, delimiter=",")
    csv_header = next(file) # skip header

    for row in csv_reader: #create loop 
        
        totalprofit= totalprofit + int(row[1])

#print (totalprofit)
 
with open(csv_file) as file:
    csv_reader = csv.reader(file, delimiter=",")
    csv_header = next(file) # skip header
    for row in csv_reader:
        pl.append([row[0], float(row[1])])  

    for x in range(len(pl)-1):
        changeofpl.append([pl[x+1][0], pl[x+1][1]-pl[x][1]]) #calculate change of profit and add to the changeofpl list 

   #summarise all changes of profit  

    for n in changeofpl:
        totalchangeofpl=totalchangeofpl +n[1]
    
    #print(totalchangeofpl)
    avgplchange=round(totalchangeofpl/len(changeofpl),2) #tried to use total months but new list length is 85, so used len of new list  

    #print outside loop to get final value
    #print(avgprofitlosschange)
#set new variables equal to zero to start off with 
greatin = 0
greatde = 0
increasemonth=0
decreasemonth=0

u=0 
#loop to find greatest increase and greatest decrease and show the corresponding month  
for u in changeofpl:
    if u[1]>greatin: 
        greatin=u[1]
        increasemonth=u[0]
    if u[1]<greatde:
        greatde=u[1]
        decreasemonth=u[0]
#print(increasemonth,greatest_increase)
#print(decreasemonth,greatest_decrease)

#set formatting for printing 

print('Financial Analysis')
print('----------------------------')
print('Total Months: {a}'.format(a=monthcount))
print('Total: ${b}'.format ( b=totalprofit) )
print('Average Change: ${c}'.format(c=avgplchange))
print('Greatest Increase in Profits: {d}  ${e}'.format(d=increasemonth, e=round(greatin)))
print('Greatest Decrease in Profits: {f}  ${g}'.format(f=decreasemonth, g=round(greatde)))

with open(out_file, 'w') as f:
    
    f.write('Financial Analysis\n')
    f.write('----------------------------\n')
    f.write('Total Months: {a}\n'.format(a=monthcount))
    f.write('Total: ${b}\n'.format ( b=totalprofit) )
    f.write('Average Change: ${c}\n'.format(c=avgplchange))
    f.write('Greatest Increase in Profits: {d}  ${e}\n'.format(d=increasemonth, e=round(greatin)))
    f.write('Greatest Decrease in Profits: {f}  ${g}\n'.format(f=decreasemonth, g=round(greatde)))
        
    