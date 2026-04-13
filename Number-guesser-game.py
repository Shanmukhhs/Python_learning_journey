import random
print("Number guessing game!")
print()
while True:
    print("I am thinking of a number between 1-20,try to guess it in four turns!")
    random_num=random.randint(1,20)
    for i in range(4):
        user_input=int(input(">"))
        if user_input>random_num:
            print("Your number is too high!")
            continue
        elif user_input<random_num:
            print("Your number is too low!")
            continue
        elif user_input==random_num:
            print("You got it correct!")
            break
    else:
        print(f"You lost! I was thinking of {random_num}")
    print("Press 1 to continue and 2 to quit")
    choice=int(input(">"))
    if choice==2:
        break

            
