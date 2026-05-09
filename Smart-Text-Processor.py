import pyperclip,sys

print(f"{'*'*40:>100}")
print()
print("Smart Text Processor".center(160))
print()
print(f"{'*'*40:>100}\n")


def AddBullet(user_text):
    BulletList=user_text.split("\n")
    for i in range(len(BulletList)):
        BulletList[i]="* "+BulletList[i]
    return "\n".join(BulletList)

def OrderedList(user_text):
    NumberedList=user_text.split("\n")
    str_list=[]
    for x,y in enumerate(NumberedList,1):
        str_list.append(f"{x}. {y}")
    return "\n".join(str_list)
        

def CapitalizeWord(user_text):
    capitalizeWord=user_text.split()
    for i in range(len(capitalizeWord)):
        capitalizeWord[i]=capitalizeWord[i].capitalize()

    return " ".join(capitalizeWord)

def ExtraSpace(user_text):
    return " ".join(user_text.split())

def CountWords(user_text):
    return len(user_text.split())

def ConvertUpper(user_text):
    return user_text.upper()

def ConvertLower(user_text):
    return user_text.lower()

def FindLongest(user_text):
    LongestWord=user_text.split()
    LongestWord.sort(key=len,reverse=True)
    return LongestWord[0]

user_text=pyperclip.paste().strip()
assert bool(user_text),"Enter something!!"

while True:
    try:
        
        print("""
              1.Show Current Text
              2.Add Bullet Points
              3.Add Numbered List
              4.Capitalize Each Word
              5.Remove Extra Spaces
              6.Count Words
              7.Convert to UpperCase
              8.Convert to LowerCase
              9.Find Longest Word
              10.Exit\n
              """)
        
        user_input=int(input(">"))

        if user_input==1:
            print(user_text)
        
        elif user_input==2:
            user_text=AddBullet(user_text)
            print(user_text)
        
        elif user_input==3:
            user_text=OrderedList(user_text)
            print(user_text)
        
        elif user_input==4:
            user_text=CapitalizeWord(user_text)
            print(user_text)
        
        elif user_input==5:
            user_text=ExtraSpace(user_text)
            print(user_text)
        
        elif user_input==6:
            print(CountWords(user_text))
        
        elif user_input==7:
            user_text=ConvertUpper(user_text)
            print(user_text)
        
        elif user_input==8:
            user_text=ConvertLower(user_text)
            print(user_text)
        
        elif user_input==9:
            print(FindLongest(user_text))
        
        elif user_input==10:
            sys.exit()
        
        else:
            raise ValueError("Enter values between 1-10 only!!")
        

    
    except ValueError as v:
        print(v)
    
    except AssertionError as a:
        print(a)

    except Exception as e:
        print(e)


        
        



    














