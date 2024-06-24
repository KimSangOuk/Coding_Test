# 풀이시간 3분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 처음 주어진 수에서 나머지 입력되는 수들을 뺀 나머지를 구하는 문제

n=int(input())

for i in range(9):
    n-=int(input())

print(n)