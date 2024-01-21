# 풀이시간 10분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 횟수를 목표로 삼고 각 범위에 따라 count를 세어가는 이진 탐색문제이다.

n,m=map(int,input().split())

array=[]
for i in range(n):
  array.append(int(input()))
  
def binary_search(array,target,start,end):
  global result
  while start<=end:
    mid=(start+end)//2
    count=0
    sum_value=0
    for i in range(0,len(array)):
      sum_value+=array[i]
      if sum_value>mid:
        count+=1
        sum_value=array[i]
      elif sum_value==mid:
        count+=1
        sum_value=0
    if sum_value>0:
      count+=1
    if count<=target:
      result=mid
      end=mid-1
    else:
      start=mid+1
      
result=0
binary_search(array,m,max(array),sum(array))
print(result)