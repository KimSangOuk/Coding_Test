# 풀이시간 10분 시간제한 0.5초 메모리제한 128MB
# 1회차 정답
# 단순히 전층과 현재층의 전방의 합으로 구하고자 하는 층과 방에 인원 수를 구하는 문제이다. 그렇기에 일일이 다 더해도 좋지만은 앞에 값을 저장하는 형태로 구하는 게 제일 좋다. 이것이 다이나믹 프로그래밍이다.

for _ in range(int(input())):
  k=int(input())
  n=int(input())

  d=[[0]*(n+1) for _ in range(k+1)]

  for i in range(1,n+1):
    d[0][i]=i

  for i in range(1,k+1):
    for j in range(1,n+1):
      d[i][j]=d[i-1][j]+d[i][j-1]

  print(d[k][n])