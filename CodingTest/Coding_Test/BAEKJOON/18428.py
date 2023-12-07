# 이것이 취업을 위한 코딩테스트다 part03 '20. 감시 피하기'와 동일

from itertools import combinations

n=int(input())

graph=[]
for _ in range(n):
  graph.append(list(map(str,input().split())))

temp=[['']*n for _ in range(n)]

empty_space=[]

for i in range(n):
  for j in range(n):
    if graph[i][j]=='X':
      empty_space.append((i,j))

case_list=list(combinations(empty_space,3))

answer='Yes'

def watch(y,x,d):
  global answer
  if y<0 or y>=n or x<0 or x>=n or temp[y][x]=='O':
    return
  if temp[y][x]=='S':
    answer='No'
  else:
    if d==0:
      watch(y,x+1,0)
    if d==1:
      watch(y,x-1,1)
    if d==2:
      watch(y+1,x,2)
    if d==3:
      watch(y-1,x,3)

def main():
  global answer
  for case in case_list:
    for i in range(n):
      for j in range(n):
        if (i,j) in case: 
          temp[i][j]='O'
        else:
          temp[i][j]=graph[i][j]
    answer='Yes'
    for i in range(n):
      for j in range(n):
        if temp[i][j]=='T':
          for d in range(4):
            watch(i,j,d)

    if answer!='No':
      return 'Yes'

answer=main()
if answer=='Yes':
  print("YES")
else:
  print("NO")