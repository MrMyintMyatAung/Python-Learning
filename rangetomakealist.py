

squares = [value**2 for value in range(1, 11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here is the first three players in My Team:")

for player in players[:3]:
    print(player.title())