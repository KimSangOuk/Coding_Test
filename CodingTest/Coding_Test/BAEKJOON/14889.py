# 풀이시간 20분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 단순히 각 팀이 이루어지는 경우를 구해서 팀에 소속되는 경우와 안되는 경우를 구분해서 각 차의 최소를 구하는 모든 경우의 수를 탐색하는 완전 탐색, 브루트 포스 알고리즘이다.

from itertools import combinations

n=int(input())
team_num=n//2
whole=[i for i in range(n)]

board=[]
whole_team=0
for i in range(n):
  board.append(list(map(int,input().split())))
  

cases=list(combinations(whole,team_num))
result=0
answer=int(1e9)

for case in cases:
  team1=0
  team2=0
  for i in range(n):
    for j in range(n):
      if i in case and j in case:
        team1+=board[i][j]
      elif i not in case and j not in case:
        team2+=board[i][j]
  result=abs(team1-team2)
  answer=min(answer,result)

print(answer)