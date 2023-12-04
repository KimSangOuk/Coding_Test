# 풀이 시간 - 10분/30분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# n이 100,000이하기 때문에 적어도 O(nlogn) 알고리즘 사용 필요해보임
# 작은 수부터 조를 형성해서 최대 조의 수를 구하기 때문에 그리디 알고리즘

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
count=0
space=0
result=0
for i in arr:
  space=max(i,space) # 이 부분만 다른데, 조의 최대 공간을 표현하고 싶었다.
  count+=1
  if space==count: # 어차피 공간과 수가 일치하는 순간에 조가 결정된다. 남는 인원이 생길뿐
    result+=1
    count=0

print(result)

# 답안지
# n = int(input())
# data=list(map(int,input().split()))
# data.sort()

# result=0 # 총 그룹의 수
# count=0 # 현재 그룹에 포함된 모험가의 수
# for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
#   count+=1 # 현재 그룹에 모험가를 포함시키기
#   if count>=i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
#     result+=1 # 총 그룹의 수 증가시키기
#     count=0 # 현재 그룹에 포함된 모험가의 수 초기화

# print(result) # 총 그룹의 수 출력