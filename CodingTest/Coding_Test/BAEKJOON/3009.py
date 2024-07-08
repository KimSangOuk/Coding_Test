x_cnt=dict()
y_cnt=dict()
for _ in range(3):
    x,y=map(int,input().split())
    if x not in x_cnt:
        x_cnt[x]=1
    else:
        x_cnt[x]+=1
    if y not in y_cnt:
        y_cnt[y]=1
    else:
        y_cnt[y]+=1
answer_x=0
answer_y=0
for k in x_cnt.keys():
    if x_cnt[k]==1:
        answer_x=k
for k in y_cnt.keys():
    if y_cnt[k]==1:
        answer_y=k
print(answer_x,answer_y)