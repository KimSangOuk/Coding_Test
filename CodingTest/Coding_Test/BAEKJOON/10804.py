# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 1~20까지 들어있는 배열에서 각 구간의 숫자를 교환하면 되는 문제이다.

arr=[0]*21
for i in range(1,21):
    arr[i]=i

for _ in range(10):
    a,b=map(int,input().split())
    arr[a:b+1]=arr[b:a-1:-1]

print(*arr[1:])