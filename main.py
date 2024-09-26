

import csv
import random as rd
from utils.table import Seat ,Table
from utils.opernspace import Openspace 

with open('new_colleagues.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    data=[]
    for row in spamreader:
       data.append(row)
    print(data)

list_seats=[]
for name in data:
Seat = Seat()
Seat.set_occupant(name)
list_seats.append(seat)




