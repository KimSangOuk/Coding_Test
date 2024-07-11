from collections import deque

def solution(m, musicinfos):
    answer = ''
    answer_list=[]
    num=0
    for music in musicinfos:
        num+=1
        start_t,end_t,title,melody=map(str,music.split(","))
        play_time=(int(end_t[0:2])-int(start_t[0:2]))*60+(int(end_t[3:5])-int(start_t[3:5]))
        q=deque(list(melody))
        melody_list=[]
        index=0
        while(q):
            now=q.popleft()
            if now!='#':
                melody_list.append(now)
                index+=1
            else:
                melody_list[index-1]+=now
        mq=deque(list(m))
        index_m=0
        m_list=[]
        while(mq):
            now=mq.popleft()
            if now!='#':
                m_list.append(now)
                index_m+=1
            else:
                m_list[index_m-1]+=now

        realtime_melody=[]
        for i in range(play_time):
            realtime_melody.append(melody_list[i%len(melody_list)])
        for i in range(len(realtime_melody)):
            include_tf=True
            for j in range(len(m_list)):
                if i+j>=len(realtime_melody) or realtime_melody[i+j]!=m_list[j]:
                    include_tf=False
                    break
            if include_tf:
                answer_list.append((play_time,num,title))
                break
    if len(answer_list)==0:
        answer="(None)"
        return answer
    answer_list.sort(key=lambda x:(-x[0],x[1]))
    answer=answer_list[0][2]

    return answer