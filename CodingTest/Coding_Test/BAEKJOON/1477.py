# 풀이시간 45분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 각 새로운 휴게소를 세울 수 있는 공간은 휴게소들 사이와 시작점과 끝점으로부터 처음과 끝 휴게소 사이 이기 때문에 휴게소들 입력을 받아 정렬을 시키고 앞과 뒤에 좌표를 처음과 끝을 달아준다. 각 휴게소를 설치하기 위해서는 특정 위치마다 설치되게 해야되는데 이 때 최대 값이기 때문에 시작점을 각 휴게소로 했을 때 오른쪽으로 설치하면서 갯수를 거리가 달라질 때마다 갯수를 구할 수 있다. 이진탐색으로 범위를 조절하며 특정 거리일 때의 총 갯수를 설치해야 하는 휴게소의 갯수와 비교하면서 진행하면 된다.

n,m,l=map(int,input().split())

array=list(map(int,input().split()))
array.sort()
array=[0]+array+[l]

end=0
for i in range(len(array)-1):
  end=max(array[i+1]-array[i],end)

def binary_search(array,target,start,end):
  result=0
  while start<=end:
    mid=(start+end)//2
    count=0
    for i in range(len(array)-1):
      value=array[i+1]-array[i]
      if value%mid==0:
        count+=value//mid-1
      else:
        count+=value//mid
    if count>target:   
      start=mid+1
    elif count<=target:
      result=mid
      end=mid-1
  return result

result=binary_search(array,m,1,end)
print(result)