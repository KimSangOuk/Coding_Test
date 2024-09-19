N=int(input())

s=[list(map(int,input().split())) for _ in range(N)]
answer=1e9

def cal(arr):
    sumValue=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sumValue+=s[arr[i]][arr[j]]+s[arr[j]][arr[i]]
    return sumValue

for i in range(1<<N):
    team1,team2=[],[]
    for j in range(N):
        if (1<<j)&i:
            team1.append(j)
        else:
            team2.append(j)
    if team1 and team2:
        answer=min(answer,abs(cal(team1)-cal(team2)))

print(answer)