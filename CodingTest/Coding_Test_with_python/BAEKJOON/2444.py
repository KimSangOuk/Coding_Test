# 별의 갯수의 규칙을 파악해서 별과 공백을 갯수를 맞춰서 출력해주면 된다.
# 풀이시간 : 3분

n=int(input())

for i in range(1,n):
    print((n-i)*" ",end="")
    print("*"*(1+(i-1)*2))

print("*"*(n+n-1))

for i in range(1,n):
    print(" "*(i),end='')
    print("*"*((n+n-1)-2*(i)))