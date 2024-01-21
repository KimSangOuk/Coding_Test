# 풀이시간 45분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 배열이 정렬되어 있지 않은 상태에서 연속하는 부분을 나누어 그 안에서의 점수를 구해야하는 문제이다. 이 때 점수가 최소가 되게 해야한다. 일단 배열을 모든 방법으로 끊는 방법이 있는데 가짓수가 너무 많아서 불가능하다. 그렇다면 특정 규칙에 따라 끊어야하면서 전체 부분 수열의 갯수를 조절하고 그 갯수와 주어진 구간의 갯수를 맞춰가야한다. 구간을 나누는 방법 중에는 최대 점수를 기준으로 역으로 구간을 끊어 갯수를 맞춰가는 방법이 있는데 이 때, 한번만 배열을 순회하므로 시간복잡도 상으로 가능하다. 그렇기에 구간을 정해진 최대 구간의 갯수와 비교하면서 진행하면 된다. 이때 구해진 구간의 갯수가 목표 갯수보다 크다면 구간의 갯수를 줄여야 하므로 최대 점수를 늘려야한다. 그리고 같거나 작다면 정답이 될 수 있고 또한 같더라도 점수의 최소를 구해야 하므로 낮춰가며 구할 수 있다.

n,m=map(int,input().split())

array=list(map(int,input().split()))

def binary_search(array,target,start,end):
  result=0
  while start<=end:
    mid=(start+end)//2
    min_value=int(1e9)
    max_value=0
    count=1
    for i in range(len(array)):
      min_value=min(min_value,array[i])
      max_value=max(max_value,array[i])
      if max_value-min_value>mid:
        count+=1
        max_value=array[i]
        min_value=array[i]
    if count>target:
      start=mid+1
    else:
      result=mid
      end=mid-1
  return result

result=binary_search(array,m,0,max(array)-min(array))
print(result)