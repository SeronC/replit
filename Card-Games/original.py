import os  #OS for Python operating platform
import sys  #SYS for system internals and clean exit sequence
import time  #time for sleep and display time
from random import shuffle
import random  #random for card selection

if os.name == "nt":  #ANSI for Windows Terminal/Console
  os.system("")

pyv = sys.version  #Determining Python version for compatibility
pyversion = pyv[1]


def legacy_homescreen():  #Python v!=3
  print("""\033[1;30;41m    Card Game    \033[0;40m
Game by GHS Year 13 Students.""")  #\033[0;0m Default
  print("\033[0;36;40m Currently using", os.name.upper(),
        "for Python \033[0;40m")


def homescreen():  #Python v=3
  print("""\x1b[1;30;41m    Card Game    \x1b[3;30;0m
Game by GHS Year 13 Students.""")
  print("\x1b[0;36;40mCurrently using", os.name.upper(),
        "for Python\x1b[3;30;0m")


#Start screen
def loadin():
  print("Loading Game.")
  time.sleep(0.15)
  os.system('cls' if os.name == 'nt' else 'clear')

  print("Loading Game..")
  time.sleep(0.5)
  os.system('cls' if os.name == 'nt' else 'clear')

  print("Loading Game..")
  time.sleep(0.15)
  os.system('cls' if os.name == 'nt' else 'clear')


loadin()

if "3" in pyversion:
  homescreen()
else:
  legacy_homescreen()


def Leave_Game():  #Exit sequence
  print("Exiting Game...")
  time.sleep(0.6)
  sys.exit("""Thank you for hitting PLAY!
Check out the creator: replit.com/@Seronchanderabo
""")


#Play or Exit
gameLoop = True
Exiter = True
while gameLoop:
  while Exiter:
    pl = str(input("Play or Exit? P/E: "))
    pl = pl.lower()

    #Play
    if pl == "p":
      print("Loading Gamemode...")
      time.sleep(0.4)
      Exiter = False
      gameLoop = False
      os.system('cls' if os.name == 'nt' else 'clear')

    #Exit
    elif pl == "e":
      Leave_Game()

    #False input (!= P or E)
    else:
      print("Enter 'P' key for 'play' or 'E' key for 'exit'.")
      pass

#Gamemode 1 War Cards


#cards (basic deck)
class Card:
  suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

  values = [
    None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen",
    "King", "Ace"
  ]

  #Card format
  def __init__(self, v, s):
    #suit + value are ints
    self.value = v
    self.suit = s

  #Suitable Options
  def __lt__(self, c2):
    if self.value < c2.value:
      return True
    if self.value == c2.value:
      if self.suit < c2.suit:
        return True
      else:
        return False
    return False

  #Duplicate check
  def __gt__(self, c2):
    if self.value > c2.value:
      return True
    if self.value == c2.value:
      if self.suit > c2.suit:
        return True
      else:
        return False
    return False

  #Card Labelling
  def __repr__(self):
    v = self.values[self.value] +\
        " of " + \
        self.suits[self.suit]
    return v


#Gives players cards
class Deck:
  #Shuffle Deck
  def __init__(self):
    self.cards = []
    for i in range(2, 15):
      for j in range(4):
        self.cards\
            .append(Card(i,
                         j))
    shuffle(self.cards)

  #Clear Deck
  def rm_card(self):
    if len(self.cards) == 0:
      return
    return self.cards.pop()


#Player Information
class Player:

  def __init__(self, name):
    self.wins = 0
    self.card = None
    self.name = name


#Game instructions
class Game:

  #Player Names
  def __init__(self):
    name1 = input("Player 1 Name? ")
    name2 = input("Player 2 Name? ")
    self.deck = Deck()
    self.p1 = Player(name1)
    self.p2 = Player(name2)

  #Declare Winner
  def wins(self, winner):
    w = "{} wins this round."
    w = w.format(winner)
    print(w)

  #Declare Draw
  def draw(self, p1n, p1c, p2n, p2c):
    d = "{} drew {} {} drew {}"
    d = d.format(p1n, p1c, p2n, p2c)
    print(d)

  #Start Gamemode
  def play_game(self):
    cards = self.deck.cards
    print("Beginning Game..")
    #Quit
    while len(cards) >= 2:
      m = "Type 'Q' to quit. Any key to play: "
      response = input(m)

      if response == "Q" or "q":
        break

      p1c = self.deck.rm_card()
      p2c = self.deck.rm_card()

      p1n = self.p1.name
      p2n = self.p2.name

      self.draw(p1n, p1c, p2n, p2c)

      if p1c > p2c:
        self.p1.wins += 1
        self.wins(self.p1.name)

      else:
        self.p2.wins += 1
        self.wins(self.p2.name)
    #Winner Declare
    win = self.winner(self.p1, self.p2)
    print("Game Over! {} wins".format(win))

  #Decides who wins
  def winner(self, p1, p2):
    if p1.wins > p2.wins:
      return p1.name

    if p1.wins < p2.wins:
      return p2.name

    return "Tie! Both players win this round."


#Gamemode 2 Snap
class snap():
  global suits
  suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
  global number
  number = [
    "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen",
    "King"
  ]

  def playername():
    p1 = str(input("Enter name for player 1: "))
    global player1
    player1 = [p1]
    p2 = str(input("Enter name for player 2: "))
    global player2
    player2 = [p2]

    #print(player1, player2)

  def give1():
    player1.append(random.choice(suits))
    player1.append(random.choice(number))
    print(player1[0], "now has a", player1[2], "of", player1[1])

  def give2():
    player2.append(random.choice(suits))
    player2.append(random.choice(number))
    print(player2[0], "now has a", player2[2], "of", player2[1])

  def compare_card():
    if player1[2] not in number:
      print("An error has occured. (snap-compare_card-player1_not_in_num)")
    elif player2[2] not in number:
      print("An error has occured. (snap-compare_card-player2_not_in_num)")
    else:
      player1val = number.index(player1[2])
      #print(number.index(player1[2]))
      player2val = number.index(player2[2])
      #print(number.index(player2[2]))
      if player1val > player2val:
        print(player1[0], "wins!")
      elif player1val < player2val:
        print(player1[0], "wins!")
      elif player1val == player2val:
        print("Tie! nobody wins!")
      else:
        print("An error has occured. (snap-compare_card-else)")


#Gamemode selection
Gamemode_1 = "War Cards"
Gamemode_2 = "Snap!"


def play_gamemode():
  while True:
    while True:
      gm = str(
        input(f"{Gamemode_1}(1), {Gamemode_2}(2) or Exit Program? 1/2/E: "))

      #Game mode 1
      if gm == "1":
        print("Loading", Gamemode_1)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
          Gamemode_1, """is still under development.
If you encounter any issues, reload the page and try other gamemodes
or try again later."
        """)

        game = Game()
        game.play_game()

        break

      #Game mode 2
      elif gm == "2":
        print("Loading", Gamemode_2)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Gamemode_2, "is still under development.")
        print(
          "If you encounter any issues, reload the page and try other gamemodes."
        )

        snap.playername()
        snap.give1()
        snap.give2()
        snap.compare_card()

        break

      elif gm.lower() == "e":
        Leave_Game()

      else:
        print("Enter either '1' or '2'")
        continue


#Play Again
while True:
  play_gamemode()
  again = input("Play again? Y/N: ")
  if again.lower() == "y":
    play_gamemode()
    continue
  elif again.lower() == "n":
    Leave_Game()
    break
  else:
    print("Enter either Y or N")
    pass
