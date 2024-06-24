# 풀이시간 5분 시간제한 2초 메모리제한 256MB
# 1회차 정답
# 데이터의 최대 크기가 100만이기 때문에 NlogN인 라이브러리를 이용해서 역순으로 정렬해서 출력하면 되는 문제.

n=int(input())

arr=[]
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
for i in range(n):
    print(arr[i])