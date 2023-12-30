# 풀이시간 1시간 20분/50분 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 시간제한 초과
# 맨 처음에 문제의 형식을 보고 하나씩 놔보면서 보는 완전탐색, 즉 브루트 포스 알고리즘이라는 걸 떠올렸다. 또한 순열을 사용해야함을 알았고, 시계방향과 반시계 방향 또한 친구를 놓는것은 상관없다는 것 또한 알아 차렸다. 또한 더해서 영역을 넓히는 아이디어까지 좋았다. 끝과 시작점을 찾는 아이디어가 그러하다. 하지만 순열을 사용했을 때, 풀이시간이 급격하게 커지는 것을 알지 못해서 15! 정도면 풀이시간 내에 든다고 생각했다. 여기서 부터가 제대로 접근하지 못한 시작이다.
# 그러다 보니 답자체는 맞게 나와도 알고리즘에서 시간초과가 나올 수 밖에 없었다.

# 2회차 풀이







































# 1회차 풀이
# 시간초과를 시작으로 아쉬운 점이 몇가지 있었다. 먼저 아이디어에서 정답지를 보고 원형을 펼치는 것뿐만 아니라 펼쳐서 두배로 늘릴 수 있다는 아이디어를 배웠다. 영역을 넓히는 아이디어도 알고 있었고, 원형을 다룰 때 펼치는 방식도 알고 있었지만 이 두가지를 혼합하는 것은 처음 보았다.
# 영역을 넓히는 문제 해결 방식 외에도 또 떠올리지 못한 것은 각 지점으로 필요한 만큼 끊어보지 못한 점이다. 한 지점으로 끊어보는 점도 있었지만 이러한 점은 두배로 펼치는 아이디를 얻었다면 접근할 수 있지 않았을까 라는 생각이 든다.

from itertools import permutations

# 여기서 시계회전으로 쓰는 아이디가 평상시 다운 아이디어이다.
def clock(n,start,value):
  start+=value
  if start>=n:
    start-=n
  return start

def check_scope(n,weak,start,end):
  count=0
  # print(n,weak,start,end)
  for i in weak:
    # print(i)
    for k in range(len(start)):
      if start[k]>end[k]:
        if (i>=start[k] and i<n) or i<=end[k]:
          count+=1
          break
      else:
        if i>=start[k] and i<=end[k]:
          count+=1
          break
  if count==len(weak):
    return True
  else:
    return False
      
    

def solution(n, weak, dist):
  answer=-1

  friend_num=len(dist)
  dist.reverse()
  # 친구들의 수를 최소로 하여 1명부터 ~ 최대 수까지 뽑아본다.
  for i in range(1,friend_num+1):
    # 이렇게 접근한 이유는 시간 복잡도를 고려를 하지 않고 접근해서 이러한 문제가 발생한 것이다.
    arr=list(permutations(weak,i))
    # 각 경우에서
    for one_case in arr:
      start=list(one_case)
      end=[]
      for k in range(len(one_case)):
        # 시계든 반시계든:
        end.append(clock(n,start[k],dist[k]))
      # print(start,end)
      if check_scope(n,weak,start,end):
        return i
      
  return answer

n=12
week=[1,5,6,10]
dist=[1,2,3,4]
print(solution(n,week,dist))

n=12
week=[1,3,4,9,10]
dist=[3,5,7]
print(solution(n,week,dist))

# def solution(n, weak, dist):
#   # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
#   length=len(weak)
#   for i in range(length):
#     weak.append(weak[i]+n)
#   answer=len(dist)+1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist)+1로 초기화
#   # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
#   for i in range(0,length):
#     # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
#     for case in list(permutations(dist,len(dist))):
#       count=1 # 투입할 친구의 수
#       # 해당 친구가 점검할 수 있는 마지막 위치
#       end=weak[i]+case[count-1]
#       # 시작점부터 모든 취약 지점을 확인
#       for k in range(i,i+length):
#         # 점검할 수 있는 위치를 벗어나는 경우
#         if end<weak[k]:
#           count+=1 # 새로운 친구를 투입
#           if count>len(dist): # 더 투입이 불가능하다면 종료
#             break
#           end=weak[k]+case[count-1]
#       answer=min(count,answer) # 최솟값 계산
#   if answer>len(dist):
#     answer=-1
#   return answer
