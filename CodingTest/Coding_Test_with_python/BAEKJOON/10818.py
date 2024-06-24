# 풀이시간 5분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 배열을 받아서 단순히 최솟값과 최댓값을 출력하는 문제이다.

n=int(input())
array=list(map(int,input().split()))
print(min(array),max(array))