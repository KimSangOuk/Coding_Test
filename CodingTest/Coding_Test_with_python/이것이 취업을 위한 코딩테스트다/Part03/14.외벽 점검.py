# 풀이시간 1시간/50분 시간제한 1초 메모리제한 128MB
# 3회차 오답 - 풀이시간 초과 및 풀이방법 도달 x
# 순열로 친구들을 놓는 모든 경우의 수를 탐색하면서 시작지점도 매번 다르게 해서 원형으로 시계 반시계로 작동하는 점까지 고려하는 브루트포스 알고리즘이자 시뮬레이션 유형이라고도 할 수 있을 것 같다.
# 마지막에 다 풀어놓고 케이스 안에서 -1로 바꾸어 버려서 전체 값이 한번 -1이 나오면 다시 안바뀌게 되는 점을 찾아내지 못했다. 왜 못찾았는가? count가 기존 인원을 넘어서는 순간 잘못되었기 때문에 -1 처리를 하려고 했지만 이 경우는 min이기 때문에 답에 바로 포함되어버려서 문제가 되었던 것이다. 답이 틀린 경우가 min이나 max를 통해서 걸러질 수 있는 경우를 고려하지 않고 바로 처리하려고 하였기 때문에 틀어졌다. 왜 바로 처리하려고 하였는가? 보통 같은 경우에는 바로 continue 시키거나 답에 포함시키도록 하는게 습관화 되어있기도 하고 이렇게 하는 경우는 드물기 때문에 헷갈렸다고 할 수 있다. 그렇기 때문에 다음에 답을 구하고 min처리를 한다면 그 답이 고정이 되어 다른 케이스 검사를 방해하는 것은 아닌지 살펴볼 필요가 있다.

from itertools import permutations
import copy

def solution(n, weak, dist):
  answer = len(dist)+1

  circle_weak=copy.deepcopy(weak)
  for i in range(len(weak)):
    circle_weak.append(weak[i]+n)

  friends_num=len(dist)
  for case in list(permutations(dist,friends_num)):
    for i in range(len(weak)):
      start=weak[i]
      count=1
      f_num=0
      end=start+case[f_num]
      # print("케이스별",case,start,end)
      for j in range(i,i+len(weak)):
        if end<circle_weak[j]:
          count+=1
          f_num+=1
          if f_num>=friends_num:
            break
          start=circle_weak[j]
          end=circle_weak[j]+case[f_num]
          # print("진행도",start,end)
      
      # print(count)
      answer=min(answer,count)
  if answer>friends_num:
    answer=-1
  return answer

# n = 200
# weak = [0, 10, 50, 80, 120, 160]
# dist = [1, 10, 5, 40, 30]
# # return = 3
# print(solution(n,weak,dist))

# n=12
# weak=[1,5,6,10]
# dist=[1,2,3,4]
# print(solution(n,weak,dist))

# n=12
# weak=[1,3,4,9,10]
# dist=[3,5,7]
# print(solution(n,weak,dist))














# 풀이시간 120분/50분 시간제한 1초 메모리제한 128MB
# 2회차 오답 - 풀이시간 초과 및 시간제한 넘어감, 오답도 발생
# 일단 나의 첫번째 잘못은 저번 기억에 너무 의존해서 시뮬레이션인지 브루트포스인지도 따지지 않고 풀기 시작했다는 점이다.
# 각 지점에 친구를 둔다는 아이디어는 생각해냈으나, 각 경우를 나아가면서 찾으려 해서 식이 복잡해지기 시작했다. 나아가면서 찾은 것이 틀린 아이디어는 아니나, 문제가 되었던 것은 어떤 지점에 어떤 친구를 두는지 정하는 기준이 애매 모호했다는 점이다.
# 그러나 순열을 사용해서 친구의 경우를 전부 사용하면서 나아가는 방법을 왜 사용해지 못했는가? 각 지점에 친구를 세워두기에는 지점의 수가 친구의 수보다 많고 정해진 점에 두는 것이 아니라 생각하기 어려웠다. 보통 순열이나 조합이라 함은 특정 리스트에서 뽑아서 어디 지점에 세워두는 것이 확실할 때, 사용하다보니 세워놓는 지점이 애매하고 나아가는 경우는 처음 접하다보니 사용하지 않게되었다.
# 그렇다면 다음에는 접했을 때, 어떻게 떠올릴 수 있겠는가? 각 지점에 친구를 세워둔다는 생각을 했다면 정확한 기준이 있고 그 기준에 따라서 내가 놓을 수 있는지를 따져야 한다. 내가 푼 방법의 경우, 애매한 기준이었기에 저렇게 풀기보다는 전부 세워보는 경우가 맞다고 할 수 있을 것이다. 그리고 특정기준이 아니라 순서가 필요한 경우에도 순열을 사용할 수 있다는 것을 문제에서 알 수 있다. 점의 수가 매번 불규칙하고 전부 친구가 필요한 경우가 아니더라도 우리는 경우가 올 수 있는 순서가 필요하고 모든 경우를 따질 필요가 있으므로 순열을 사용하는 것이다.
# 그 뿐만 아니라 친구의 시작지점을 정하는 기준도 나같은 경우는 그냥 추리였다. 정확한 판단이 아니라 모든 지점을 따질 필요가 있음에도 그렇게 하지 않고 예측으로 풀었다고 볼 수 있다.
# 기준이 애매하면 모든경우를 보는 브루트포스를 생각해보아라.

# def solution(n, weak, dist):
#   answer = 0
#   least=n*2
#   for i in range(len(weak)):
#     weak.append(weak[i]+n)
#   start=0
#   end=0
#   for i in range(len(weak)//2):
#     if weak[i+len(weak)//2-1]-weak[i]<least:
#       start=i
#       end=i+len(weak)//2-1
#       least=weak[i+len(weak)//2-1]-weak[i]
#   # print(start,end)
#   use=[False]*len(dist)
#   t=0
#   while True:
#     t+=1
#     # print(start,end)
#     max_num=0
#     use_one=0
#     last=0
#     for k in range(len(dist)):
#       if not use[k]:
#         test_dist=dist[k]+weak[start]
#         # print(test_dist,dist[k],weak[start])
#         count=0
#         tmp=0
#         for j in range(start,end+1):
#           if test_dist>=weak[j]:
#             # print(test_dist,weak[j])
#             count+=1
#             tmp=j
#         if count>max_num:
#           use_one=k
#           max_num=count
#           last=tmp
#           # print(use_one,count,last)
#     start=last+1
#     # print(start)
#     use[use_one]=True
#     if start>end:
#       break

#   for i in use:
#     if i:
#       answer+=1
#   return answer

# n=12
# weak=[1,5,6,10]
# dist=[1,2,3,4]
# print(solution(n,weak,dist))

# n=12
# weak=[1,3,4,9,10]
# dist=[3,5,7]
# print(solution(n,weak,dist))

# # 풀이시간 1시간 20분/50분 시간제한 1초 메모리제한 128MB
# # 1회차 오답 - 시간제한 초과
# # 맨 처음에 문제의 형식을 보고 하나씩 놔보면서 보는 완전탐색, 즉 브루트 포스 알고리즘이라는 걸 떠올렸다. 또한 순열을 사용해야함을 알았고, 시계방향과 반시계 방향 또한 친구를 놓는것은 상관없다는 것 또한 알아 차렸다. 또한 더해서 영역을 넓히는 아이디어까지 좋았다. 끝과 시작점을 찾는 아이디어가 그러하다. 하지만 순열을 사용했을 때, 풀이시간이 급격하게 커지는 것을 알지 못해서 15! 정도면 풀이시간 내에 든다고 생각했다. 여기서 부터가 제대로 접근하지 못한 시작이다.
# # 그러다 보니 답자체는 맞게 나와도 알고리즘에서 시간초과가 나올 수 밖에 없었다.

# # 1회차 풀이
# # 시간초과를 시작으로 아쉬운 점이 몇가지 있었다. 먼저 아이디어에서 정답지를 보고 원형을 펼치는 것뿐만 아니라 펼쳐서 두배로 늘릴 수 있다는 아이디어를 배웠다. 영역을 넓히는 아이디어도 알고 있었고, 원형을 다룰 때 펼치는 방식도 알고 있었지만 이 두가지를 혼합하는 것은 처음 보았다.
# # 영역을 넓히는 문제 해결 방식 외에도 또 떠올리지 못한 것은 각 지점으로 필요한 만큼 끊어보지 못한 점이다. 한 지점으로 끊어보는 점도 있었지만 이러한 점은 두배로 펼치는 아이디를 얻었다면 접근할 수 있지 않았을까 라는 생각이 든다.

# from itertools import permutations

# # 여기서 시계회전으로 쓰는 아이디가 평상시 다운 아이디어이다.
# def clock(n,start,value):
#   start+=value
#   if start>=n:
#     start-=n
#   return start

# def check_scope(n,weak,start,end):
#   count=0
#   # print(n,weak,start,end)
#   for i in weak:
#     # print(i)
#     for k in range(len(start)):
#       if start[k]>end[k]:
#         if (i>=start[k] and i<n) or i<=end[k]:
#           count+=1
#           break
#       else:
#         if i>=start[k] and i<=end[k]:
#           count+=1
#           break
#   if count==len(weak):
#     return True
#   else:
#     return False
      
    

# def solution(n, weak, dist):
#   answer=-1

#   friend_num=len(dist)
#   dist.reverse()
#   # 친구들의 수를 최소로 하여 1명부터 ~ 최대 수까지 뽑아본다.
#   for i in range(1,friend_num+1):
#     # 이렇게 접근한 이유는 시간 복잡도를 고려를 하지 않고 접근해서 이러한 문제가 발생한 것이다.
#     arr=list(permutations(weak,i))
#     # 각 경우에서
#     for one_case in arr:
#       start=list(one_case)
#       end=[]
#       for k in range(len(one_case)):
#         # 시계든 반시계든:
#         end.append(clock(n,start[k],dist[k]))
#       # print(start,end)
#       if check_scope(n,weak,start,end):
#         return i
      
#   return answer

# n=12
# week=[1,5,6,10]
# dist=[1,2,3,4]
# print(solution(n,week,dist))

# n=12
# week=[1,3,4,9,10]
# dist=[3,5,7]
# print(solution(n,week,dist))

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
