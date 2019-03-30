import os
import csv

file_to_load = os.path.join("Resources","budget_data.csv")
file_to_output = "Resources/budget_analysis.txt"
print(file_to_load)

#Varibles to Track
total_months = 0
total_profit_loss = 0
previous_profit_loss = []
profit_loss_change = 0
highest_increase = ["", 999999999999999]
highest_decrease = ["", 0]
ch_profit_loss = 0
avg_change = 0
average_profit_loss = 0
row_count = 0

with open(file_to_load) as profit_loss_total:
    reader = csv.DictReader(profit_loss_total)
    for row in reader:
        total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
        row_count = row_count + 1
        profit_loss = int(row["Profit/Losses"])

    for i in range (1, profit_loss):
        avg_change = (profit_loss[i+1]/ profit_loss[1])
        average_profit_loss = sum(avg_change)/ row_count

#print (row_count)
#print (total_profit_loss)
#cwd = os.getcwd()
#print(cwd)
with open(file_to_load) as profit_loss_data:
    reader = csv.DictReader(profit_loss_data)

    for row in reader:
        #print(f"{row}")
        total_months = total_months+ 1
        previous_profit_loss = int(row["Profit/Losses"])- 1
        #total_profit_loss = total_profit_loss + int(row["Profit/Losses"])

#print(f"{row}")
        #profit_loss_change = int(row["Profit/Losses",]) - previous_profit_loss
#print(f"{profit_loss_change}")
        #previous_profit_loss = int(row["Profit/Losses"])
#print(f"{previous_profit_loss}")

        # Determine the greatest increase
        if (profit_loss_change > highest_increase[1]):
                highest_increase[1] = profit_loss_change
                highest_increase[0] = row["Date"]

        if (profit_loss_change < highest_decrease[1]):
                highest_decrease[1] = profit_loss_change
                highest_decrease[0] = row["Date"]
        # Add to the revenue_changes list
        #ch_profit_loss.append(row["Profit/Losses"])
        ch_profit_loss = int(row["Profit/Losses"])
        #ch_profit_loss = ch_profit_loss+ 1
    # Set the Revenue average
        #average_profit_loss = (profit_loss_change / row_count)

        #print (profit_loss_change/row_count)
        print (average_profit_loss)

#try:
    #avg_change = (sum(round(changes_profit_loss)/ changes_profit_loss,2))
#except ZeroDivisionError:
    #pass
    #print analysis
print ("Financial Analysis")
print ("------------------------")
print ("Total Months: ", str(total_months))
print ("Total: ", "$ "+ str(total_profit_loss))
print ("Average Change: ","$ " + str(average_profit_loss))
print ("Greatest Increase in Profits: ", str(highest_increase[0])+ " ($" +  str(highest_increase[1]) + ")")
print ("Greatest Decrease in Profits: ", str(highest_decrease[0])+ " ($" +  str(highest_decrease[1]) + ")")

    #print output_file
with open(file_to_output, "w") as txt_file:
    #file=open("",r)
    #for line in file:
    #print line
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_profit_loss))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(ch_profit_loss / total_profit_loss))
        #txt_file.write("Average Change: " + "$" + str(round(sum(changes_profit_loss) / len(str(changes_profit_loss)),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(highest_increase[0])+ " ($" +  str(highest_increase[1]) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(highest_decrease[0]) + " ($" + str(highest_decrease[1]) + ")")
