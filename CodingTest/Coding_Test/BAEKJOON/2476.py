# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 각 인원수 만큼 주사위 값대로 해당 금액을 조건에 따라 구해내고 그 금액 중 최대 금액을 구하면 되는 문제.

max_value=0
n=int(input())

for i in range(n):
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    k=0
    if arr[0]==arr[1] and arr[1]==arr[2]:
        k=10000+arr[0]*1000
    elif arr[0]==arr[1] or arr[1]==arr[2]:
        same=arr[0] if arr[0]==arr[1] else arr[1]
        k=1000+same*100
    else:
        k=arr[0]*100
    max_value=max(max_value,k)

print(max_value)