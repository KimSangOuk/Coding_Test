# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순히 주어진 식을 출력하면 되는 문제이다.

a,b,c=map(int,input().split())

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)