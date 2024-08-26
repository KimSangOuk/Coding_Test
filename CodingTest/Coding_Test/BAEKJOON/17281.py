from itertools import permutations

n=int(input())

go_by_inning=[list(map(int,input().split())) for _ in range(n)]

cases=list(permutations(range(2,10),8))
# print(cases)

max_score=0

for case in cases:
    go=[]
    out_cnt=0
    num=0
    inning_cnt=0
    score=0
    case=list(case)
    case=case[0:3]+[1]+case[3:]
    while True:
        # print(case,num)
        if go_by_inning[inning_cnt][case[num]-1]==0:
            out_cnt+=1
            if out_cnt>=3:
                out_cnt=0
                inning_cnt+=1
                go=[]
                if inning_cnt==n:
                    break
        else:
            if go_by_inning[inning_cnt][case[num]-1]>=4:
                score+=len(go)+1
                go=[]
            else:
                new_go=[]
                for i in range(len(go)):
                    if (go[i]+go_by_inning[inning_cnt][case[num]-1])>=4:
                        score+=1
                    else:
                        new_go.append(go[i]+go_by_inning[inning_cnt][case[num]-1])
                new_go.append(go_by_inning[inning_cnt][case[num]-1])
                go=new_go
        num=(num+1)%9
    max_score=max(max_score,score)
print(max_score)