# 풀이시간 30분 시간제한 0.1초 메모리제한 256MB
# 1회차 정답
# 데이터의 수가 1000이기 때문에 이중 배열로 풀어도 백만이 되어 0.1에 충분이 돌아갈 수 있다고 생각했다. 두개의 문자열에서 서로 문자가 하나씩 늘어날 때마다 모든 경우, 즉 최대로 긴 공통 부분수열의 길이를 재기 위해서는 비교를 해야되고 그 비교를 2차원 배열에 기록할 수 있다고 생각했다. 이 때, 문자가 늘어날 때마다 그전의 값이 지금값에 영향을 줄 수 있기 때문에 다이나믹 프로그래밍이라고 생각했다. 다이나믹 프로그래밍이라고 가정하고 2차원 배열을 만들었을 때, 영향을 줄 수 있는 것은 현재 추가되는 문자가 같은지, 다른지와 순서 정도라고 생각했고 문자가 같은 경우에서 증가하는 모습을 보였다. 즉 같은 문자가 추가되면 두개의 문자가 추가 되기 전보다 길이가 각 1씩 늘어나기 때문에 표의 왼쪽 위의 값보다 +1이 되고 같지 않을 경우에는 값이 늘어나지 않기 때문에 각 위쪽과 왼쪽의 값 중 큰 길이가 최대 길이가 된다.

s1=list(input())
s2=list(input())

dp=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]
for i in range(1,len(s1)+1):
  for j in range(1,len(s2)+1):
    if s1[i-1]==s2[j-1]:
      dp[i][j]=dp[i-1][j-1]+1
    else:
      dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[len(s1)][len(s2)])