from collections import deque
import heapq

for tc in range(1,int(input())+1):
    answer=0
    N,M,K,A,B=map(int,input().split())
    clientLog=dict()
    receptionDeskT=[0]+list(map(int,input().split()))
    receptionDeskLog=[]
    for i in range(1,N+1):
        heapq.heappush(receptionDeskLog,(0,i))
    maintenanceWindowT=[0]+list(map(int,input().split()))
    maintenanceWindowLog=[]
    for i in range(1,M+1):
        heapq.heappush(maintenanceWindowLog,(0,i))
    timeList=[0]+list(map(int,input().split()))
    visitTime=[]
    for i in range(1,K+1):
        visitTime.append((i,timeList[i]))
        clientLog[i]=dict()
    visitTime.sort(key=lambda x:x[1])
    visitTimeQ=deque(visitTime)
    inputClient=[]
    inputClient2=[]
    receptionDeskChoice=[]
    maintenanceWindowChoice=[]
    waitClient=[]
    t=0
    endClient=[]
    endClientNum=0
    while True:
        # 접수 창구에 들어갈 고객 선정
        while len(visitTimeQ)>0 and visitTimeQ[0][1]==t:
            now=visitTimeQ.popleft()
            heapq.heappush(inputClient,now)
        # 투입할 접수 창구 선정
        while len(receptionDeskLog)>0 and receptionDeskLog[0][0]<=t:
            now=heapq.heappop(receptionDeskLog)
            heapq.heappush(receptionDeskChoice,now[1])
        # 접수 창구에 고객 투입
        while len(receptionDeskChoice)>0 and len(inputClient)>0:
            client=heapq.heappop(inputClient)
            desk=heapq.heappop(receptionDeskChoice)
            heapq.heappush(receptionDeskLog,(t+receptionDeskT[desk],desk))
            heapq.heappush(waitClient,(t+receptionDeskT[desk],desk,client[0]))
            clientLog[client[0]]=[desk]

        # 투입할 정비 창구 선정
        while len(maintenanceWindowLog)>0 and maintenanceWindowLog[0][0]<=t:
            now=heapq.heappop(maintenanceWindowLog)
            heapq.heappush(maintenanceWindowChoice,now[1])

        # 정비 창구에 고객 투입
        while len(maintenanceWindowChoice)>0 and len(waitClient)>0 and waitClient[0][0]<=t:
            client=heapq.heappop(waitClient)
            desk=heapq.heappop(maintenanceWindowChoice)
            heapq.heappush(maintenanceWindowLog,(t+maintenanceWindowT[desk],desk))
            clientLog[client[2]].append(desk)
            endClientNum+=1

        # 완료된 사람이 K명이면 종료
        if endClientNum==K:
            break
        t+=1
    for key in clientLog.keys():
        if clientLog[key]==[A,B]:
            answer+=key
    if answer==0:
        print("#"+str(tc)+" "+str(-1))
    else:
        print("#"+str(tc)+" "+str(answer))
