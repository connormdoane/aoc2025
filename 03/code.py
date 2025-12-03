with open("input.txt", 'r') as f:
  lines = [line.rstrip() for line in f]
  lines.pop()

def part1():
  count = 0
  for line in lines:
    first = max(line[:-1])
    ind = line.index(first)
    second = max(line[ind+1:])
    count += int(first+second)
  print(count)

def part2():
  count = 0
  for line in lines:
    digits = []
    for i in range(11, 0, -1):
      digits.append(max(line[:-i]))
      i = line[:-i].index(digits[-1])
      line = line[i+1:]
    digits.append(max(line))
    count += int(''.join(digits))
  print(count)

if __name__ == "__main__":
  part1()
  part2()
