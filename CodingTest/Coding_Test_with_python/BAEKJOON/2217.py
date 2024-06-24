# 풀이시간 10분 시간제한 2초 메모리제한 192MB
# 1회차 정답
# 로프를 배열로 받아 내림차순으로 정렬한 다음 각 로프에서 구해지는 최대 중량을 구하면 되는 문제이다. 지금 필요한 최대 중량만 구해서 비교하므로, 그리디 알고리즘이라고 할 수 있다.

n=int(input())
ropes=[]
for _ in range(n):
  ropes.append(int(input()))

ropes.sort(reverse=True)

count=1
result=0
for rope in ropes:
  weight=rope*count
  result=max(weight,result)
  count+=1

print(result)