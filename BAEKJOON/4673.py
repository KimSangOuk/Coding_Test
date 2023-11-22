# 풀이시간 30분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 10000보다 작은 숫자를 출력하는 것에서 쭉 10000 이하의 숫자를 다 둘러본 후 찾는 완전탐색, 브루트포스 알고리즘이라는 것을 깨달았다. 또한 10,000개 이기 때문에 돌아보는 수가 O(NlogN)가지의 알고리즘만 쓸 수 있다는 것을 알게 되었다.

def self_made(num):
  self=num
  length=len(str(num))
  for i in range(0,length):
    self+=int(str(num)[i])
  return self

arr=[]
for i in range(1,10001):
  if self_made(i)<=10000:
    arr.append(self_made(i))

arr.sort()

for i in range(1,10001):
  if i not in arr:
    print(i)