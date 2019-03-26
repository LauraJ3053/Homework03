import csv

csv_path = os.path.join( ..\Resources\budget_data.csv)

#Varibles to Track
total_months = 0
total_profit_loss = 0



with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
	
	for row in csvreader:
	
		total_months = total_months +1
		total_profit_loss = total_profit_loss + int(row["Profit and Loss"]
		
		Print months