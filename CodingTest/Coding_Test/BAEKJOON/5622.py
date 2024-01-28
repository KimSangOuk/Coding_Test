# 풀이시간 5분 시간제한 1초 메모리제한 128MB
# 1회차 정답
# 각 다이얼의 길이에 각 문자의 주어진 숫자를 더해주면 되는 문제이다.

s=input()

dial=dict()
dial['A']=2
dial['B']=2
dial['C']=2
dial['D']=3
dial['E']=3
dial['F']=3
dial['G']=4
dial['H']=4
dial['I']=4
dial['J']=5
dial['K']=5
dial['L']=5
dial['M']=6
dial['N']=6
dial['O']=6
dial['P']=7
dial['Q']=7
dial['R']=7
dial['S']=7
dial['T']=8
dial['U']=8
dial['V']=8
dial['W']=9
dial['X']=9
dial['Y']=9
dial['Z']=9

result=0
for k in s:
    result+=dial[k]
print(result+len(s))