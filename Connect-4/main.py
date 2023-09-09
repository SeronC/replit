import os

print("""Welcome to:

  C《》N N £ C T  4

by Seron
[replit.com/@seronchanderabo]

-Game inspiration by Hasbro's Connect Four""")
start = input("  --Press ENTER to Start-- \n")

os.system('cls' if os.name == 'nt' else 'clear')

board = [["0"] * 7] * 6

for i in range(len(board)):
    print(board[i])
