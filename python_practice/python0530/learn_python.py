with open('learn.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    line1 =line.replace('Python','C')
    print(line1.rstrip())