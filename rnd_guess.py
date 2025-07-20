import random
x= random.randint(1,101)
y=int(input("Enter your guess here: "))
while(x!=y):
    if x>y:
        print("Your guess is lower than the generated number.")
    elif x<y:
        print("Your guess is higher than the generated number.")
    y=int(input("Enter your guess here: "))
print("You guessed correctly!")