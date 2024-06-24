# 이것이 취업을 위한 코딩테스트다 part03 '23. 국영수'와 동일

n=int(input())
arr=[]
for _ in range(n):
  a=list(input().split())
  arr.append((a[0],int(a[1]),int(a[2]),int(a[3])))

arr.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in range(n):
  print(arr[i][0],)