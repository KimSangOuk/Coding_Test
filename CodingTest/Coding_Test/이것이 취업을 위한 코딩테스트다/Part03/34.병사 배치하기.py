# 풀이시간 8분/40분 시간제한 1초 메모리제한 256MB
# 3회차 정답
# 가장 긴 증가하는 부분 수열의 한 종류이다. 현재까지의 최대 길이를 기록하는 식인데, 현재까지의 최대 길이는 앞에서 현재의 수보다 작은 수들 중에 가장 길이가 길어진 수의 +1이므로 이를 식으로 표현해서 풀수 있다.

n=int(input())
array=list(map(int,input().split()))
array.reverse()

dp=[1]*(n)

for i in range(0,n):
    max_value=0
    for j in range(i):
        if array[j]<array[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))

# 풀이시간 60분/40분 시간제한 1초 메모리제한 256MB
# 2회차 풀이 - 풀이방식 접근 실패
# 가장 긴 증가하는 부분 수열이라는 알고리즘을 완전히 저번에 숙지하지 못해서 한참 뺑뺑 돌아가다가 결국 풀지 못했다.
# 가장 긴 증가하는 부분 수열(LIS) 의 기본 아이디어는 다음과 같다.
# 앞에서부터 인덱스의 값이 i일 때, 그 인덱스보다 작은 값들에 대하여 현재의 수보다 그 수들이 작은 경우 보다 1이 큰 것이 현재의 값이 되는것이다. 즉 최대값을 찾아나가면 되는 것이다.

n=int(input())

arr=list(map(int,input().split()))+[0]
arr.reverse()

dp=[0]*(n+1)
max_value=0
for i in range(1,n+1):
  if arr[i]>=arr[i-1]:
    dp[i]=dp[i-1]+1
  else:
    dp[i]=dp[i-1]

# print(dp)
print(n-dp[n])

# 풀이시간 초과/40분 시간제한 1초 메모리제한 256MB
# 1회차 오답 - 풀이방식 접근 실패
# 다이나믹 프로그래밍이라는 주제를 모르고 접근했다면 다이나믹 프로그래밍인 것도 모를 정도의 문제였다. LIS(Longest Increasing Subsequence) - '가장 긴 증가하는 부분 수열'이라는 알고리즘을 사용하는 문제였는데 다이나믹의 기록이 이렇게도 쓰일 수 있구나라는 것을 알게해주는 문제였다. 알고리즘 자체는 단순히 보다 앞에서 연속될 수 있는 수를 찾아 수를 하나씩 올린 다음, 이어질 수 있는 최대 길이를 구하는 방식이었다.
# 나의 접근 같은 경우는 어떻게는 하나씩 영향을 받는 것을 찾아내려고 이리저리 d값으로 잡고 해보았지만 결국 접근하지 못하였다. d값에 오히려 집착하지 않고 풀이법을 찾으려했다면 풀었을 가능성이 더 높았을 것 같다. 길이가 최대로 이어지도록 스택을 쌓아보았다면 어땠을까 생각이 든다.

# 1회차 풀이
# n=int(input())

# array=[]
# temp=list(map(int,input().split()))
# for i in range(1,n+1):
#   array.append((i,temp[i-1]))

# array.sort(key=lambda x:x[1])

# previous=array[0][0]
# count=0
# for num,value in array:
#   if previous>num:
#     count+=1

# print(n-count)

# # 답안 예시
# n=int(input())
# array=list(map(int,input().split()))
# # 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
# array.reverse()

# # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
# d=[1]*(n+1)

# # 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
# for i in range(1,n+1):
#   for j in range(i):
#     if array[j]<array[i]:
#       d[i]=max(d[i],d[j]+1)

# # 열외시켜야 하는 병사의 최소 수를 출력
# print(n-max(d))