# 풀이시간 초과/40분 시간제한 1초 메모리제한 256MB
# 1회차 오답 - 풀이방식 접근 실패
# 다이나믹 프로그래밍이라는 주제를 모르고 접근했다면 다이나믹 프로그래밍인 것도 모를 정도의 문제였다. LIS(Longest Increasing Subsequence) - '가장 긴 증가하는 부분 수열'이라는 알고리즘을 사용하는 문제였는데 다이나믹의 기록이 이렇게도 쓰일 수 있구나라는 것을 알게해주는 문제였다. 알고리즘 자체는 단순히 보다 앞에서 연속될 수 있는 수를 찾아 수를 하나씩 올린 다음, 이어질 수 있는 최대 길이를 구하는 방식이었다.
# 나의 접근 같은 경우는 어떻게는 하나씩 영향을 받는 것을 찾아내려고 이리저리 d값으로 잡고 해보았지만 결국 접근하지 못하였다. d값에 오히려 집착하지 않고 풀이법을 찾으려했다면 풀었을 가능성이 더 높았을 것 같다. 길이가 최대로 이어지도록 스택을 쌓아보았다면 어땠을까 생각이 든다.

# 2회차 풀이




# 1회차 풀이
n=int(input())

array=[]
temp=list(map(int,input().split()))
for i in range(1,n+1):
  array.append((i,temp[i-1]))

array.sort(key=lambda x:x[1])

previous=array[0][0]
count=0
for num,value in array:
  if previous>num:
    count+=1

print(n-count)

# 답안 예시
n=int(input())
array=list(map(int,input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
d=[1]*(n+1)

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1,n+1):
  for j in range(i):
    if array[j]<array[i]:
      d[i]=max(d[i],d[j]+1)

# 열외시켜야 하는 병사의 최소 수를 출력
print(n-max(d))