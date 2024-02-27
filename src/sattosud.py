# Created by Gareth Marriott
# V00875748

import fileinput
# from pprint import pp


# def convert_grid_to_val(i,j,num):
#     return (81*(i-1))+(9*(j-1))+(num-1)+1

def convert_val_to_grid(num):
    num = int(num)-1
    i = int(num / 81)+1
    j = int(num / 9)+1
    val = (num % 9)+1
    return (i,j,val)

sat = ""
for line in fileinput.input():
    sat += line.replace("\n"," ")
sat = sat.split(" ")
# pp(sat)

sud = ""
for clause in sat:
    try:
        c = int(clause)
        if c > 0:
            sud += str(convert_val_to_grid(int(clause))[2])
    except ValueError:
        pass

for i,char in enumerate(sud):
    if i%3 == 0:
        print(" ",end="")
    if i%9 == 0:
        print()
    print(char,end="")
print()