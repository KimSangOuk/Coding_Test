# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 문자열을 받아서 세수가 같을 경우, 두수만 같을 경우, 세수 다 다를 경우를 분리해서 결과값을 조건대로 구해주면 된다.

arr=list(map(int,input().split()))
arr.sort(reverse=True)
result=0
if arr[0]==arr[1] and arr[1]==arr[2]:
    result=10000+arr[0]*1000
elif arr[0]==arr[1] or arr[1]==arr[2]:
    same=arr[0] if arr[0]==arr[1] else arr[1]
    result=1000+same*100
else:
    result=arr[0]*100

print(result)