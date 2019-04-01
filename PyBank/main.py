# naming dependencies
import os
import csv

# files to load
file_to_load = os.path.join("PyBank","Resources","budget_data.csv")
file_to_output = "PyBank/Resources/budget_analysis.txt"
#print(file_to_load)

# checking pathway
#cwd = os.getcwd()
#print(cwd)

# varibles
total_months = 0
total_pl = 0
prev_pl = 0
pl_change = 0
grtst_increase = ["", float]
grtst_decrease = ["", float]
pl_changes = []

# reading files
with open(file_to_load) as budget_data:
    reader = csv.DictReader(budget_data)
    #print(budget_data)

# looping through data
    for row in reader:
        #print(f"{row}")

# calculating the totals
        total_pl = total_pl + int(row["Profit/Losses"])
        total_months = total_months+ 1

# getting changes in profit and loss
        pl_change = int(row["Profit/Losses"[1]])- prev_pl
        #print (pl_change)

# resetting the value of previous profit and loss
        prev_pl = -int(row["Profit/Losses"])
        #print (pl_change)

# determining greatest increase
    def gr_increase_function(pl_change):
        max_value = None
        for i in pl_change:
            if not max_value:
                max_value = value
            elif value > max_value:
                max_value = value
        return max_value

# determining greatest decrease
    def gr_decrease_function(pl_change):
        min_value = None
        for j in pl_change:
            if not min_value:
                min_value = value
            elif value > min_value:
                min_value = value
        return min_value

# add to the profit and loss changes list
        pl_changes.append(int(row["Profit/Losses"]))
        #Print (pl_changes)

# Set the profit and loss average
        pl_avg = sum(pl_changes) / len(pl_changes)



# to print analysis
print ("Financial Analysis")
print ("------------------------")
print ("Total Months: ", str(total_months))
print ("Total: ", "$ "+ str(total_pl))
print ("Average Change: ","$ " + str(pl_avg))
print ("Greatest Increase in Profits: ", str(grtst_increase[0])+ " ($" +  str(grtst_increase[1]) + ")")
print ("Greatest Decrease in Profits: ", str(grtst_decrease[0])+ " ($" +  str(grtst_decrease[1]) + ")")

# file to output
with open(file_to_output, "w") as txt_file:
    #file=open("",r)
    #for line in file:
    #print line
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_pl))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(pl_change / total_pl))
    txt_file.write("Average Change: " + "$" + str(round(sum(pl_changes) / len(str(pl_changes)),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(grtst_increase[0])+ " ($" +  str(grtst_increase[1]) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(grtst_decrease[0]) + " ($" + str(grtst_decrease[1]) + ")")
