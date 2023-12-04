# 이것이 취업을 위한 코딩테스트다 part03 '13. 치킨 배달'와 동일

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