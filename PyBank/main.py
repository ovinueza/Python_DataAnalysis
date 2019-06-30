import csv
import os

#Load file
file_to_load = os.path.join("Resources","budget_data.csv")

#Setting variables
total_months = 0
total_pnl = 0

pnl_change = 0
last_pnl = 0
changes_list =[]

greatest_increase = ["", 0]
greatest_decrease = ["", 10000000]

#Read the csv 
with open(file_to_load) as financial_data:
    reader = csv.DictReader(financial_data)   

    for row in reader:
        #calculate total months
        total_months = total_months + 1

        #calculate total profit and loss
        total_pnl = total_pnl + int(row["Profit/Losses"])

        #calculate greatest increase and decrease by comparing to each value in the changes_list
        pnl_change  = int(row["Profit/Losses"]) - last_pnl

        last_pnl = int(row["Profit/Losses"])

        if (pnl_change > greatest_increase[1]):
            greatest_increase[0] = row ["Date"]
            greatest_increase[1] = pnl_change

        if (pnl_change < greatest_decrease[1]):
             greatest_decrease[0] = row ["Date"]
             greatest_decrease[1] = pnl_change 

        changes_list = changes_list + [pnl_change]
           
#calculate net average based on all data compuled in the changes list, excluding the first row
net_average = (sum(changes_list)-changes_list[0])/(len(changes_list)-1)

#Financial Analysis text file
financial_analysis = (
    f"Financial Analysis\n"
    f"------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_pnl}\n"
    f"Average Change: ${net_average:0.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(financial_analysis)

#Output
file_to_output = "financial_analysis.txt"
with open(file_to_output, "w") as txt_file:
    txt_file.write(financial_analysis)