# 이것이 취업을 위한 코딩테스트다 part03 '33. 퇴사'와 동일

n=int(input())

d=[0]*(n+1)

array=[]
for i in range(1,n+1):
  take,cost=map(int,input().split())
  array.append((i,i+take-1,cost))

for i in range(1,n+1):
  for start,end,cost in array:
    if end==i:
      d[i]=max(d[i],d[start-1]+cost)
  d[i]=max(d[i],d[i-1])

print(d[n])