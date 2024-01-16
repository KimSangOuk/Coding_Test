# 풀이시간 45분/30분 시간제한 1초 메모리제한 128MB
# 3회차 정답 - but 풀이시간 오래 걸려서 더 풀어봄
# 음식의 양이 적은 순으로 다 먹어치우기 때문에 남은 시간동안 음식을 다 먹을 수 있는지에 따져가면서 heapq로 음식을 하나씩 제거해 가면서 풀면 되는 그리디 문제이다.
# 전체 음식을 다 먹을 수 있는지 없는지 판단하는 부분, 즉, 시간이 다되고 남은 음식이 있는지 처리하는 부분에서 시간이 조금 더 소모되었다. 전체의 음식량이 시간보다 적다면 다 먹을 수 있다는 뜻이다.

import heapq

def solution(food_times, k):
  answer = 0

  q=[]
  reduce=0
  
  for i in range(len(food_times)):
    heapq.heappush(q,(food_times[i],i+1))

  while q and k>=(q[0][0]-reduce)*len(q):
    k-=(q[0][0]-reduce)*len(q)
    reduce+=q[0][0]-reduce
    heapq.heappop(q)

  if q:
    q.sort(key=lambda x:x[1])
    answer=q[k%len(q)][1]
  else:
    answer=-1
  return answer

food_times=[3,1,2]
k=5
print(solution(food_times,k))

# 2회차 풀이
# 풀이시간 초과 시간제한 1초 메모리제한 128MB
# 2회차 오답 - 결국 정답을 내지 못함
# 아이디어 면에서 전에 풀었던 아이디어식, 즉 그리디 먼저 작은거부터 먹어치운다. 그리디의 아이디어의 핵심인 지금 원하는거부터 처리한다. 식으로 풀어낼 수 있었으나, 아이디어도 알고 있었고 구현에서 시간이 조금 걸렸음. 근데 여기서 문제 발생. 그리디 식으로 풀어내는데, while문에서 heapq를 처리해야 하는데 while문의 조건문에서는 그럼 처리를 하지 못하는 거임 여기서 아 어떡하지? 해서 여기서부터 다 꼬임, 걍 생각대로 구현이 안됨.
# 내 지식상에는 heapq의 정렬은 다 넣고 다 빼는거 까지가 한 템포라서 무조건 첫번째, 작은거를 찾아내기 위해서는 빼야됨, 하지만 사실 맨 앞에 있는게, 제일 작았던 거임. 이걸 모르는 이상 구현할 수가 없는 아이디어 였다. 나머지 구현 관련 아이디어는 다 맞음. 정답을 구해내는 부분에서, 남은 거의 번호 추출하는 부분만 빼고
import heapq

def solution(food_times, k):
  answer = 0

  q=[]
  for i in range(1,len(food_times)+1):
    heapq.heappush(q,(food_times[i-1],i))

  prev_food_amount_stack=0
  food_count=len(food_times)

  # 심지어 나는 누적 시간을 계산을 안하고 k에서 바로 빼기도 하고, 음식 갯수도 따로 변수를 안두고 len(q)로 세서 더 짧았음 코드가, 근데 그 안꺼내고 처음 값을 구할 수 없는 모순에 빠짐
  while k>=prev_food_amount_stack*food_count:
    now_food,now_food_index=heapq.heappop(q)
    prev_food_amount_stack+=now_food
    food_count-=1
    k-=prev_food_amount_stack*food_count

  # 여기서는 남은 음식중에서의 순서를 구해야됬는데, 앞에서 두번씩 빼거나 나중에 빼버리니까 이게 남은 음식이 q에 제대로 안남음. 그러니 헷갈려서 똥망
  answer=k%food_count+1
  
  return answer

food_times=[3,1,2]
k=5
print(solution(food_times,k))


# 풀이 시간 - 1시간 오버 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 결국 정답을 못냄
# 먼저 그리디인거는 작은 숫자부터 없애야한다 이거를 알고 있는거부터 그리디 아이디어는 합격인데, 방법을 찾지를 못함. 음식의 수를 줄여가면서 하는것도 알고리즘 상에도 좋고 시간 상에도 맞아떨어져서 다 좋았지만, 그 이후에 자료형을 알지 못한 대가가 큼.
# food_times의 길이가 200,000 이하이길래, 무조건 nlogn 알고리즘인데 길이는 곧 음식 종류의 수 이기에 음식의 종류를 줄이는 아이디어가 맞구나. 여기까지도 좋았음.

# 1회차 풀이
# 음식을 제거할 수 없는거부터 문제가 있었는데 아는 자료형이 없음. 그러다보니 다음 상황 생각을 못했고 최소를 없앤다. 이 아이디어 부터가 우선순위 큐를 생각할만함. 그리고 심지어 자료형에 이름도 붙어있으면 좋겠다는 생각을 했었고, 그래서 우선순위 큐를 구해서 그 자료형의 형태로 다시 그림을 그려봤어야함.
# 즉, 생각할 건 다 생각했는데 저 조건을 만족시키는, 즉 막힌 부분을 만족시키는 자료형을 찾지를 못함. 이게 핵심이다.******
def solution(food_times, k):
  answer = 0
  food_num=len(food_times)

  if k>=sum(food_times):
    return -1

  for _ in range(food_num): 
    min_food=min(food_times) # 아이디어는 괜찮았다고 생각되지만 문제점, 다 먹은 음식을 없앨 수가 없음. 이게 핵심 아이디어의 결함 -> 이게 우선순위 큐였으면 가장 작은 큐를 제거.
    if k<food_num: # 초가 음식 수보다 작으면 그냥 돌림
      answer=k+1
    else: # 초가 음식 수보다 많으면
      if min_food*food_num>k: # 제일 적게 남은 음식을 소모하는데 걸리는 시간보다 남은 시간이 적으면
        answer=k//food_num+1 # 음식 수로 최대한 소모 시킨 다음 돌림
      else: # 제일 적은 음식이 다 소모가 될 정도의 시간이 있으면 -> 만약 정답이였으면 소모가 다 될 시간이 있는지 확인하고 - 남은 음식 소모 시간 = (지금 큐에서 걸리는 시간 - 앞의 큐에서 걸렸던 시간) 확인하고
        k-=food_num*min_food # 음식 다 소모 한 시간 -> 총시간 업데이트 하고
        food_num-=1 # 음식 수도 줄임 -> 이건 맞고
        
  return answer

# 답안지
import heapq
def solution(food_times,k):

  # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
  if k>=sum(food_times):
    return -1

  # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
  q=[]
  for i in range(food_num):
    # (음식 시간, 음식 번호) 형태로 우선순위 큐를 이용
    heapq.heappush(q,(food_times[i],i))

  food_sum=0 # 먹기 위해 사용한 시간
  previous=0 # 직전에 다 먹은 음식 시간
  food_num=len(food_times) # 남은 음식의 개수

  # food_sum(먹기 위해 사용한 시간) + (현재의 음식 시간 - 이전 음식 시간)*현재 음식 개수와 k 비교
  while food_sum+(q[0][0]-previous)*food_num<=k:
    now=heapq.heappop(q)[0]
    food_sum+=food_num*(now-previous)
    previous=now # 이전 음식 시간 재설정
    food_num-=1 # 다 먹은 음식 제외

  # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
  result=sorted(q,key=lambda x:x[1]) # 음식의 번호 기준으로 정렬
  return result[(k-food_sum)%food_num][1]