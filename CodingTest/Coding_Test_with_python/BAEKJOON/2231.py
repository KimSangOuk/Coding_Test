# 풀이시간 10분 시간제한 2초 메모리제한 192MB
# 1회차 정답
# 시간 복잡도 면에서 했갈렸는데 1,000,000개의 for문이 최소한 돌아가야되는데 그 자리수는 해봤자 길어야 7개까지 이기 때문에 10,000,000이 넘어가지 않아서 이중포문이 가까스로 가능하다. 알고리즘 면에서는 생성자를 현재 수까지 하나씩 따져가면서 찾는것이기 때문에 브루스포스 알고리즘이다.

n=int(input())
result=0
for i in range(1,n):
  length=len(str(i))
  self=i
  for j in range(0,length):
    self+=int(str(i)[j])
  if self==n:
    result=i
    break

if result==0:
  print(0)
else:
  print(result)