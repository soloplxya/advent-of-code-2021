import os, re

line = None 

dir_path = os.path.dirname(os.path.realpath(__file__))
def read_file(filename):
    global line
    file_path = dir_path + "\\" + filename
    print(file_path)
    text_file = open(file_path, "r")
    line = text_file.read()

read_file("input-exercise6.txt")


# create an array of fishes and doing some preprocessing 
fishes = [int(lanternfish) for lanternfish in line.split(",")]

print(fishes)


day = 0
# use a while loop to keep track of the days 
while (day < 80): 
    to_add = 0
    for i in range(len(fishes)): 
        # if the internal timer of the fishes not equal to zero 
        if fishes[i] > 0: 
            fishes[i] = fishes[i] - 1 
        # if the internal timer of the fishes equal to zero 
        else: 
            # when the internal timer of the fishes hit zero, zero becomes a 6
            fishes[i] = 6
            # a new 8 is added to the back of the list 
            to_add += 1 
            
    # print(to_add)
    # add the fishes that are born into the fishes array 
    for i in range(to_add): 
        fishes.append(8)

    # increment the day 
    day += 1 
print(len(fishes))

     