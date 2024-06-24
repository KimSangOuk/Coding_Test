n=int(input())
array=[]
for i in range(n):
  name,score=map(str,input().split())
  array.append([name,int(score)])

array.sort(key=lambda x:x[1])
for i in range(len(array)):
  print(array[i][0],end=' ')