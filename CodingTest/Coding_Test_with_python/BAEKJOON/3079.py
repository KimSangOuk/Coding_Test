# 풀이시간 30분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 우리가 구하고자 하는 것은 시간이기 때문에 특정 시간 t가 몇명을 받아들일 수 있는지 보면 된다. 배열을 정렬했을 때, 각 심사대로 전체 시간을 나눈 값의 합이 인원의 수용량이므로 그 수용량이 우리가 세우고자 하는 목표인원 보다 크다면 답으로 가능은 하나 시간을 더 줄여볼 수 있기 때문에 작은 부분을 탐색하고 반대일 경우에는 큰 부분을 탐색하면 된다. 아무리 시간이 적게 들어도 한명일 경우, 가장 작은 수보다는 크고, 아무리 시간이 많이 걸려도 제일 오래 걸리는 탐색대에 목표 인원을 전부 세우는 수보다는 작기 때문에 start,end를 다음과 같이 지정했다.

n,m=map(int,input().split())
array=[]
for i in range(n):
  array.append(int(input()))

array.sort()
result=0

def binary_search(array,target,start,end):
  global result
  while start<=end:
    mid=(start+end)//2
    count=0
    for i in range(0,len(array)):
      count+=mid//array[i]

    # print(mid,count)
    if count>=target:
      result=mid
      end=mid-1
    else:
      start=mid+1
  return result

binary_search(array,m,array[0],m*array[-1])
print(result)