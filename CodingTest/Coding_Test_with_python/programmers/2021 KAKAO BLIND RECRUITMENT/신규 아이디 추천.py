# 풀이시간 30분
# 1회차 정답
# 문자열을 다루는 문제 유형이라고 읽으면서 생각이 들었다. 파이썬에는 문자열을 다루는 기본 라이브러리 함수를 많이 제공해서 쉽게 접근했다. lower()로 소문자로 전부 바꾸고 길이를 다루는 경우는 배열의 슬라이싱을 통해 처리했다.
# '.'이 연속된 경우를 처리하는 것이 살짝 까다롭다고 생각했는데 '.'가 연속된 숫자가 전부 달라서 replace()한번만으로 안된다고 생각하고 반복문으로 그 수를 전부 하나인 경우로 치환했다.

def solution(new_id):
  answer = ''
  
  new=''
  new_id=new_id.lower()
  for i in new_id:
      if i.isalnum() or i=='-' or i.isalpha() or i=='_' or i=='.':
          new+=i
  
  end_stack=0
  stack=0
  for i in range(len(new)):
      if new[i]=='.':
          stack+=1
      else:
          end_stack=max(stack,end_stack)
          stack=0
  end_stack=max(stack,end_stack)
  
  
  
  for i in range(end_stack,1,-1):
      new=new.replace('.'*i,'.')
  
  if len(new)!=0 and new[0]=='.':
      new=new[1:]
  
  if len(new)!=0 and new[len(new)-1]=='.':
      new=new[:len(new)-1]
  
  if len(new)==0:
      new='a'
  if len(new)>=16:
      new=new[:15]
      if new[len(new)-1]=='.':
          new=new[:len(new)-1]
  if len(new)<=2:
      while len(new)<3:
          new+=new[len(new)-1]
  
  return new