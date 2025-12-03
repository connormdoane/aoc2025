count1 = count2 = 0

for i in open(0).read().rstrip().split(','):
  i1, i2 = i.split('-')
  for j in range(int(i1), int(i2)+1):
    s = str(j)
    if s[:len(s)//2] == s[len(s)//2:]:
      count1 += j
    for k in range(1, len(s)//2+1):
      if s.replace(s[:k], '') == '':
        count2 += j
        break

print(count1, count2)
