# - 무슨 SQL문 써서 풀거 같은 문제를...
# - 각 차량에 대한 기록을 정리해야하기 때문에 각 차량에 대해서 스택식으로 정리할 딕셔너리 하나랑 전체 구할 시간을 정리해둘 딕셔너리를 하나 두었다. 결국, 전체 기록을 조회하면서 한번 더 나오면 시간의 차를 구해서 total 딕셔너리에 더하고 마지막에 남은 기록, 즉 23:59에 처리될 기록또한 한번 더 전체적으로 순회해서 처리해주었다.
# - 시간을 구한 이후에는 단순히 시간에 따른 요금 계산 문제이다. 각 기록을 요금에 맞게 계산해주고 그 기록을 다시한번 정렬해서 답에 넣어주면 된다.
# - 풀이시간 : 25분

import math

def solution(fees, records):
    answer = []
    default_minute,default_fee,unit_time,unit_fee=fees[0],fees[1],fees[2],fees[3]
    total_record=dict()
    left_record=dict()
    for r in records:
        t,n,s=r.split()
        if n not in total_record:
            total_record[n]=0
            left_record[n]=t
        else:
            if left_record[n]!='':
                total_record[n]+=(int(t[0:2])*60+int(t[3:5]))-(int(left_record[n][0:2])*60+int(left_record[n][3:5]))
                left_record[n]=''
            else:
                left_record[n]=t
    for key in left_record:
        if left_record[key]!='':
            total_record[key]+=(23*60+59)-(int(left_record[key][0:2])*60+int(left_record[key][3:5]))
    prev_answer=[]
    for key in total_record:
        used_t=total_record[key]
        if used_t<=default_minute:
            prev_answer.append((key,default_fee))
        else:
            prev_answer.append((key,default_fee+math.ceil((used_t-default_minute)/unit_time)*unit_fee))
    prev_answer.sort()
    for i in range(len(prev_answer)):
        answer.append(prev_answer[i][1])
    return answer 