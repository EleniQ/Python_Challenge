import os 
import csv 
#print("----------------") Setting my in and out filepaths, had a lot of issues with this due to my onedrive so used the os.getcwd command
csv_file= os.path.join(os.getcwd(),'Instructions','PyPoll','Resources','election_data.csv')
out_file= os.path.join(os.getcwd(),'Instructions','PyPoll','Analysis','out_election_data.txt')
#print(csv_file)


def func():#used this function to insert into my loop
    for row in namelist: 
        if row[0] == col[2]: 
            row[1]=row[1]+1
            return (0)
    namelist.append([col[2],1,0]) #adding name, votes, space for %
    
    
def srt (e): #basic sort function as when I tried to use max, it placed the wrong canidate first (based off name)  
    return (e[1])
    
namelist =[]#creation of new list in which my data will store 
#open file 'with open' so no close reqyired, set csv_reader to read file with the , as the delimiter. Skip and store the header. 
with open(csv_file,'r') as file: 
    csv_reader = csv.reader(file, delimiter=",")
    csv_header = next(file) # skip header
    for col in csv_reader: 
       
        func()# run my function 
    totalvotes= sum(x[1] for x in namelist)# can find total votes now from the list of 3, adding those instead of cycling through whole list individually. 
    for x in namelist:
        x[2]= round((x[1]/ totalvotes)*100,3)#works out percentage of votes for each candidate, rounds to 3 dp
    namelist.sort(key=srt, reverse=True)#sorts list via top result using my srt function 
    Winner= (namelist[0])
    #This section prints all results and exports all data to a txt.file that shows exactly how it does on the readme. I have use the format function. 
print('Election Results')
print('----------------------')
print('Total Votes: {a}'.format(a=totalvotes))
for row in namelist: #goes through the shorter list I made to assign the correct results as I did not give variables 
    print('{a}: {b}% ({c}) '.format(a=row[0],b=row[2],c=row[1]))
    
print('----------------------')
print('Winner: {a}'.format(a=Winner[0]))
print('----------------------')

with open(out_file, 'w') as f:
    
    f.write('Election Results\n')
    f.write('----------------------\n')
    f.write('Total Votes: {a}\n'.format(a=totalvotes))
    for row in namelist: 
        f.write('{a}: {b}% ({c})\n'.format(a=row[0],b=row[2],c=row[1]))
        
    f.write('----------------------\n')
    f.write('Winner: {a}\n'.format(a=Winner[0]))
    f.write('----------------------\n')