import os, re

dir_path = os.path.dirname(os.path.realpath(__file__))
def read_file(filename):
    global lines
    file_path = dir_path + "\\" + filename
    print(file_path)
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()
read_file("input-exercise5.txt")


''' Preprocessing '''

# get largest X,Y values in the array to determine the width of the 2D virtual board to build 
def get_largest(array): 
    largest_X = -1000
    largest_Y = -1000
    for i in range(len(array)): 
        start_end_coordinates = array[i].split('->')
        start_coordinates = start_end_coordinates[0]
        end_coordinates = start_end_coordinates[1]
        start_X = int(start_coordinates.split(',')[0])
        start_Y = int(start_coordinates.split(',')[1])
        end_X = int(end_coordinates.split(',')[0])
        end_Y = int(end_coordinates.split(',')[1])

        if (start_X > largest_X): 
            largest_X = start_X
            if (end_X > largest_X): 
                largest_X = start_X
        
        if (start_Y > largest_Y): 
            largest_Y = start_Y
            if (end_Y > largest_Y): 
                largest_Y = start_Y

    return (largest_X, largest_Y)


def get_XY(line): 
    start_end_coordinates = line.split('->')
    start_coordinates = start_end_coordinates[0]
    end_coordinates = start_end_coordinates[1]
    start_X = int(start_coordinates.split(',')[0])
    start_Y = int(start_coordinates.split(',')[1])
    end_X = int(end_coordinates.split(',')[0])
    end_Y = int(end_coordinates.split(',')[1])
    return (start_X, start_Y, end_X, end_Y)


def is_diagonal(start_X, start_Y, end_X, end_Y): 
    if abs(start_X - end_X) == abs(start_Y - end_Y):
        return True 
    else: 
        return False

# check if the line is horizontal 
def is_horizontal(start_X, start_Y, end_X, end_Y): 
    return start_X == end_X

# check if the line is vertical 
def is_vertical(start_X, start_Y, end_X, end_Y): 
    return start_Y == end_Y

# return the absolute of the difference between the start point and the end point 
def get_difference(start_point, end_point): 
    return abs(start_point - end_point)

# build 2D array that is filled with zeroes 
def build_2D_array(largest_X, largest_Y): 
    arr = [[0 for i in range(largest_Y)] for j in range(largest_X)]
    return arr 

# count number of elements
def count(array): 
    count = 0
    for r in range(len(array)): 
        for c in range(len(array[0])): 
            if array[r][c] >= 2: 
                count += 1
    return count 



# build two dimensional array 
two_dimen_arr = build_2D_array(1000, 1000)
print(len(two_dimen_arr))
print(len(two_dimen_arr[0]))


'''Actual Calculations'''
for i in range(len(lines)): 
    # print(lines[i])
    value = get_XY(lines[i])
    start_X, start_Y, end_X, end_Y = value
    # check if the line is either horizontal or vertical as per the question 
    if is_horizontal(start_X, start_Y, end_X, end_Y) or is_vertical(start_X, start_Y, end_X, end_Y): 

        if is_horizontal(start_X, start_Y, end_X, end_Y): 
            difference = get_difference(start_Y, end_Y)
    
            for j in range(difference+1): 
                if start_Y > end_Y: 
                    two_dimen_arr[start_X][start_Y - j] += 1
                else:
                    two_dimen_arr[start_X][start_Y + j] += 1

        if is_vertical(start_X, start_Y, end_X, end_Y):
            difference = get_difference(start_X, end_X)
            for j in range(difference+1): 
                if start_X > end_X: 
                    two_dimen_arr[start_X - j][start_Y] += 1
                else: 
                    two_dimen_arr[start_X + j][start_Y] += 1
        
        if is_diagonal(start_X, start_Y, end_X, end_Y): 
            # case 1 the centre diagonal 
            difference = get_difference(start_X, start_Y)
            for j in range(difference + 1): 
                if start_X > end_X: 
                    two_dimen_arr[start_X - j][start_Y + j] += 1
                else: 
                    two_dimen_arr[start_X + j][start_Y - j] += 1
            



                
                    

# results 
print(count(two_dimen_arr))

