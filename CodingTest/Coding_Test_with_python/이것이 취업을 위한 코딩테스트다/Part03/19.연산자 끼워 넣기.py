# 풀이시간 초과/30분 시간제한 2초 메모리제한 512MB
# 2회차 정답
# 정해진 부호의 개수를 사용하면서 dfs로 깊이 탐색처럼 들어갔다가 부호가 전부다 소진되면, 즉 가장 깊이 들어간 숫자를 다 쓴 상태가 되면 결과를 비교하여 답을 도출해 내면서 모든 경우를 탐색하는 식으로 구하면 되는 문제이다. DFS의 시간복잡도는 O(N)이지만 데이터의 수가 작기 때문에 충분히 가능하다.

n=int(input())

num=list(map(int,input().split()))

code=list(map(int,input().split()))

max_answer=-int(1e9)
min_answer=int(1e9)

def dfs(result,deep):
  global max_answer,min_answer
  if deep==n:
    max_answer=max(result,max_answer)
    min_answer=min(result,min_answer)
  else:
    if code[0]>0:
      deep+=1
      code[0]-=1
      dfs(result+num[deep-1],deep)
      code[0]+=1
      deep-=1
    if code[1]>0:
      deep+=1
      code[1]-=1
      dfs(result-num[deep-1],deep)
      code[1]+=1
      deep-=1
    if code[2]>0:
      deep+=1
      code[2]-=1
      dfs(result*num[deep-1],deep)
      code[2]+=1
      deep-=1
    if code[3]>0:
      deep+=1
      code[3]-=1
      if result<0:
        result=-result 
        result=-(result//num[deep-1])
      else:
        result=result//num[deep-1]
      dfs(result,deep)
      code[3]+=1
      deep-=1

dfs(num[0],1)
print(max_answer)
print(min_answer)

# 풀이시간 초과/30분 시간제한 2초 메모리제한 512MB
# 1회차 오답 - 답 유출 실패
# 재귀함수를 사용해서 dfs까지는 알겠는데 더 이상 접근이 안됬다. 접근 방식을 점화식이나 조건문으로 생각하려고 해봐도 그림이 안그려졌다. 저번 풀이가 맞았었는데 아마 조합이나 이런걸로 푼거 같고 dfs로 푼거 같지는 않다.
# 재귀함수에 맨 처음 무슨 값을 넣고 어떤 결과에서 돌아올지 부터가 상상이 안됬다. 계산한 값이 들어가서 또 계산하는 거 까지는 알겠는데, 어떤 값을 넣어야 끝에서 끝나는지가 알 수가 없었고 값이 많다보니까 global 선언도 어떤걸 써야되는지 감이 안왔다.
# 끝나는 조건을 생각해보는게 답인 것 같다. 끝에서 돌아올 조건과 그 끝까지 가는 조건 이 두가지는 확실하다. 그리고 재귀함수에서 값을 변경해서 다음 재귀함수에 넣는 그림을 그려보는게 좋은 것 같다.
# 이 부분은 계속해서 연습하고 답지를 안보고 조건을 찾아가려는 연습을 해야하는 부분이 것 같다.

# # 답안 예시
# n=int(input())
# # 연산을 수행하고자 하는 수 리스트
# num_list=list(map(int,input().split()))
# # 더하기, 빼기, 곱하기, 나누기 연산자 개수
# plus,minus,mul,div=map(int,input().split())

# # 최댓값과 최솟값 초기화
# min_value=1e9
# max_value=-1e9

# # 깊이 우선 탐색 메서드
# def dfs(i,now):
#   global min_value, max_value, plus,minus,mul,div
#   # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
#   if i==n:
#     min_value=min(min_value,now)
#     max_value=min(max_value,now)
#   else:
#     # 각 연산자에 대하여 재귀적으로 수행
#     if plus>0:
#       plus-=1
#       dfs(i+1,now+num_list[i])
#       plus+=1
#     if minus>0:
#       minus-=1
#       dfs(i+1,now-num_list[i])
#       minus+=1
#     if mul>0:
#       mul-=1
#       dfs(i+1,now*num_list[i])
#       mul+=1
#     if div>0:
#       div-=1
#       dfs(i+1,int(now/num_list[i]))
#       div+=1
      
# dfs(1,num_list[0])