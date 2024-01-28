# 풀이시간 1분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 입력을 받은 수들의 갯수를 세는 문제이다.

from collections import Counter

n=int(input())
arr=list(map(int,input().split()))
counter=Counter(arr)
print(counter[int(input())])