# 풀이시간 25분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 앞에 3,2,1 전의 개수의 합을 더한 값이 정답이 되는 문제이다. 그렇기 때문에 다이나믹 프로그래밍으로 바텀 업해서 풀 수 있다. 원리는 더할 수 있는 수가 3,2,1이기 때문에 앞에 수에 1,2,3,을 더하는 가짓수를 구하면 된다는 뜻인것 같다.

for _ in range(int(input())):
  n=int(input())

  d=[1]*(n+1)
  d[1]=1

  for i in range(2,n+1):
    first,second,third=0,0,0
    if i-3>=0:
      first=d[i-3]
    if i-2>=0:
      second=d[i-2]
    if i-1>=0:
      third=d[i-1]
    d[i]=first+second+third
    #print(i,d[i],first,second,third)

  print(d[n])