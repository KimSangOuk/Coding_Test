# - 각 주어지는 물건의 계산의 합이 주어진 합과 일치하는지를 비교해주면 된다.
# - 풀이시간 : 3분

total=int(input())
n=int(input())
cal=0
for i in range(n):
    a,b=map(int,input().split())
    cal+=a*b
if cal==total:
    print("Yes")
else:
    print("No")