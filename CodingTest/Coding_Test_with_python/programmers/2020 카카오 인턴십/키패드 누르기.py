# 풀이시간 20분
# 1회차 풀이
# - BFS로 거리를 구할까하다가 키패드가 12개 밖에 없고 매번 알고리즘이 돌아가는 것보다는 그냥 가로, 세로의 차로 거리를 구하는게 편할 것 같아서 패드의 위치를 따로 다 dict을 사용해 기록하였다. 그런 후 손가락을 이동시키며 정답을 기록하고 또 거리에 따라 주어진 조건을 만족시키도록 하였다.

def solution(numbers, hand):
answer = ''
right_hand_pos='#'
left_hand_pos='*'
num_pos=dict()
num_pos[0]=(3,1)
num_pos[1]=(0,0)
num_pos[2]=(0,1)
num_pos[3]=(0,2)
num_pos[4]=(1,0)
num_pos[5]=(1,1)
num_pos[6]=(1,2)
num_pos[7]=(2,0)
num_pos[8]=(2,1)
num_pos[9]=(2,2)
num_pos['*']=(3,0)
num_pos['#']=(3,2)

for num in numbers:
    if num==1 or num==4 or num==7:
        answer+='L'
        left_hand_pos=num
    elif num==3 or num==6 or num==9:
        answer+='R'
        right_hand_pos=num
    else:
        left_to_dist=abs(num_pos[num][0]-num_pos[left_hand_pos][0])+abs(num_pos[num][1]-num_pos[left_hand_pos][1])
        right_to_dist=abs(num_pos[num][0]-num_pos[right_hand_pos][0])+abs(num_pos[num][1]-num_pos[right_hand_pos][1])
        if left_to_dist==right_to_dist:
            if hand=='right':
                answer+='R'
                right_hand_pos=num
            else:
                answer+='L'
                left_hand_pos=num
        elif left_to_dist>right_to_dist:
            answer+='R'
            right_hand_pos=num
        else:
            answer+='L'
            left_hand_pos=num

return answer