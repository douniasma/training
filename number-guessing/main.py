import random

random_number = random.randint(1, 1000)

num=-1  
while num != random_number:
    print("enter num: ")
    num =int(input()) 
    if num >1000 or num<1:
        print('FAIl')
    if num == random_number: 
        print('go girl')
    if num > random_number: 
        print('too big')
    if num < random_number:
        print('too small')
print('slay')