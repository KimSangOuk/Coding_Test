# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 입력받은 수를 문자로 받아서 수를 뒤집고 그 뒤집은 두수를 비교해서 큰 수를 출력하면 된다.

a,b=map(str,input().split())
a=int(a[::-1])
b=int(b[::-1])
if a<b:
    print(b)
else:
    print(a)