# 풀이시간 초과/30분 시간제한 2초 메모리제한 512MB
# 1회차 오답 - 답 유출 실패
# 재귀함수를 사용해서 dfs까지는 알겠는데 더 이상 접근이 안됬다. 접근 방식을 점화식이나 조건문으로 생각하려고 해봐도 그림이 안그려졌다. 저번 풀이가 맞았었는데 아마 조합이나 이런걸로 푼거 같고 dfs로 푼거 같지는 않다.
# 재귀함수에 맨 처음 무슨 값을 넣고 어떤 결과에서 돌아올지 부터가 상상이 안됬다. 계산한 값이 들어가서 또 계산하는 거 까지는 알겠는데, 어떤 값을 넣어야 끝에서 끝나는지가 알 수가 없었고 값이 많다보니까 global 선언도 어떤걸 써야되는지 감이 안왔다.
# 끝나는 조건을 생각해보는게 답인 것 같다. 끝에서 돌아올 조건과 그 끝까지 가는 조건 이 두가지는 확실하다. 그리고 재귀함수에서 값을 변경해서 다음 재귀함수에 넣는 그림을 그려보는게 좋은 것 같다.
# 이 부분은 계속해서 연습하고 답지를 안보고 조건을 찾아가려는 연습을 해야하는 부분이 것 같다.

# 답안 예시
n=int(input())
# 연산을 수행하고자 하는 수 리스트
num_list=list(map(int,input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
plus,minus,mul,div=map(int,input().split())

# 최댓값과 최솟값 초기화
min_value=1e9
max_value=-1e9

# 깊이 우선 탐색 메서드
def dfs(i,now):
  global min_value, max_value, plus,minus,mul,div
  # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
  if i==n:
    min_value=min(min_value,now)
    max_value=min(max_value,now)
  else:
    # 각 연산자에 대하여 재귀적으로 수행
    if plus>0:
      plus-=1
      dfs(i+1,now+num_list[i])
      plus+=1
    if minus>0:
      minus-=1
      dfs(i+1,now-num_list[i])
      minus+=1
    if mul>0:
      mul-=1
      dfs(i+1,now*num_list[i])
      mul+=1
    if div>0:
      div-=1
      dfs(i+1,int(now/num_list[i]))
      div+=1
      
dfs(1,num_list[0])