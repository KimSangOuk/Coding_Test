# 풀이시간 10분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 각 문자열의 글자 중 다른 수가 최소가 되는 갯수를 구하면 된다. 그렇기 위해서 모든 문자열의 구간을 탐색하면 된다.

a,b=map(str,input().split())

min_value=int(1e9)

for i in range(0,len(b)-len(a)+1):
    count=0
    for j in range(len(a)):
        if a[j]!=b[i+j]:
            count+=1
    min_value=min(min_value,count)

print(min_value)