# Unit 3 Homework: Python

Completed two assignments for module 3. 

# Steps

I completed PyPoll first as I found this easier to complete and was able to use less variables in the code. 
PyBank required me to set more variables as I struggled to complete the averages and greatest increase and decrease without them.


# What I have done 
## PyPoll
I have created a code that efficiently returns a good chunk of the required data using a function, and then created a new list (namelist) for my information to be stored in.
I then created a sort function to order the code to produce the winner. 
All of this data prints within the terminal, has been debugged, and produced a txt.file in the Analysis folder. 

The Results you will see in terminal and in the txt.file are: 

Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------


## PyBank 

I started out by using a generator expression to find the rows.
This part was simpler, but then I realised it would be far more easy going for me to assign variables when proceeding to get Total, Average Change, Greatest Increase and Greatest Decrease. I utlised them through the creation of lists, pl and changeofpl.
I think this code is far less efficient then my PyPoll code as it stores quite a few variables. 

The Results you will see in terminal and in the txt.file are:

  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  
## For Additiona detail on the code, please check the main.py file within PyBank and PyPoll folders. 
The txt.file can be found in the Analysis folder within their respective folders.
The original CSV resource can be found within the respective folder too. 



