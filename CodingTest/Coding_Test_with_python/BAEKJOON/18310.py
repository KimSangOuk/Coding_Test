# 이것이 취업을 위한 코딩테스트다 part03 '24. 안테나'와 동일

n=int(input())
array=list(map(int,input().split()))

array.sort()
if n%2==0:
  print(array[n//2-1])
else:
  print(array[n//2])