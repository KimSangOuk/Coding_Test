# 풀이시간 1분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 별을 입력으로 받은 수의 역순으로 찍는 문제.

n=int(input())

for i in range(n,-1,-1):
    print("*"*i)