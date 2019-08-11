# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('', 'Resources','election_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    #csvreader = csv.reader(csvfile, delimiter=',')
    csvreader = csvfile.read()
    #print(csvreader)
    table = [row.split(',') for row in csvreader.split('\n')]
    #print(table) 
i=1
total = 0
current_value = 0
length = len(table)
# * The total number of months included in the dataset
#print(f"total number of months included in the dataset: {length}")
candidate_cnt = []
candidate = []
#print("length of excel :",length)
#reading Excel File
for i in range(1,length-2):
    #print ("Excel row:",i)
    if i == 1:
        #print("row 1")
        candidate_name = table[i][2]
        candidate_vote_count = 1
        #print(candidate_name)
        candidate.append(candidate_name)
        candidate_cnt.append(candidate_vote_count) 
        #print("candidate:",candidate)
        #print("candidate_cnt:",candidate_cnt)
    elif i > 1:
        candidate_name = str(table[i][2])
        if i == (length-1):
            candidate_name = candidate_name + '\r'
        #print("elif ", "Excel row count:",i)
        #print("searching for candidate:",candidate_name)
        candidate_found="n"
        #loop for candidate list
        for j in range(0,len(candidate)):
            #print("index of candidate list: ", j)
            if candidate_name == candidate[j]:
                candidate_found = "y"
                #print ("candidate found in list")
                #print ("candidate list index:", j)
                current_candidate_vote_cnt = candidate_cnt[j]
                candidate_cnt[j] = current_candidate_vote_cnt + 1
                #print ("current_candidate_vote_cnt :", current_candidate_vote_cnt)
                #print("candidate_cnt :", candidate_cnt[j])
                break
                #else continue "for loop"
            else:
                continue
        if candidate_found == "n":
                candidate.append(candidate_name)
                candidate_cnt.append(1)
print ("Final List")
print("candidate list:", candidate)
print ("candidate cnt:", candidate_cnt)
tot_votes = ("Total Votes: " , sum(candidate_cnt))
print(tot_votes)   
max_vote = max(candidate_cnt) 
#print(max_vote)
for k in range(0,len(candidate_cnt)):
    if max_vote == candidate_cnt[k]:
        win = ("Winner :", candidate[k])
        #print(win)
# Define path to output file my_analysis.txt
output_path = os.path.join('', 'Resources', "my_PyPoll_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:
     # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter='\n')
    csvwriter.writerow("Election Results")
    csvwriter.writerow("-----------------------------------------")
    csvwriter.writerow(tot_votes)
    csvwriter.writerow("-----------------------------------------")
    for j in range(0,len(candidate)):
        str1 = (candidate[j], " : ",)
        str2 = ((round(candidate_cnt[j]/sum(candidate_cnt),2))*100, "% (", candidate_cnt[j], ")")
        str3 = str1 + str2
        csvwriter.writerow(str3)
    csvwriter.writerow("-----------------------------------------")
    csvwriter.writerow(win)
    csvwriter.writerow("-----------------------------------------")
# For window users only
#!explorer .    