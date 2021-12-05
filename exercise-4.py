import os, re

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
read_file("input-exercise4.txt")

board_arr = [] 

# create a Board class 
class Board: 
    def __init__(self, elements, seq): 
        self.elements = elements 
        self.seq = seq # use the sequence number to identify the boards 

# Board class will contain the Board values 
class Board_value: 
    
    def __init__(self, value, boolean, seq): 
        self.seq = seq 
        self.value = value 
        self.boolean = boolean # boolean used to indicate if the number in the board is already in the list 
    
    def get_boolean(self): 
        return self.boolean

    def get_value(self): 
        return self.value

    def set_boolean(self, new_boolean): 
        self.boolean = new_boolean


inputs = lines[0].split(",")
print(inputs)
seq = 0 
for i in range(2,len(lines),6): 
    arr = [] 
    for j in range(5): 
        value = lines[i+j].split(" ")
        print(value)

        # removing the newline 
        res = []
        for sub in value:
            res.append(re.sub('\n', '', sub))   

        value = res
        
        for index in range(5): 
            # print(value[index])
            arr.append(Board_value(value[index], False, i+j))
   
    
    board_arr.append(Board(arr, seq))
    seq+=1 


# ouch at the time complexity 
for i in range(len(inputs)):
    for j in range(len(board_arr)): 
        Board = board_arr[j]

        for k in range(5): 
            # print(Board.elements[k].value)
            if inputs[i] == Board.elements[k].value: 
                Board.elements[k].boolean = True
            
            

            




    






