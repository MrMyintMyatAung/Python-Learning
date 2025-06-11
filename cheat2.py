import os

# Dump memory
os.system("del mine.dmp")
os.system("procdump -ma minesam.exe mine")

# Find gameboard
mark = b'\x00\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x0F'  # Bytes object

line_length = 32
board_size = 500  # characters in whole board

with open("mine.dmp", "rb") as f:
    data = f.read()

start = data.find(mark)
if start < 0:
    print("Gameboard not found")
    exit()

# Print gameboard
for i in range(0, board_size, line_length):
    line = ''
    for j in range(line_length):
        g = data[start + i + j]

        if g == 0x10:
            c = "-"
        elif g == 0x0F:
            c = " "
        elif g == 0x8F:
            c = "*"
        elif g == 0x00:
            c = " "
        else:
            adjusted = g - 16
            c = chr(adjusted) if 0 <= adjusted < 256 else "?"  # Prevent chr() error
        
        line += c
    print(line)
