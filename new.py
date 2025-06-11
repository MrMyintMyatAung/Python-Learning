import os

# Dump memory

cmd = "del mine.dmp"
os.system(cmd)
cmd = "procdump -ma minesam.exe mine"
os.system(cmd)

# Find gameboard

mark ='\x00\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x0F'

line_length = 32
board_size = 600 # characters in whole board

with open("mine.dmp", "rb") as f:
  data= f.read()

start = data.find(mark)
if start <0:
  print "Gameboard not found"

# Print gameboard

for i in range(0, board_size, line_length):
  line = ''
  for j in range(line_length):
    g = data[start+i+j]
    if g == '\x10':
      c = "-"
    elif g == '\x0f':
      c = " "
    elif g == '\x8f':
      c = "*"
    elif g == '\x00':
      c = " "
    else:
      c = chr( ord(g) - 16 )
    line += c
  print line