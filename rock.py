import random
print("Rock : 0,paper : 1, scissor : 2")
a=int(input("Enter your choice:"))
if(a>=3 or a<0):
    print("Invalid input--try agin once:")
else:
    b = random.randint(0, 2)
    print(b)
    if(a==b):
        print(" its a Draw")
    elif(a==2 and b==0):
        print(" you lose")
    elif (a == 0 and b == 2):
        print("you win")
    elif(a>b):
        print("You win")
    elif(a<b):
        print("you lose")