import os 

lines = None 
gamma = ""
epsilon = ""

dir_path = os.path.dirname(os.path.realpath(__file__))
def read_file(filename):
    global lines
    file_path = dir_path + "\\" + filename
    print(file_path)
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

read_file("input-exercise3.txt")


# PART 1 
# idea : for every column, go through all the rows and count the number of 1s and 0s
for i in range(12):
    # initialize ones and zeroes 
    ones = 0
    zeroes = 0 
    for j in range(len(lines)): 
        if lines[j][i] == "1": 
            ones = ones + 1 
        else: 
            zeroes = zeroes + 1 
    if ones > zeroes: 
        gamma += "1"
        epsilon += "0"
    else: 
        gamma += "0"
        epsilon += "1"

# PART 2 
# determine oxygen generator rating 


    
       

# RESULTS 
print(gamma)
print(epsilon)



