# 풀이시간 3분 시간제한 1초 메모리제한 1024MB
# 1회차 정답
# 배열을 역순으로 정렬해서 앞에서부터 k-1번째 순서를 출력하면 되는 문제이다.

n,k=map(int,input().split())
array=list(map(int,input().split()))

array.sort(reverse=True)
print(array[k-1])