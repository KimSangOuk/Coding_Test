# - 각 문자열을 입력 받은 후 인덱스로 문자를 찾아 붙여서 출력하면 된다.
# - 풀이시간 : 3분

for tc in range(int(input())):
  s=input()
  print(s[0]+s[-1])