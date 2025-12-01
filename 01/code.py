import sys

with sys.stdin as f:
  lines = [line.rstrip() for line in f]

def part1():
  dial = 50
  count = 0
  for line in lines:
    sign = 1 if line[0] == 'R' else -1
    dial += sign * int(line[1:])
    dial %= 100
    count += (dial == 0)
  print(count)
  
def part2():
  dial = 50
  count = 0
  for line in lines:
    sign = 1 if line[0] == 'R' else -1
    turn = dial + sign * int(line[1:])
    count += abs(turn) // 100 + (dial > 0 and turn <= 0)
    dial = turn % 100
  print(count)

def both():
  dial = 50
  count1 = count2 = 0
  for line in lines:
    sign = 1 if line[0] == 'R' else -1
    turn = dial + sign * int(line[1:])
    count2 += abs(turn) // 100 + (dial > 0 and turn <= 0)
    dial = turn % 100
    count1 += (dial == 0)
  print(count1)
  print(count2)
    

if __name__ == "__main__":
  # part1()
  # part2()
  both()
