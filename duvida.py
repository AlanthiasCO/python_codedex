import random

names = ['Rasheed', 'Thomas', 'Mister', 'Kevin', 'Ron', 'Alvester']
count = 0

while count < 10:
    random_number = random.randint(1, 6)
    
    if random_number == 1:
        print('Rasheed')
    elif random_number == 2:
        print('Thomas')
    elif random_number == 3:
        print('Mister')
    elif random_number == 4:
        print('Kevin')
    elif random_number == 5:
        print('Ron')
    else:
        print('Alvester')
    
    #count += 1