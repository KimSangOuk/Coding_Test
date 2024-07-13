from itertools import permutations
from collections import deque
import copy

def solution(expression):
    answer = 0

    oper=['+','-','*']

    oper_prior=list(permutations(oper,3))

    exp_list=list(expression)
    num_str=''
    exp_main=[]
    for i in exp_list:
        if i not in oper:
            num_str+=i
        else:
            exp_main.append(num_str)
            exp_main.append(i)
            num_str=''
    if num_str!='':
        exp_main.append(num_str)
    max_value=0
    for prior in oper_prior:
        exp=copy.deepcopy(exp_main)
        for op in prior:
            new_arr=[]
            k=0
            while k<len(exp):
                if exp[k] == op:
                    mid=eval(new_arr[-1]+exp[k]+exp[k+1])
                    new_arr[-1]=str(mid)
                    k+=2
                else:
                    new_arr.append(exp[k])
                    k+=1
            exp=new_arr
        max_value=max(max_value,abs(int(exp[0])))
    answer=max_value

    return answer