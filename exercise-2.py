import os 

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

read_file("input-exercise2.txt")

horizontal = 0 
depth = 0 
aim = 0
for i in range(len(lines)): 

    arr = lines[i].split(" ")
    direction = arr[0]
    magnitude = arr[1]
    if direction == "forward": 
        horizontal += int(magnitude)
        amount = aim*int(magnitude)
        depth += amount
    if direction == "up":
        # depth -= int(magnitude) 
        aim -= int(magnitude)
    if direction == "down":
        # depth += int(magnitude)
        aim += int(magnitude)

print("Horizontal:{0}, Depth:{1}".format(horizontal, depth))
result = horizontal * depth 
print(str(result))


