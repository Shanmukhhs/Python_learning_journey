def collatz(num):
    while num!=1:
        if num%2==0:
            num=num//2
            print(num,end=" ")
        elif num%2==1:
            num=(num*3)+1
            print(num,end=" ")
try:
    user_input=int(input("Enter a number:"))
    collatz(user_input)
except Exception as e:
    print("Enter a integer.")
        

     
    
