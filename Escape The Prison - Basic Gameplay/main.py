import random

print("""___________________________
| Welcome to: |  |  |  |  |
|  |  [[[[[   |  |  |  |  |
|  |  |O O|  Escape |  |  | 
|  |  [ - ]  the prison|  |
|  | __| |__  |  |  |  |  | 
|  |//|   |\\\\ by Seron |  |
```````````````````````````
Check out other projects here:
replit.com/@Seronchanderabo

-Basic Gameplay:
. Home-screen
. PIN entry
. Restart Sequence

How to play:
-You are a prisoner
-You need to enter the PIN to escape
-If your answer is correct, you win!
""")
while True:
    pin = random.randint(1, 100)
    print(pin)
    while True:
        answer = input("Enter PIN: ")
        answer = int(answer)
        if answer == pin:
            print("Well done, you have escaped!")
            break
        elif answer > pin:
            print("Too high.")
        elif answer < pin:
            print("Too low.")
    restart = input("Would you like to play again? (Y/N): ")
    restart = restart.lower()
    if restart == "y":
        continue
    elif restart == "n":
        break
    else:
      print("Enter 'Y' or 'N'.")
      break
exit("Exiting...")
