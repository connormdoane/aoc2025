def count_surrounding(x,y):
  if lines[x][y] != '@':
    return False
  count = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if x+i >= len(lines) or x+i < 0 or y+j >= len(lines[0]) or y+j < 0:
        continue
      count += 1 if lines[x+i][y+j] == '@' else 0
  return count-1<4

with open(0) as f:
  lines = [list(line.rstrip()) for line in f]
  count = 0
  removed = True
  first_pass = True
  while removed:
    removable = set()
    removed = False
    for x in range(len(lines)):
      for y in range(len(lines[0])):
        if count_surrounding(x,y):
          count += 1
          removable.add((x,y))
          removed = True
    for x,y in removable:
      lines[x][y] = '.'
    if first_pass:
      print(count)
      first_pass = False
  print(count)
