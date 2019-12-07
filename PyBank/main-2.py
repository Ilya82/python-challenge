# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")
print("----------------------------")

#1
with open(csvpath, 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    months_total = 0
    for row in csvreader:
        months_total += 1  #print(current_total) #this runs every time the loop runs
    print("Total months: " + str(months_total)) #this runs only once after the loop completes

#2  
with open(csvpath, 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    my_sum = 0
    for row in csvreader:
        my_sum = my_sum + int(row[1])
    print("Total: " + "$" + str(my_sum)) 

#3
with open(csvpath, 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    header = next(csvreader)
    change_sum = 0
    for row in csvreader:
        change_sum = change_sum + int(row[2])

average_change = round((change_sum / (months_total-1)),2)
print("Average  Change: " + "$" +  str(average_change))

max_profit = max(change_sum)
print ("Greatest Increase in Profits: " + str(max_profit)