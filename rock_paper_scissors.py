import random

def gameWin(comp,you):
    if comp == you:
         return None
    elif comp == 'r':
        if you == 'p':
             return True
        elif you =='s':
             return False
    elif comp == 'p':
        if you == 'r':
             return False
        elif you =='s':
             return True
    elif comp == 's':
        if you == 'p':
             return False
        elif you =='r':
             return True
         
 
while True:
     randNo = random.randint(1,3)
     if randNo == 1:
         comp = 'r'
     if randNo == 2:
         comp = 'p'
     if randNo == 3:
         comp = 's'
     you = input("Your turn : Rock(r) Paper(p) or Scissors(s)?")


     a = gameWin(comp,you)

     print(f"Comp chose {comp}")
     print(f"You chose {you}")
     if a == None:
          print("The game is a tie.")
     elif a:
          print("You Win!")
     else:
          print("You Lose!")

     play_again = input("Do you want to play again? (Y/N): ")
     if  play_again != 'Y' and play_again != 'y':
          break




     