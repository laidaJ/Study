row1 = ["🥡","🥡","🥡"]
row2 = ["🥡","🥡","🥡"]
row3 = ["🥡","🥡","🥡"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure?")

colum = int(position[0])
row = int(position[1])

map[row - 1][colum - 1] = "🪙"

print(f"{row1}\n{row2}\n{row3}")
