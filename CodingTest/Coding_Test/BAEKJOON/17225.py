import sys
input=sys.stdin.readline

A,B,N=map(int,input().split())

result_A=[]
result_B=[]

blue_t=0
red_t=0
cnt=1
result=[]
for _ in range(N):
    t,who,num=map(str,input().split())
    t,num=int(t),int(num)
    if who=='B' and blue_t<t:
        blue_t=t
    if who=='R' and red_t<t:
        red_t=t
    for _ in range(num):
        if who=='B':
            result.append(('B',blue_t))
            blue_t+=A
        if who=='R':
            result.append(('R',red_t))
            red_t+=B

result.sort(key=lambda x:(x[1],x[0]))
for k in range(1,len(result)+1):
    if result[k-1][0]=='B':
        result_A.append(k)
    else:
        result_B.append(k)

print(len(result_A))
print(*result_A)
print(len(result_B))
print(*result_B)