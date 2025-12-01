with open("input.txt", 'r') as f:
  lines = [line.rstrip() for line in f]

def part1():
  dial = 50
  count = 0
  for line in lines:
    if line[0] == 'L':
      dial -= int(line[1:])
      while dial < 0:
        dial += 100
    elif line[0] == 'R':
      dial += int(line[1:])
      while dial > 99:
        dial %= 100
    if dial == 0:
      count += 1
  print(count)

def move_dial(direction, count, dial, start_count):
  dial_res = dial
  res = start_count
  if direction == 'L':
    for i in range(count):
      dial_res -= 1
      if dial_res == 0:
        res += 1
      if dial_res == -1:
        dial_res = 99
  if direction == 'R':
    for i in range(count):
      dial_res += 1
      if dial_res == 100:
        dial_res = 0
      if dial_res == 0:
        res += 1
  return dial_res, res
  
def part2():
  dial = 50
  count = 0
  for line in lines:
    dial, count = move_dial(line[0], int(line[1:]), dial, count)
  print(count)

if __name__ == "__main__":
  part1()
  part2()
