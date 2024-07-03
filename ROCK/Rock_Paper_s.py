
import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False
    
print("Computer turn : Rock(r) Paper(p) or Scissior(s) ?")
randno = random.randint(1,3)

if randno==1:
        comp='r'
elif randno==2:
        comp='p'
elif randno==3:
        comp='s'

you=input("Your turn : Rock(r) Paper(p) or Scissior(s) ? ")
a=gamewin(comp,you)

print(f"Computer choose {comp}")
print(f"Your turn {you}")

if a==None:
        print("The game is tie...")
elif a:
        print("Congratulation You win...")
else :
        print("Sorry you loose...")