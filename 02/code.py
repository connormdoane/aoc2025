with open("input.txt", 'r') as f:
  lines = [line.rstrip().split(',') for line in f][0]
  lines = [line.split('-') for line in lines]

def is_invalid(i):
  return i[:len(i)//2] == i[len(i)//2:]
  
def part1():
  res = 0
  for line in lines:
    for i in range(int(line[0]), int(line[1])+1):
      if is_invalid(str(i)):
        res += i
  print(res)

def is_invalid_2(i):
  for k in range(1,len(i)):
    flag = True
    for j in range(0, len(i)-k, k):
      if i[j:j+k] != i[j+k:j+k+k]:
        flag = False
    if flag:
      return True
  return False
    
def part2():
  res = 0
  for line in lines:
    for i in range(int(line[0]), int(line[1])+1):
      if is_invalid_2(str(i)):
        res += i
  print(res)

if __name__ == "__main__":
  part1()
  part2()
