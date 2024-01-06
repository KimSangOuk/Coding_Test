# 풀이시간 4시간
# 1회차 정답 - 하지만 시간이 너무 오래걸려서 다시 풀어보기
# 그리디 알고리즘으로 가까이에 있는 것처럼 접근했었는데 실은, 경로에 따라 최단 루트가 달라질 수 있기 때문에, 또 루트는 따로 따져야하는 문제였다.
# 풀기는 했으나 정답에 도달하는데 시간이 오래걸려서 다시 풀어보기로 하였다.
# 여러군에데서 시간이 오래걸렸는데 하나하나 써보겠다.
# 첫번째, 재귀함수를 구현하는데 시간이 오래걸렸다. 처음에는 전부 'A'가 되었을 때, 조건으로 재귀함수를 빠져나가려고 하다가 하도 안되서 A가 아닌 수를 찾아가는 DFS 방법으로 바꾸어서 풀었더니 금방 완성시킬 수 있었다. 여기서 시간을 많이 잡아먹었다. 왜냐하면 맨 처음 DFS까지 생각이 도달하는데도 오래걸렸기 때문이다. 경로가 가장 가까운 수만을 찾아가는 방법이라고 볼 수 없다는 점을 깨닫는데 오래걸렸다. 여기서 2~3시간이 걸렸다.

def cnt_num(n,num_list):
  count=0
  start=0
  for i in num_list:
      value=abs(i-start)
      if value>n//2:
          value=n-value
      # print(value)
      count+=value
      start=i
  return count

def cnt_alpha(alpha_list):
  count=0
  for a in alpha_list:
      to_alpha=0
      if (ord('Z')-ord('A'))//2<(ord(a)-ord('A')):
          to_alpha=(ord('Z')-ord('A'))-(ord(a)-ord('A'))+1
      else:
          to_alpha=ord(a)-ord('A')
      count+=to_alpha
  return count

def dfs(find_num,find_alpha,i,now):
  global n, array, answer
  if i==n:
      # print(len(array),find_num)
      # print(find_alpha)
      value=cnt_num(len(array),find_num)+cnt_alpha(find_alpha)
      # print(cnt_num(len(array),find_num),cnt_alpha(find_alpha),value)
      answer=min(value,answer)
  else:
      left,right=now,now
      while left>-(len(array)+1) and array[left]=='A':
          left-=1
      while right<len(array) and array[right]=='A':
          right+=1
      # print(left)
      if left!=-(len(array)+1)-1:
          find_num.append(left%len(array))
          find_alpha.append(array[left%len(array)])
          array[left]='A'
          dfs(find_num,find_alpha,i+1,left)
          k=find_num.pop()
          array[left]=find_alpha.pop()
      if right!=len(array):
          find_num.append(right%len(array))
          find_alpha.append(array[right%len(array)])
          array[right]='A'
          dfs(find_num,find_alpha,i+1,right)
          k=find_num.pop()
          array[right]=find_alpha.pop()


def solution(name):
  global n, array, answer
  answer=int(1e9)

  array=list(name)
  n=0
  for i in array:
      if i!='A':
          n+=1
  dfs([],[],0,0)

  return answer