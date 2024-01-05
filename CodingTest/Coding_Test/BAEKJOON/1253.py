# 풀이시간 40분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 하나의 수를 지정해서 목표로 두고 그 목표를 나머지 수들로 찾을 수 있는지를 구하는 문제이다. 이 때, 첫번째 수는 반복문을 통해 N회로 찾을 수 있지만 똑같이 N^2로 찾을 시 시간 초과에 걸리기 때문에 이진탐색으로 찾아주는 것이 적절하다. 이때, 중복으로 목표점, 첫번째 수, 두 번째 수가 들어가지 않도록 하는 것이 중요하다.

n=int(input())

array=list(map(int,input().split()))

def binary_search(array,target,first,start,end):
  while start<=end:
    mid=(start+end)//2
    if mid==first:
      mid+=1
      if mid>end:
        break
    if array[mid]+array[first]==target:
      return True
    elif array[mid]+array[first]<target:
      start=mid+1
    else:
      end=mid-1
  return False
array.sort()
count=0
for i in range(n):
  target=i
  delete=array.pop(i)
  for j in range(n-1):
    first=j
    if binary_search(array,delete,first,0,len(array)-2):
      count+=1
      break
  array.insert(i,delete)

print(count)