print("\033[1;34;40m D A S T A N \033[0m")

board = [
  [['  '], ['  '], ['k1'], ['  '], ['  '], ['  ']],
  [['  '], ['!!'], ['!!'], ['!!'], ['!!'], ['  ']],
  [['  '], ['  '], ['  '], ['  '], ['  '], ['  ']],
  [['  '], ['  '], ['  '], ['  '], ['  '], ['  ']],
  [['  '], ['""'], ['""'], ['""'], ['""'], ['  ']],
  [['  '], ['  '], ['  '], ['k2'], ['  '], ['  ']],
]


def show_board():
  for i in range(6):
    print(board[i])


player1 = str(input("\033[1;34;44m Enter player one name:\033[0m "))
player2 = str(input("\033[1;34;44m Enter player two name:\033[0m "))

currentplayer = [1, 2]
players = (player1, currentplayer[0]), (player2, currentplayer[1])


def gameplay():
  print("Stage 1")
  print("Stage 2")
  print("Stage 3")
  
  show_board()


GameOver = False
while GameOver == False:
  for i in range(len(currentplayer)):
    print(f"Player {players[i][1]}'s ({players[i][0]}) turn:")

    print("Gameplay")
    gameplay()

  GameOver = True
