import csv

path = "../data/datause1.csv"
with open(path,'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
