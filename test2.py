r,c = map(int, input().split())
sy,sx = map(int, input().split())
gy,gx = map(int, input().split())
c = [list(input()) for _ in range(r)]

c[sy-1][sx-1] = 0
queue = [(sy-1, sx-1)]
count = 0

while True:
  queue_next = []
  count += 1
  for y,x in queue:
    for i,j in ((0,1),(1,0),(0,-1),(-1,0)):
      if c[y + i][x + j] == '.':
        c[y + i][x + j] = count
        queue_next.append((y+i, x+j))
  queue = queue_next
  if (gy - 1, gx - 1) in queue_next:
    break
print(count)
