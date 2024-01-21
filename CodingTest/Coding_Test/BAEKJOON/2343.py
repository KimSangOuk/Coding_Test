# 풀이시간 30분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 그룹의 수를 목표로 삼고 결과 값은 우리가 원하는 블루레이의 길이로 한다면 우리는 이진탐색을 통해 이 길이를 탐색해 나갈 수 있는데, 이 때, 현재의 값으로 만든 그룹의 수가 목표 그룹의 수보다 작거나 같으면 일단 가능하기 때문에 답으로 저장해두고 더 늘릴 수 있기 때문에 그룹의 크기를 줄이면 된다. 

n,m=map(int,input().split())
array=list(map(int,input().split()))

def binary_search(array,target,start,end):
  global result
  while start<=end:
    mid=(start+end)//2
    sum_value=0
    max_value=0
    count=0
    for i in range(0,len(array)):
      sum_value+=array[i]
      if sum_value>mid:
        max_value=max(sum_value-array[i],max_value)
        sum_value=array[i]
        count+=1
      elif sum_value==mid:
        max_value=max(sum_value,max_value)
        sum_value=0
        count+=1
    if sum_value>0:
      max_value=max(sum_value,max_value)
      count+=1
    if count<=target:
      result=mid
      end=mid-1
    else:
      start=mid+1

result=0
binary_search(array,m,max(array),sum(array))
print(result)
      
        
        