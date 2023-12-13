# 정수 N을 입력받기
n=int(input())
# 모든 식량 정보 입력받기
arr=list(map(int,input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d=[0]*(n+1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[1]=arr[0]
d[2]=max(arr[0],arr[1])
for i in range(3,n+1):
  d[i]=max(d[i-1],d[i-2]+arr[i-1])

# 계산된 결과 출력
print(d[n])