# 풀이시간 40분
# 1회차 정답
# 단순하게 정렬한 다음 앞에서부터 보트에 담아가는 문제인줄 알았으나 꽉꽉 채워서 보트에 넣기 위해서는 맨 끝과 앞에 있는 두 사람을 담아야 최대한 많이 담을 수 있다는 것을 알고 난 다음 각 인덱스를 좁혀가며 풀었다.

def solution(people, limit):
answer = 0

n=len(people)
people.sort()

light=0
heavy=n-1
left=n
while True:
    if light>=heavy:
        answer+=left
        break
    elif light==heavy:
        answer+=1
        break
    if people[light]+people[heavy]<=limit:
        light+=1
        heavy-=1
        answer+=1
        left-=2
        continue
    while light!=heavy and people[light]+people[heavy]>limit:
        heavy-=1

return answer