# 풀이시간 2시간/60분 시간제한 0.5초 메모리제한 512MB
# 1회차 정답 - but, 풀이시간 오래 걸림
# 주어진 조건대로 2차원 배열을 다루는 시뮬레이션 문제이다. 최대한 시간을 줄여보고자 처음에는 인덱스를 제한하면서 배열 또한 최소한의 크기로 풀려고 하다가 너무 인덱스가 복잡해지기도 하고 조건이 까다로워져서 100*100으로 만들어놓고 풀었다.
# 2차원 배열에서 모든 행과 열을 조건에 따라 추출하고 추출한 것을 정렬한 후에 다시 배열에 넣으면 되는 문제이다. 이 때, 우리는 조건에 따라 행인지 열인지를 결정해야 하므로 각 최대 길이를 정렬을 시작하기 전에 초기화 해놓고 다시 구해야 한다.
# 시간은 인덱스를 다루는 부분에서 오래걸렸는데 처음부터 100*100으로 했으면 더 쉬워졌을 거라는 생각이 들었다. 이때, 처음에 시간복잡도를 가장 쉬운 방법으로 잡고 계산해보고 가능하다면 쉬운 방법으로 하는 것이 좋다는 생각이 들었다. 즉, 최대한 범위를 늘려서 쉬운 방법으로 해보고 안되면 좁히는 식으로 해야겠다.

import sys
input=sys.stdin.readline

r,c,k=map(int,input().split())

a=[[0]*(101) for _ in range(101)]
for i in range(1,4):
    arr=list(map(int,input().split()))
    for j in range(1,4):
        a[i][j]=arr[j-1]

max_r_len=3
max_c_len=3

# 정렬과 최대 길이 업데이트
def rc_sort(array,rc):
    global max_r_len,max_c_len
    count=[0]*101
    # print(len(array))
    for i in range(1,101):

        count[array[i]]+=1
    num_cnt_arr=[]
    for i in range(1,101):
        if count[i]>0:
            num_cnt_arr.append((i,count[i]))
    num_cnt_arr.sort(key=lambda x:(x[1],x[0]))
    result_arr=[]
    for num,cnt in num_cnt_arr:
        result_arr.append(num)
        result_arr.append(cnt)
    if rc=='r':
        max_c_len=max(max_c_len,len(result_arr))
    else:
        max_r_len=max(max_r_len,len(result_arr))
    return [0]+result_arr+[0]*(100-len(result_arr))

t=0
while t<100:
    # A[r][c]에 들어가는 값이 k이면 종료
    if a[r][c]==k:
        break
    t+=1
    # 모든 행을 정렬
    if max_r_len>=max_c_len:
        max_c_len=0
        # 행을 추출
        for i in range(1,101):
            tmp=[]
            for j in range(0,101): # 이번 행의 숫자 추출
                tmp.append(a[i][j])
            tmp=rc_sort(tmp,"r") # 정렬
            for j in range(0,101): # 정렬한 행 다시 투입
                a[i][j]=tmp[j]

    # 모든 열을 정렬
    else:
        max_r_len=0
        for j in range(1,101):
            tmp=[]
            for i in range(0,101): # 이번 행의 숫자 추출
                tmp.append(a[i][j])
            tmp=rc_sort(tmp,"c") # 정렬
            for i in range(0,101): # 정렬한 행 다시 투입
                a[i][j]=tmp[i]

    # print(max_r_len,max_c_len)
    # for i in range(1,max_r_len+1):
    #     for j in range(1,max_c_len+1):
    #         print(a[i][j],end=' ')
    #     print()
    # print()

# 100초가 지나도 A[r][c]가 안되어서 -1
if a[r][c]!=k:
    print(-1)
# 최소 시간 출력
else:
    print(t)