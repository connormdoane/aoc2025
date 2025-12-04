with open(0) as f:
  lines = [list(line.rstrip()) for line in f]
  
def count_surrounding(x,y):
  count = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if x+i >= len(lines) or x+i < 0 or y+j >= len(lines[0]) or y+j < 0:
        continue
      count += 1 if lines[x+i][y+j] == '@' else 0
  return count-1<4
  
def part1():
  count = 0
  for x in range(len(lines)):
    for y in range(len(lines[0])):
      if lines[x][y] == '@' and count_surrounding(x,y):
        count += 1
  print(count)

def part2():
  count = 0
  removable = set()
  removed = True
  while removed:
    removable = set()
    removed = False
    for x in range(len(lines)):
      for y in range(len(lines[0])):
        if lines[x][y] == '@' and count_surrounding(x,y):
          count += 1
          removable.add((x,y))
          removed = True
    for x,y in removable:
      lines[x][y] = '.'
  print(count)

if __name__ == "__main__":
  part1()
  part2()
