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
    print(len(lines))
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
ogr = lines 
j = 0
while (len(ogr) > 1):
    # iterate through the rows
    ones = 0
    zeroes = 0
    new_array = []

    for i in range(len(ogr)): 
        print(i)
        # print(ogr[i])
        if ogr[i][j] == "1": 
            ones = ones + 1 
        elif ogr[i][j] == "0": 
            zeroes = zeroes + 1 
    

    # if ones greater than zeroes or number of ones equals to zero
    if (ones > zeroes) or (ones == zeroes): 
        #print('a')
        for i in range(len(ogr)): 
            if ogr[i][j] == "1": 
                new_array.append(ogr[i])
    else: 
        #print('b')
        for i in range(len(ogr)): 
            if ogr[i][j] == "0": 
                new_array.append(ogr[i])
    ogr = new_array
    j = j + 1 

    print(ogr)

   



# csr 
csr = lines 
j = 0
while (len(csr) > 1):
    # iterate through the rows
    ones = 0
    zeroes = 0
    new_array = []

    for i in range(len(csr)): 
        print(i)
        # print(ogr[i])
        if csr[i][j] == "1": 
            ones = ones + 1 
        elif csr[i][j] == "0": 
            zeroes = zeroes + 1 
    

    # if ones greater than zeroes or number of ones equals to zero
    if (ones > zeroes) or (ones == zeroes): 
        #print('a')
        for i in range(len(csr)): 
            if csr[i][j] == "0": 
                new_array.append(csr[i])
    else: 
        #print('b')
        for i in range(len(csr)): 
            if csr[i][j] == "1": 
                new_array.append(csr[i])
    csr = new_array
    j = j + 1 

   

        



    
       

# RESULTS 
print(ogr)
print(csr)
   
print(gamma)
print(epsilon)



