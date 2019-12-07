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
    data = list(csvreader) # convert to list to use 2 for loops
    months_total = 0
    my_sum = 0
    change_sum = 0
    max = data[0] # set first row from the file as max
    
    for index, row in enumerate(data):
        change = int(row[1]) - int(data[index - 1][1] or 0)
        months_total += 1
        
        my_sum += int(row[1]) # count total
        if index > 0: change_sum += change # when value is empty count it as zero
        if int(row[1]) > int(max[1]): max = row # if current row is greater than max, save it as max and compare with new value at next iteration
        
    min = max # set min as max
    for row in data:
        if int(row[1]) < int(min[1]): min = row # if current row is less then min, save it as min and compare with new value at next iteration
              
print("Total months: " + str(months_total)) #this runs only once after the loop completes
print("Total: " + "$" + str(my_sum))
print("Average  Change: " + "$" +  str( round(change_sum / (months_total - 1), 2)))
print ("Greatest Increase in Profits: " + max[0] + " ($" + max[1] + ")")
print ("Greatest Decrease in Profits: " + min[0]+ " ($" + min[1] + ")")