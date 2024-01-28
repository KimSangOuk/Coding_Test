# 풀이시간 3분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 스와이프를 해가면서 풀면 되는 문제.

m=int(input())
ball=[0]*4
ball[1]=1
for _ in range(m):
    a,b=map(int,input().split())
    ball[a],ball[b]=ball[b],ball[a]

for i in range(1,4):
    if bool(ball[i]):
        print(i)