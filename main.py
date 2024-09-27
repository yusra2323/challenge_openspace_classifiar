

import csv
import random as rd
from utils.table import Seat ,Table
from utils.openspace import Openspace 

with open('new_colleagues.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    data=[]
    for row in spamreader:
       data.append(row)
       data = [student for sublist in data for student in sublist]
    data.remove('Duc')
    print(len(data))
     
    print(data)





