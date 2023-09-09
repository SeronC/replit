player_one = "1"
player_two = "2"

board = ""

# CUSTOM GRID SIZE (4-9)
"""
while True:
  rows = int(input("How many rows? "))
  if rows > 4 and rows < 10:
    break
  else:
    print("Number of rows must be larger than 3 and less than 10. \n")

while True:
  columns = int(input("How many columns? "))
  if columns > 4 and columns < 10:
    break
  else:
    print("Number of columns must be larger than 3 and less than 10. \n")
"""
#CREATING THE GRID
columns, rows = 6, 6
grid_box = "|_"

grid_columns = columns * (grid_box)
grid_num_start = "   "
grid_num_spacing = (len(grid_box) - 1) * (" ")

for i in range(columns):
  i = i + 1
  grid_num_start = grid_num_start + str(i) + grid_num_spacing

#print(grid_num_start)
board = board + grid_num_start

for j in range(rows):
  j = j + 1
  #print(j, grid_columns + "|")
  board = board + "\n" + str(j) + " " + grid_columns + "|"
#BOARD LAYOUT
print(board)

print("Board Length:", len(board))

#ROW SEPERATION
row1 = board[18:31]
row2 = board[34:47]
row3 = board[50:63]
row4 = board[66:79]
row5 = board[82:95]
row6 = board[98:111]

grid = f"""{row1}
{row2}
{row3}
{row4}
{row5}
{row6}"""
print(grid)
