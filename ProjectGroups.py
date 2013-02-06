import csv
with open("ProjectGroups.csv", "wb") as out:
    fileWriter = csv.writer(out, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    with open('ProjectGroups.txt', 'rb') as f:
        for row in csv.reader(f, delimiter=','):   
            fileWriter.writerow(row)

