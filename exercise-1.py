import os 
# initialize variables 
count = 0 
lines = None 

dir_path = os.path.dirname(os.path.realpath(__file__))
def read_file(filename):
    global lines
    file_path = dir_path + "\\" + filename
    print(file_path)
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()
    return lines

read_file("input-exercise1.txt")

for i in range(len(lines) - 1):  
    if int(lines[i+1]) > int(lines[i]): 
        count = count + 1 

print(str(count))