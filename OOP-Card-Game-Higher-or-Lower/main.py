import random

valid_entries = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
rnum = random.randint(1, 13)

print(rnum) #Optional code for debugging
result = 0 #NameError exception handling

while result != rnum:
  user = input("Enter a Card Value: \nAce(1), 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack(11), Queen(12), King(13): " + "\nEntry: ")
    
  if user not in valid_entries:
    print("Invalid entry: Input not in array.")
        
  if user in valid_entries:
    result = valid_entries.index(user) + 1
    print(f"System entry = {result}") #Optional code for debugging
        
    if rnum > result:
      print ("Enter a higher number")
    elif rnum < result:
      print("Enter a lower number")
    elif rnum == result:
      print("Correct number!")
    else:
      print("Error - check validation loop") #Optional code for debugging
            
print("Thanks for playing!") #Optional code for end sequence