# 풀이시간 1분 시간제한 1초 메모리제한 256MB
# 1회차 정답
# 단순히 오름차순 정렬한 후에 두번째 원소를 출력하면 되는 문제이다.

arr=list(map(int,input().split()))
arr.sort(reverse=True)
print(arr[1])