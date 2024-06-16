# - 공백 부분은 갯수를 증가시키며 "*"은 갯수를 줄여가며 출력하면 된다.
# - 풀이 시간 : 3분

n=int(input())
for i in range(n):
    print(" "*i+"*"*(n-i))