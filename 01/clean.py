dial = 50
count1 = count2 = 0

for line in open(0).read().split():
  turn = dial + (1 if line[0] == 'R' else -1) * int(line[1:])
  count2 += abs(turn) // 100 + (dial > 0 and turn <= 0)
  dial = turn % 100
  count1 += (dial == 0)

print(count1, count2)
