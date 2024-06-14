# - 0.5초 이내에 즉 대략 10,000,000회 연산 내에 풀기 위해서는 최대 숫자가 10,000,000이기 때문에 반복문을 한번 만 써서 구하면 된다고 생각했다. 여기서 for문으로 일일이 찾을까 하다가 규칙성을 이용하기로 하였다.
# - while 문을 통해서 전체 늘어나는 횟수를 구하여 대각선 줄 내에서의 몇번째인지를 구한다. 이때, 각 증가폭이 1씩 늘어나는 점을 이용하면 된다. 또한 대각선이 짝수번째인지 홀수번째인지에 따라 시작점의 위치가 변화하므로 이 것을 tf로 두어 구분하였다. 마지막으로는 증가하는 폭, k+1이 각 분모와 분자의 합이 되어 그 수에서 cnt를 빼어 분자나 분모를 구하였다.
# - 풀이시간 : 20분

n=int(input())

tf=True
k=1
total=0
prev_total=0
while True:
    total+=k
    if total>=n:
        cnt=n-prev_total
        if tf:
            # print("total:",k+1,"answer:",k+1-cnt,"/",cnt)
            print(str(k+1-cnt)+"/"+str(cnt))
        else:
            # print("total:",k+1,"answer:",cnt,"/",k+1-cnt)
            print(str(cnt)+"/"+str(k+1-cnt))
        break
    tf=not(tf)
    prev_total=total
    k+=1