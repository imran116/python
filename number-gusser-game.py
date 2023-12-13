import random

random_number = random.randint(1, 50)
print("-------WELCOM TO NUMBER GUSSER GAME--------")
print("-------------------------------------------")
for i in range(1,6):
    print("Attempt [{} of 5]".format(i))
    inputNumber = int(input("Enter a Guess Number[1-50]:-- "))
    
    if(inputNumber == random_number):
        print("You Won!!")
        break
    elif(inputNumber>random_number):
        print("Oh,no You Choose a larger number,guess small number.\n")
    else:
        print("Oh,no You Choose a small number,guess big number.\n")

print("You Loose!!")
print("The Guess Number is: "+str(random_number))

