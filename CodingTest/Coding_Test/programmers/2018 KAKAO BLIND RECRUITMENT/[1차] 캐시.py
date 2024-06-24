# 캐시 알고리즘은 빠르게 데이터를 처리하기 위해 캐시에서의 데이터 이동을 다루는 알고리즘이다.
# 이 중에서 LRU(Least Recently Used) 알고리즘은 '페이지 전환 알고르즘' 중 하나이다. 프로세스에서 한 페이지를 새로 적재하려고 할 때, 현재 사용되고 있는 캐시에 내재된 페이지들 중 가장 오래 사용되지 않은 페이지를 새로운 페이지로 교체하는 알고리즘이다.
# 즉, [ A, B, C ] 라는 형태의 cache의 크기가 3일 때, 새롭게 찾고자 하는 페이지가 해당 캐시에 이미 들어 있으면 cache hit, 아니면 cache miss가 발생하는데 hit의 경우에는 가장 최근에 사용되었기 때문에 업데이트 해주어서 A가 사용되었다 했을 경우, [ B, C, A ]로 업데이트 해준다. miss의 경우에는 들어 있지 않기 때문에 새로운 페이지가 'F'라고 했을 경우, [ B, C, F ]로 업데이트 해주면 된다.
# 생각
# 캐시 관련된 알고리즘은 처음 접하였기 때문에 찾는데 시간이 좀 걸렸다. 문제에서 상세 예시를 주지 않았기 때문에 처음부터 학습을 요구하고 접근하길 바랬던 문제였던 거 같다.
# 파이썬으로 간단히 구현하는 거 자체는 어렵지 않았다. 리스트를 두고 miss의 경우와 hit의 경우만 나누어서 시간을 추가해 주면서 리스트를 업데이트 해주면 되었다.
# 추가적으로 대소문자의 구분이 없기 때문에 한쪽으로 변경해주면 된다. 나의 경우는 lower()를 써서 소문자로 변환해주었다.
# 풀이시간 : 25분
# 1회차 정답

from collections import deque

def solution(cacheSize, cities):
    answer = 0

    q=deque()

    for city in cities:
        city=city.lower()
        if city in q:
            answer+=1
            q.remove(city)
            q.append(city)
        else:
            answer+=5
            if len(q)>=cacheSize:
                if len(q)!=0:
                    q.popleft()
                if cacheSize!=0:
                    q.append(city)
            else:
                q.append(city)


    return answer