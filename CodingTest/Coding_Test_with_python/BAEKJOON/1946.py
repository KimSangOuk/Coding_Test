# 풀이시간 20분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 각 순위 a,b를 받았을 때, 다른 모든 사람과 비교했을 때, 하나라도 높은게 있다면 count하는 문제이다. 모든 사람과 비교를 각 하면 가장 간단하겠지만 데이터의 수가 100,000이기 떄문에 이중 포문은 불가능하다. 그렇기 때문에, 첫번째 점수의 순위를 기준으로 정렬을 한다면, 다른 점수만 보았을 때, 위에서 부터 순위가 더 높다면 그 사람은 두개의 시험 중 하나의 순위는 높다는 뜻이 된다. 그렇기 때문에 그 순위를 업데이트 해가면서 수를 세어가면 된다.

for tc in range(int(input())):
  n=int(input())
  array=[]
  for i in range(n):
    a,b=map(int,input().split())
    array.append((a,b))
  array.sort()
  update=n+1
  count=0
  for i in range(n):
    if update>array[i][1]:
      update=array[i][1]
      count+=1
  print(count)