# 풀이시간 3시간 시간제한 1초 메모리제한 256MB
# 1회차 오답 - 풀이시간 초과, 풀이방법에 접근하지 못함
# 결국 답지를 보고 풀이방식을 이해했다.
# 왜 풀지 못했는가? 그리디에서 제일 하면 안되는 짓인, 규칙을 찾으려고 발버둥 쳤고, 결국 규칙을 찾아내지 못했다. 그리디는 있는 그대로 각 상황에서 필요한 것만 챙기는 알고리즘인데, 규칙을 찾으려고 계속 무언가 했다.
# 왜 풀지 못했는가? 전체를 힙큐에 넣고 뺄 생각만 계속해서 했다. 그러다보니 전체에서 통일되는 규칙을 찾아야만 했고, 결국 찾지 못했다. 왜 계속 전체를 힙큐에 넣으려고 하였는가? 필요한 부분만 힙큐에 넣으려고 해본 적이 없기도 하고, 전체적인 데이터량만 보고 전체를 넣는거라고 착각해버렸다.
# 다음에는 어떻게 이러한 것들을 피하고 올바른 답을 찾을 수 있겠는가? 일단, 우리가 필요로 하는 범위를 상황에 따라 구해보고 그 범위내에서 정렬이 필요한 것인지 아니면 전체범위에서 필요한 것인지 생각을 해봐야겠다. 그리고 문제에서 던져주는 데이터의 수가 꼭 전체 범위가 아니라는 사실 또한 인지해야겠다.
# 그리고 그리디 문제일 경우에는, 지금 내가 상황별로 필요로 한게 무엇인지 이것이 범위를 나누는지도 생각해봐야겠다.

import heapq

n,k=map(int,input().split())

jewels=[]
bags=[]

for _ in range(n):
  m,v=map(int,input().split())
  heapq.heappush(jewels,(m,v))

for _ in range(k):
  c=int(input())
  bags.append(c)

result=0
bags.sort()
bag_num=0
real_take=[[] for _ in range(len(bags))]
while True:
  if bag_num>len(bags)-1:
    break
  if not jewels:
    break
  m,v=heapq.heappop(jewels)
  c=bags[bag_num]
  
  if m<=c and len(real_take[bag_num])==0:
    real_take[bag_num].append((m,v))
  elif m<=c and len(real_take[bag_num])>0:
    if real_take[bag_num][0][1]>=v:
      bag_num+=1
      heapq.heappush(jewels,(m,v))
    elif real_take[bag_num][0][1]<v:
      tmp=real_take[bag_num].pop(0)
      real_take[bag_num].append((m,v))
      heapq.heappush(jewels,tmp)
  elif m>c:
    bag_num+=1
    heapq.heappush(jewels,(m,v))

  # print(real_take)

for i in range(len(real_take)):
  if real_take[i]:
    result+=real_take[i][0][1]

print(result)


import sys
import heapq # 힙
input=sys.stdin.readline # 입력 빠르게
n,k = map(int,input().split())
gems = [[*map(int,input().split())] for _ in range(n)]
bags = [int(input()) for _ in range(k)]
gems.sort() # 무게 오름차순, 무게 같으면 가격 오름차순
bags.sort() # 가방 무게 오름차순
result = 0 # 결과 출력값 초기화
tmp = [] # 보석의 가격 저장 리스트

for bag in bags: # 각 가방 무게에 대해
    while gems and gems[0][0] <= bag: #제일 가벼운 보석무게를 bag이 허용하는한 반복
        heapq.heappush(tmp, -gems[0][1]) # 가격을 최대힙에 저장(음수로 저장하여 최소힙을 최대힙으로)
        heapq.heappop(gems) # 가격 저장한 보석은 버리기
    if tmp: #bag 무게 이하 보석 가격 다 저장했으면
        result -= heapq.heappop(tmp) # 제일 가치가 높은 가격 더하기(음수니까 빼기)
print(result)

#######

import heapq

n,k=map(int,input().split())

jewels=[]
for _ in range(n):
    heapq.heappush(jewels,list(map(int,input().split())))

bags=[]
for _ in range(k):
    heapq.heappush(bags,int(input()))

tmp=[]
answer=0
while bags:
    bag=heapq.heappop(bags)
    while jewels and bag>=jewels[0][0]:
        heapq.heappush(tmp,-heapq.heappop(jewels)[1])
    if tmp:
        answer+=-heapq.heappop(tmp)
print(answer)