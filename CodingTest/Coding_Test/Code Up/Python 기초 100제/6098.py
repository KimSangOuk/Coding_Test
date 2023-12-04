box=[]
for _ in range(10):
  box.append(list(map(int,input().split())))

a_x,a_y=1,1
box[a_y][a_x]=9
while True:
  if box[a_y][a_x+1]==2:
    box[a_y][a_x+1]=9
    a_x+=1
    break
  elif box[a_y][a_x+1]==1:
    if box[a_y+1][a_x]==2:
      box[a_y+1][a_x]=9
      a_y+=1
      break
    elif box[a_y+1][a_x]==1:
      break
    else:
      box[a_y+1][a_x]=9
      a_y+=1
  else:
    box[a_y][a_x+1]=9
    a_x+=1

for y in range(10):
  for x in range(10):
    print(box[y][x],end=' ')
  print('\n')
    