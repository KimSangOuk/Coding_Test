# 풀이시간 3분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 기존의 배열에서 입력받은 배열의 차를 구하면 되는 문제.

default=[1,1,2,2,2,8]
input_chess=list(map(int,input().split()))

for i in range(6):
    print(default[i]-input_chess[i],end=' ')