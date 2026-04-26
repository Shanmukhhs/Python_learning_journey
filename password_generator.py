import sys, random

print("Password generator")
print()

alpha_low = [x for x in "abcdefghijklmnopqrstuvwxyz"]
alpha_upp = [y.upper() for y in "abcdefghijklmnopqrstuvwxyz"]
special_char =[z for z in "!@#$%^&*()-_+=[]{}|:,.<>?/~"]
num_char = [str(w) for w in range(10)]

total_list = alpha_low + alpha_upp + special_char + num_char

partial_list=alpha_low + alpha_upp + num_char

storage = []

try:
    while True:
        password = ""
        
        user = int(input("Enter the length of password: "))
        
        if user <= 0:
            raise ValueError("Length must be positive!")
        user_1=input("\nDo you want to use special characters? (y/n) :")
        user_1=user_1.lower()
        
        if user_1=="y":
            chosen_list=total_list
        
        elif user_1=="n":
            chosen_list=partial_list

        else:
            raise ValueError(" Enter (y/n) only!!")
            
        for i in range(user):
            password+=random.choice(chosen_list)
            

        print("Generated password:", password)
        
        storage.append(password)
        
        print("\n1 -> Restart\n2 -> Quit\n3 -> Show stored passwords")
        flow = int(input("> "))
        
        if flow == 1:
            continue
        elif flow == 2:
            sys.exit()
        elif flow == 3:
            print("Stored passwords:", storage)
        else:
            raise ValueError("Enter 1, 2 or 3 only!")

except ValueError as v:
    print(v)

except Exception as e:
    print(f"Oops something went wrong: {e}")

finally:
    print("Thank you!")