# - (게임의 한바퀴=인원수)*(내가 필요한 숫자의 갯수) 만큼 숫자를 각 진수를 변환한 다음 이어붙여 각 턴과 순서에 맞게 필요한 숫자를 이어붙여 출력하면 된다. 이 때, 각 숫자를 나머지 값과 나머지를 이용해서 진수로 변환해주면 된다. 나는 마땅히 알파벳 변환할 방법이 안떠올라서 간단하게 dict에 각 숫자를 넣은 다음 수행하였다.
# - 풀이시간 : 40분

def to_10_n(num,n):
  dict_num={ 0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
  answer=''
  while num>0:
      d=num%n
      num=num//n
      answer+=dict_num[d]
  return answer[::-1]

def solution(n, t, m, p):
  answer = ''
  total_s='0'
  for i in range(1,t*m):
      total_s+=to_10_n(i,n)
  for k in range(t):
      answer+=total_s[(p-1)+m*k]
  return answer