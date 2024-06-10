# 구하지 못하는 경우를 생각해서 5원을 중심으로 갯수를 줄여가면서 2원이 나머지 돈을 처리할 수 있는지를 고려하며 반복문을 사용하였다. 최대 5원이 될 수 있는 갯수를 구하고 반복문을 사용하되 중간에 가능한 케이스가 있으면 그 케이스가 최소가 되는 케이스이므로, 즉 5원이 가장 많이 사용되면서 2원으로 나머지가 떨어지는 케이스이므로 break 시켰다. 값에 변화가 없이, 즉 나누어지는 케이스가 없으면 -1을 출력한다.
# 풀이시간 : 5분

n=int(input())

max_cnt_5=n//5
answer=100000
for i in range(max_cnt_5,-1,-1):
    if (n-i*5)%2==0:
        answer=min(i+(n-i*5)//2,answer)
        break
if answer==100000:
    print(-1)
else:
    print(answer)