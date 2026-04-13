import random
print("Stone,Paper and Scissors game!!")

print()

while True:
    print("For how much score you wanna compete?")
    final_score=int(input(">"))
    print()
    comp_score=0
    user_score=0
    
    for x in range(final_score):
        comp_move=random.randint(1,3)
        sto,pap,sci=1,2,3
        print("computer chose it's move now,choose yours!")
        print()
        user_input=input("Enter your move (stone,paper or scissor):")
       
        if user_input=="stone"and comp_move is pap:
            comp_score+=1
            user_score+=0
            print(f"user:{user_input}\ncomputer:paper")
            print(f"It's {user_score} - {comp_score}")
            continue

        elif user_input=="stone"and comp_move is sci:
            comp_score+=0
            user_score+=1
            print(f"user:{user_input}\ncomputer:scissor")
            print(f"It's {user_score} - {comp_score}")
            continue

        elif user_input=="paper" and comp_move is sto:
            comp_score+=0
            user_score+=1
            print(f"user:{user_input}\ncomputer:stone")
            print(f"It's {user_score} - {comp_score}")
            continue

        elif user_input=="paper" and comp_move is sci:
            comp_score+=1
            user_score+=0
            print(f"user:{user_input}\ncomputer:scissor")
            print(f"It's {user_score} - {comp_score}")
            continue

        elif user_input=="scissor" and comp_move is sto:
            comp_score+=1
            user_score+=0
            print(f"user:{user_input}\ncomputer:stone")
            print(f"It's {user_score} - {comp_score}")
            continue

        elif user_input=="scissor" and comp_move is pap:
            comp_score+=0
            user_score+=1
            print(f"user:{user_input}\ncomputer:paper")
            print(f"It's {user_score} - {comp_score}")
            continue

        else:
            comp_score+=0
            user_score+=0
            print(f"user:{user_input}\ncomputer:{user_input}")
            print(f"It's {user_score} - {comp_score}")
            continue
    else:
        if user_score>comp_score:
            print("User wins!")
        elif user_score<comp_score:
            print("Computer wins!")
        else:
            print("It's a tie")
        choice=int(input("Press 1 to continue and 2 to exit the game:"))
        if choice==2:
            break
            
            
            
            
            
            
        
    
    
    
    
