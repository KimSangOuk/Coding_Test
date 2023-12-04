# 풀이 시간 - 15분/30분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# n의 크기가 1000보다 작거나 같기 때문에 O(N^2)이하의 알고리즘으로 풀어야 한다고 생각
# 숫자를 정렬하고 내가 원하는(그리디) 기준에 맞춰서 무게를 보니 남은 갯수와 현재 무게의 수를 곱하면 내가 현재 무게에서 원하는 가짓수가 나옴. 그래서 그리디 알고리즘으로 품.

n,m=map(int,input().split())
num=[0]*m
arr=list(map(int,input().split()))
arr.sort()
result=0

for i in arr:
  num[i-1]+=1

for i in range(m):
  n-=num[i]
  result+=n*num[i]

print(result)

# 답안지
# n,m=map(int,input().split())
# data=list(map(int,input().split()))

# # 1부터 10까지의 무게를 담을 수 있는 리스트
# array=[0]*11 # 여기서만 나만 다르게 모든 무게를 포함할 수 있게 만들어놓고 무게에서 굳이 안빼도 되게 숫자를 만들어 놓음
# for x in data:
#   # 각 무게에 해당하는 볼링공의 개수 카운트
#   array[x]+=1

# result=0
# # 1부터 m까지의 각 무게에 대하여 처리
# for i in range(1,m+1):
#   n-=array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
#   result+=array[i]*n # B가 선택하는 경우의 수와 곱하기

# print(result)