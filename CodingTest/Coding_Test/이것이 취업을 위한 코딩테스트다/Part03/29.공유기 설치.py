# 풀이시간 60분/50분 시간제한 2초 메모리제한 128MB
# 1회차 정답 - 풀이시간 초과 및 더 표현의 단순화 가능
# 찾아야 되는 범위가 벌써 10억이다 보니 이진탐색을 사용해야된다는 것을 알 수 있다. 여기서 메모리도 충분하지 않으니 말이다. 가능한 최대를 구하는 문제이니 Parametic Search 알고리즘 이기도 한다는 것은 금방 알 수 있었다.
# 하지만 여기서 고민이 많이 되었던 부분은 어떻게 공유기를 설치하느냐의 문제였고 그 중 시작지점을 별도로 구한다면 데이터의 수가 200,000 이기 때문에 이중 포문이 되어 불가능하다는 점이었다. 그렇기에 단순 반복문으로 최대한 풀어내었다.
# 누적 거리를 표현하는 방법의 차이로 식이 길어졌지만 중간에 빼는 식을 기록하는 식으로 풀어도 되는 문제였다. 단지 시간이 오래걸렸다. 그리고 따로 중간 저장 좌표를 두지 않으면서 식이 길어졌다는 점이다.
# 우리의 목표는 더 빠른 시간안에 더 간결안에 푸는 것이기 때문에 연습겸 한번 더 풀어보기로 하였다.

# 2회차 풀이





# 1회차 풀이 정답
import sys

n,c=map(int,input().split())
arr=[]
for _ in range(n):
  arr.append(int(sys.stdin.readline()))

arr.sort()

start=1
end=arr[-1]-arr[0]
answer=0
while start<=end:
  mid=(start+end)//2
  #print("mid",mid)
  # 갯수를 구해
  value=1
  s=0
  # 단순히 시간이 급해서 빠르게 푸느라 생각을 한번 더 안하긴 하였으나 중간 저장 좌표를 둔다면 누적량을 따로 표현안해서 더 간결해 질 수 있었다.
  for i in range(len(arr)-1):
    if arr[i+1]-arr[i]>=mid:
  #    print(arr[i],arr[i+1])
      value+=1
      s=0
    else:
      s+=arr[i+1]-arr[i]
  #    print("s 누적량",s)
      if s>=mid:
        s=0
        value+=1
  # print("value",value)
  
  # 구한 갯수가 너무 많거나 같아
  if value>=c:
    answer=mid
    start=mid+1
  else:
    end=mid-1

print(answer)

# 답안 예시
# 나머지 부분은 같기 때문에 중간에 공유기를 설치하는 식만 적어놓겠다.
value=array[0]
count=1
# 현재의 mid값을 이용해 공유기를 설치
for i in range(1,n):
  if array[i]>=value+mid:
    value=array[i]
    count+=1