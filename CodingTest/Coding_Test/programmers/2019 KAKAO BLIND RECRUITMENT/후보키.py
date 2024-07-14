from itertools import combinations

def solution(relation):
    answer = 0

    c=len(relation[0])
    r=len(relation)
    uniqueCase=set()

    for j in range(1,c+1):
        cases=list(combinations(range(c),j))
        for case in cases:
            keys=set()
            for i in range(r):
                oneKey=[]
                for k in case:
                    oneKey.append(relation[i][k])
                keys.add(tuple(oneKey))
            if len(list(keys))==r:
                minimality=True
                for uc in list(uniqueCase):
                    all_include=True
                    for k in uc:
                        if k not in case:
                            all_include=False
                            break
                    if all_include:
                        minimality=False
                        break
                if minimality:
                    uniqueCase.add(tuple(case))
                    answer+=1

    return answer