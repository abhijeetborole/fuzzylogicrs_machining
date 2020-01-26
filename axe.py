import csv
x = 0
my_dict = {}
with open('AdSp.txt', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter="\t")
    for line in csv_reader:
        x += 1
        if(x == 1):
            continue
        print(line[0])
        print(float(line[173].replace(',', '')))
        print(x)
        print(float(line[0]))
