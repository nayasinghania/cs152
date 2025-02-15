# Question 2 - Extended Tail Clone
# Usage: Usage: python3 q2.py <filename> <n>
# <filename> is the name of the file to read
# <n> is the number of lines to print from the beginning, middle, and end of the file

import sys

def tail(filename, n):
  lines = []
  try:
    with open(filename, 'r') as f:
      for line in f:
        lines.append(line.rstrip("\n"))
    if n > len(lines):
      print( "n is longer than the amount of lines in the file")
    else:
      print("FIRST {} LINE(S)".format(n))
      for i in range(n):
        print(lines[i])
      print("\nMIDDLE {} LINE(S)".format(n))
      center = len(lines) // 2
      half = n // 2
      for i in range(center - half, center + half + 1):
        print(lines[i])
      print("\nLAST {} LINE(S)".format(n))
      for i in range(len(lines) - n, len(lines)):
        print(lines[i])
  except:
    print( "Error reading file")

def main():
  if len(sys.argv) != 3:
    print("Usage: python3 q2.py <filename> <n>")
  else:
    tail(sys.argv[1], int(sys.argv[2]))

if __name__ == "__main__":
  main();
