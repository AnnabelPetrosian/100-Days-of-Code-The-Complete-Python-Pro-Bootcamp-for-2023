# Treasure Map
# 🚨 Don't change the code below 👇
line1 = ["⬜️","⬜️","⬜️"]
line2 = ["⬜️","⬜️","⬜️"]
line3 = ["⬜️","⬜️","⬜️"]
map = [line1, line2, line3]
#print(f"{row1}\n{row2}\n{row3}")
print("Hiding your treasure! X marks the spot. ")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"


#horizontal = int(position[0])
#vertical = int(position[1])
#map[vertical - 1][horizontal - 1] = "X"


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")