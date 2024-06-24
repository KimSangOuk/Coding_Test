# 풀이 시간 - 35분/40분 시간제한 1초 메모리제한 512MB
# 1회차 정답
# 여기서 시간 복잡도에 영향을 주는건 조합과 집의 수, 케이스에서의 길이 즉, m 인데 조합은 100,000을 넘지 않고 집은 100, m.은 13이니 3중으로 완전탐색으로 찾아도 시간초과가 나오지 않는다는 판단이 나온다.
# 또한 시간 복잡도 전에 아이디어 자체가 치킨 집들 중에서 조합으로 고른 후 일일이 완전탐색하면서 찾는 아이디어라고 볼 수 있다. 즉, 브루트포스 알고리즘인것이다.

from itertools import combinations

# n*n 크기의 도시 / 남길 치킨집 갯수 최대 m
n,m=map(int,input().split())

# 집 좌표들을 담을 리스트
home=[]
# 치킨집 좌표들을 담을 리스트
chicken=[]

for i in range(n):
  arr=list(map(int,input().split()))
  for j in range(n):
    if arr[j]==1:
      home.append((i+1,j+1))
    if arr[j]==2:
      chicken.append((i+1,j+1))

# 치킨 집들 중 m개를 선택한 리스트
selected_chicken=list(combinations(chicken,m))
# print(selected_chicken)

city_chicken=0
answer=1500
# 선택된 치킨들 중 한 케이스
for case in selected_chicken:
  for home_one in home:
    distance_chicken=100
    for chicken_one in case:
      distance_chicken=min(distance_chicken,abs(home_one[0]-chicken_one[0])+abs(home_one[1]-chicken_one[1]))
    city_chicken+=distance_chicken
  # print(city_chicken)
  answer=min(city_chicken,answer)
  city_chicken=0

print(answer)

# # 답안지
# from itertools import combinations

# n,m = map(int,input().split())
# chicken,house=[],[]

# for r in range(n):
#   data=list(map(int,input().split()))
#   for c in range(n):
#     if data[c]==1:
#       house.append((r,c)) # 일반 집
#     elif data[c]==2:
#       chicken.append((r,c)) # 치킨집

# # 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
# candidates=list(combinations(chicken,m))

# # 치킨 거리의 합을 계산하는 함수
# def get_sum(candidate):
#   result=0
#   # 모든 집에 대하여
#   for hx,hy in house:
#     # 가장 가까운 치킨집을 찾기
#     temp=1e9
#     for cx,cy in candidate:
#       temp=min(temp,abs(hx-cx)+abs(hy-cy))
#     # 가장 가까운 치킨집까지의 거리를 더하기
#     result+=temp
#   # 치킨 거리의 합 반환
#   return result

# # 치킨 거리의 합의 최소를 찾아 출력
# result=1e9
# for candidate in candidates:
#   result=min(result,get_sum(candidate))

# print(result)