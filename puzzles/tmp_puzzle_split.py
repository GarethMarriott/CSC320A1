# Created by Gareth Marriott
# V00875748

import fileinput
from pprint import pp



puzzles = []
cur_puz = ""
for line in fileinput.input():
    if line[0] == "G":
        puzzles.append(cur_puz)
        cur_puz = ""
    else:
        cur_puz += line

pp(puzzles)

for i,puz in enumerate(puzzles):
    f = open("puzzle"+str(i)+".txt", "a")
    f.write(puz)
    f.close()
