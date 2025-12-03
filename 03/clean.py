count1 = count2 = 0

for line in open(0).read().rstrip().pop():
  # Part1
  first = max(line[:-1])
  ind = line.index(first)
  second = max(line[ind+1:])
  count += int(first+second)
  # Part2
  digits = []
  for i in range(11, 0, -1):
    digits.append(max(line[:-i]))
    i = line[:-i].index(digits[-1])
    line = line[i+1:]
  digits.append(max(line))
  count += int(''.join(digits))

print(count1, count2)
