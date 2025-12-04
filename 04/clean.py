import subprocess

make_video = [
  'ffmpeg',
  '-framerate',
  '10',
  '-i',
  'frames/frame%d.ppm',
  '-vf',
  'scale=640:640:flags=neighbor',
  'output.mp4'
]

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

def render_frame(frame_count, removable):
  with open("frames/frame"+str(frame_count)+".ppm", 'w') as frame:
    frame.write('P3\n')
    frame.write(str(len(lines[0])) + ' ' + str(len(lines)) + '\n')
    frame.write('255\n')
    for x in range(len(lines)):
      for y in range(len(lines[0])):
        if (x,y) in removable:
          frame.write('255 ')
          frame.write('0 ')
          frame.write('0 ')
        elif lines[x][y] == '@':
          frame.write('255 ')
          frame.write('255 ')
          frame.write('255 ')
        else:
          frame.write('0 ')
          frame.write('0 ')
          frame.write('0 ')
      frame.write('\n')

with open(0) as f:
  subprocess.run(['rm', 'output.mp4'], check=True)
  lines = [list(line.rstrip()) for line in f]
  count = 0
  removed = True
  frame_count = 0
  while removed:
    removable = set()
    removed = False
    for x in range(len(lines)):
      for y in range(len(lines[0])):
        if count_surrounding(x,y):
          count += 1
          removable.add((x,y))
          removed = True
    render_frame(frame_count, removable)
    for x,y in removable:
      lines[x][y] = '.'
    if not frame_count:
      print(count)
    frame_count += 1
  subprocess.run(make_video, check=True)
  print(count)
