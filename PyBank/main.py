# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('', 'Resources', 'budget_data.csv')
# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csvfile.read()
    table = [row.split(',') for row in csvreader.split('\n')]
    #print (table) 
    i=1
total = 0
current_value = 0
length = len(table) - 2
# * The total number of months included in the dataset
#print(f"total number of months included in the dataset: {length}")
tot_mnths = "Total Months: " + str(length)
print(tot_mnths)

# * The net total amount of "Profit/Losses" over the entire period
total_monthly_change = []
Month_year = []
profit_loss = []
monthly_change = 0
for i in range(1,(length+1)):
    if i == 0:
        last_value = 0
        current_value = 0        
    elif i == 1:
        current_mnth_yr = (table[i][0])
        current_profit_loss = (table[i][1])
        profit_loss.append(int(current_profit_loss))
        Month_year.append(current_mnth_yr)
    elif i > 1:
        last_value = (table[i-1][1])
        current_value = (table[i][1])
        current_mnth_yr = (table[i][0])
        Month_year.append(current_mnth_yr)
        current_profit_loss = (table[i][1])
        profit_loss.append(int(current_profit_loss))
        #print(profit_loss)
        monthly_change = (int(current_value)- int(last_value))
    total_monthly_change.append(monthly_change) 
prt_tot = sum(profit_loss)
#print(f"Total Monthly Change list : {str(prt_tot)}")
print_total_change = "Total :" + str(prt_tot)
print(print_total_change)
#  * The average of the changes in "Profit/Losses" over the entire period
def mean(numbers):
    return float(sum(numbers)) / max((len(numbers)-1), 1)
Average = mean(total_monthly_change)
prt_avg = "Average  Change: $" + str(Average)
print(prt_avg)
#  * The greatest decrease in losses (date and amount) over the entire period
minimum = 0
minimum = min(total_monthly_change)
min_index = total_monthly_change.index(minimum)
min_date = Month_year[min_index]
prt_min = "Greatest Decrease in Profits:" + str(min_date)+ "  " + str(minimum)
print(prt_min)
#  * The greatest increase in profits (date and amount) over the entire period
maximum = 0
maximum = max(total_monthly_change)
max_index = total_monthly_change.index(maximum)
max_date = Month_year[max_index]
prt_max = "Greatest Increase in Profits :" + str(max_date)+ "  " + str(maximum)
print(prt_max)
# Define path to output file my_analysis.txt
output_path = os.path.join('', 'Resources', "my_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:
     # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter='\n')
    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow("-----------------------------------------")
    csvwriter.writerow(tot_mnths)
    csvwriter.writerow(print_total_change)
    csvwriter.writerow(prt_avg)
    csvwriter.writerow(prt_min)
    csvwriter.writerow(prt_max)
    csvwriter.writerow("-----------------------------------------")
    
# For window users only
#!explorer .