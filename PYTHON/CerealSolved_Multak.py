import os
import csv

cereal_csv = os.path.join("../Resources", "cereal.csv")

with open (cereal_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    for row in csv.reader:
        if float (row[7]) >= 5:
            print(row[0])
