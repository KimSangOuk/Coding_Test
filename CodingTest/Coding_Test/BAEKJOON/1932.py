# 이것이 취업을 위한 코딩테스트다 part03 '32. 정수 삼각형'과 동일

n=int(input())

triangle=[]
for _ in range(n):
  triangle.append(list(map(int,input().split())))

for i in range(n-2,-1,-1):
  for j in range(i+1):
    # print(i,j)
    triangle[i][j]+=max(triangle[i+1][j],triangle[i+1][j+1])

print(triangle[0][0])