# 풀이시간 3분 시간제한 2초 메모리제한 512MB
# 1회차 정답
# 정렬한 후 주어진 번째 수를 출력하면 되는 문제이다.

n,k=map(int,input().split())
array=list(map(int,input().split()))
array.sort()
print(array[k-1])