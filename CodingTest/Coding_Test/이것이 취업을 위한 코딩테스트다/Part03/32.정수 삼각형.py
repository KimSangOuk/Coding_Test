# 풀이시간 10분/30분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 단순히 위에서 찾은 답에서 아래로 내려가면서 최대의 크기를 기록시키면서 내려가면 되는 문제이다. 하지만 나의 경우, 반대로 한다면 더 빠르게 0,0의 좌표만 출력시키면 된다고 생각해서 역삼각형으로 풀어버렸다.

n=int(input())

triangle=[]
for _ in range(n):
  triangle.append(list(map(int,input().split())))

for i in range(n-2,-1,-1):
  for j in range(i+1):
    # print(i,j)
    triangle[i][j]+=max(triangle[i+1][j],triangle[i+1][j+1])

print(triangle[0][0])