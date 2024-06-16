# - 정렬된 배열과 역정렬된 배열과 비교 후 출력을 다르게 해주면 된다.
# - 풀이시간 : 3분

arr=list(map(int,input().split()))
a=sorted(arr)
b=sorted(arr,reverse=True)
if arr==a:
    print("ascending")
elif arr==b:
    print("descending")
else:
    print("mixed")