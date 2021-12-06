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

    def get_score(self, bingo_number): 
        unmarked = 0 
        for i in range(len(self.elements)): 
            for j in range(len(self.elements[0])): 
                if self.elements[i][j].boolean == False: 
                    unmarked += self.elements[i][j].value 
        return unmarked*bingo_number 

        

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
# print(inputs)
seq = 0 
for i in range(2,len(lines),6): 
    arr = [] 
    for j in range(5): 
       
        row = lines[i+j].split(" ")
        # removing the newline 
        res = []
        for sub in row:
            res.append(re.sub('\n', '', sub))   
        row = res
        row = [Board_value(item, False, i+j) for item in row]
        arr.append(row)
        #print(len(arr))
   
    
    board_arr.append(Board(arr, seq))
    seq+=1 


# ouch at the time complexity 
for i in range(len(inputs)):
    for j in range(len(board_arr)): 
        Board = board_arr[j]
        
        
        for r in range(5): 
            # print(Board.elements[k][a].value)
            for c in range(5):
                print(Board.elements[r][c].value)
                if inputs[i] == Board.elements[r][c].value: 
                    Board.elements[r][c].boolean = True
          
            
# time to check for bingo 
for i in range(len(board_arr)): 
    board = board_arr[i]
    bingo = True 
    

    # fixed row 
    row = 0
    for c in range(len(board.elements[0])): 
        if board.elements[row][c].boolean == True: 
            bingo = bingo & True 
        else: 
            bingo = bingo & False 
        row += 1 



    # fixed col 
    col = 0
    for r in range(len(board)): 
        if board.elements[r][col].boolean == True: 
            bingo = bingo & True 
        else: 
            bingo = bingo & False 
        col += 1 


    print(bingo)

        



            
            

            




    






