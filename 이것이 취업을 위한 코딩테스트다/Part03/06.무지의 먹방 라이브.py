# 풀이 시간 - 1시간 오버 시간제한 1초 메모리제한 128MB
# 1회차 오답
# 먼저 그리디인거는 작은 숫자부터 없애야한다 이거를 알고 있는거부터 그리디 아이디어는 합격인데, 방법을 찾지를 못함. 음식의 수를 줄여가면서 하는것도 알고리즘 상에도 좋고 시간 상에도 맞아떨어져서 다 좋았지만, 그 이후에 자료형을 알지 못한 대가가 큼.
# food_times의 길이가 200,000 이하이길래, 무조건 nlogn 알고리즘인데 길이는 곧 음식 종류의 수 이기에 음식의 종류를 줄이는 아이디어가 맞구나. 여기까지도 좋았음.

# 2회차 풀이


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

# # 답안지
# import heapq
# def solution(food_times,k):
#   answer=0
#   food_num=len(food_times)

#   if k>=sum(food_times):
#     return -1

#   q=[]
#   for i in range(food_num):
#     heapq.heappush(q,(food_times[i],i))

#   food_sum=0
#   previous=0
#   while food_sum+(q[0][0]-previous)*food_num<=k:
#     now=heapq.heappop(q)[0]
#     food_sum+=food_num*(now-previous)
#     previous=now
#     food_num-=1

#   result=sorted(q,key=lambda x:x[1])
#   return result[(k-food_sum)%food_num][1]