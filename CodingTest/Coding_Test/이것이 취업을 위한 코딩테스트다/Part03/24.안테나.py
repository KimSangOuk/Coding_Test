# 풀이시간 over/20분 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 풀이방식 접근 못함
# 먼저 데이터의 수가 200,000이기 때문에 정렬 방식은 O(NlogN)의 퀵 정렬이나 계수 정렬을 사용할 수 밖에 없다. 그렇기에 정렬을 sort()를 사용해서 진행하였다. 거리의 합이 최소가 되는 점을 찾는 문제였는데, 최소가 되는 점을 찾는 방식을 내가 생각해내지 못했다.

n=int(input())
arr=list(map(int,input().split()))

arr.sort()
value=sum(arr)/len(arr)

answer=0
t=200000
for k in arr:
  if abs(k-value)<t:
    answer=k
    t=abs(k-value)
    

print(answer)