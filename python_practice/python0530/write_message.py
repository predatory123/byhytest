test = 'popular.txt'
with open(test,'w') as file_object:
    file_object.write('I love python.\n')
    file_object.write('I love java too.\n')

with open(test,'a') as file_object:
    file_object.write('she love python.\n')
    file_object.write('she love java too.')


# with open('popular.txt') as file_object:
#     testing = file_object.read()
#     print(testing)