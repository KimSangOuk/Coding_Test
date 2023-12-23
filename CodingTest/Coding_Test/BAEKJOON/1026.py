# 풀이시간 5분 시간제한 2초 메모리제한 128MB
# 1회차 정답
# 단순하게 가장 큰 수와 가장 작은 수의 곱들의 합이 최소가 된다는 점을 생각했을 때, 각 배열을 내림차순과 오름차순으로 정렬해서 곱의 합을 구하면되는 문제이다. 그리디 스럽다.

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

result=0
for i in range(n):
  result+=a[i]*b[i]

print(result)