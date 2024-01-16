# 풀이시간 30분 시간제한 1초 메모리제한 128MB
# 3회차 정답
# 입력된 문자열을 압에서부터 끊는 단위별로 탐색하여 압축시켜가는 전체 탐색하는 브루트포스 알고리즘 유형이다. 지금 같은 경우, 앞에서부터 전부 끊어서 풀었지만 prev를 두고 앞에 시작점을 다르게 한다면 더 코드를 간단화 할 수 있기도 하고 연습도 하는 겸 다시 풀어보기로 하였다.

def solution(s):
  answer = len(s)

  length=len(s)

  for unit in range(1,length//2+1):
    compress_s=""
    count=1
    for i in range(0,length-1,unit):
      if s[i:i+unit]==s[i+unit:i+2*unit]:
        count+=1
      else:
        compress_s+=str(count)+s[i:i+unit] if count>1 else s[i:i+unit]
        count=1
    if s[i:i+unit]==s[i+unit:i+2*unit]:
      compress_s+=str(count)+s[i:i+unit]
    else:
      compress_s+=s[i+unit:i+2*unit]
    answer=min(answer,len(compress_s))
  
  return answer

print(solution("aaaaa"))
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("a"))


























# 2회차 풀이
# 1시간만에 답을 보고 풀어내고 틀린 부분을 이해할 정도로 실력이 늘긴하였다. 하지만 몇가지 마음에 안드는 부분은 여전히 존재했다.
# 첫번째는 시간이 너무 오래걸린 부분, 바로 인덱스를 처리할 부분인 것이다. 어기서 시간을 썼냐면, 바로 마지막에 남은 부분을 처리하는 것이였는데, 이때, 인덱스 계산이 되지 않아서, 오래 걸렸다. 그래서 답지와 저번에 어떻게 풀었나를 보았더니 남은 부분의 인덱스를 처리안해도 따로 슬라이싱을 사용하면 끝까지만 반환하고 오류가 따로 뜨지 않았다. 이 부분에 대한 지식의 부족 때문에 일일이 인덱스를 계산해보고 경우를 따져보느라고 오래걸렸다. 이부분은 지식의 부족이었기에 고쳐나가면 된다.
# 두 번째는 표현방법의 문제였다. 저번에도 이부분은 지적한 적이 있는데 습관이 되지 못해서 그런가 고쳐지지 않았다. 그래서 한번 더 적기로 하였다. 일정 조건하에 같은 모양이 생기면 한문장으로 줄일 수 있다는 점이다. 이러한 부분이 보이면 더 짧게 쓰려고 노력해야 한다.
# 마지막 세번째는, 답에 관련된 부분이다. 숫자의 길이가 문장으로 따졌을 때, 한개 이상일 수 있다는 점을 고려해야된다는 것이다. 이부분은 종종 등장할 수 있지만 무조건 한글자라고 문자열 처리할 때 하는 관념이 있다고 생각해서 확실히 하기 위해 적어놓았다.
# 밑에 풀이는 그래도 답을 출력하고 있다. 저번보다는 성장했다는 것을 알 수 있다.

# def solution(s):
#   s_len=len(s)
#   answer=s_len

#   for i in range(1,s_len//2+1):
#     cut_line=i

#     whole_len=0

#     same=1
#     for j in range(0,s_len-cut_line,cut_line):
#       if s[j:j+cut_line]==s[j+cut_line:j+2*cut_line]:
#         same+=1
#       else:
#         if same!=1:
#           whole_len+=cut_line+len(str(same))
#         else:
#           whole_len+=cut_line
#         same=1
#     if same!=1:
#       whole_len+=cut_line+len(str(same))
#     else:
#       whole_len+=s_len-(j+cut_line)
#     answer=min(whole_len,answer)
  
#   return answer

# 풀이 시간 - 1시간 30분/30분 시간제한 1초 메모리제한 128MB
# 1회차 오답 - 예외케이스를 찾지못함
# 먼저 s의 길이가 1000이하인거를 알고 O(N^2)을 생각하게 되었는데 길이를 1에서부터 중간정도까지 단위로 나누어서 돌려야된다고 생각하니 그 안에 끊은 단위를 돌리면서 갯수를 파악해야된다고 생각하니 이중 포문이 딱맞아떨어졌다. 여기까지는 괜찮음.

# # 1회차 풀이
# # 생각한대로 이중 포문으로 돌린다음 이전것이 생긴다는 괜찮았음. 여기서 두가지로 나누어서 생각하게 됨. 그냥 글자 수만 구하는 방법이랑 전체적인 답을 구한다음에 그 글자수를 따로 세는 방법이랑 나누어졌는데 첫번재 방법은 애초에 엄청나게 많이 틀림. 여기까지 30분을 써버림. 그래서 다시 구현하니까 또 30분 정도 걸림. 이유는 찾지 못함. 다 맞춰보니 틀린 경우가 한가지 존재하게 됨. 글자수가 하나일 경우임. 그래서 강제적으로 맞춰버림. 이건 그냥 틀린거나 마찬가지라고 봄.
# def solution(s):
#   answer=100000000000 # 여기서 아무생각없이 큰수를 넣어놓는게 아니라 될 수 있는 최대의 수를 넣어놓는 것이 이론적으로나 논리적으로나 합리적이라고 봄.
  
#   for i in range(1,len(s)//2+2): # 여기서도 +2를 해놓았는데 이건 글자수가 1인 경우를 강제적으로 맞출려고 하다보니 이렇게 되버림.
#     arr=[]
#     j=0
#     while len(s)>j:  # 이거까지도 나쁘지 않았다고 봄. 끊어서 쓰나 하면서 끊으나 비슷했다고 생각함. 하지만 더 나아가서 코드를 줄이려면 이걸 어차피 for문으로 돌려야되고 끊는 단위별로 우리는 바로 갖다 쓸 생각이니 굳이 나누어놓을 필요가 없다는 것까지 캐치해서 줄여야함.
#       arr.append(s[j:j+i])
#       j=j+i

#     count=0
#     answer_s=""
#     previous=arr[0]
#     for k in arr: # 단위별로 끊는게 슬라이싱이나 range를 점프식으로 하는게 익숙하지 않으니 방법을 찾지 못하고 결국 이렇게 씀
#       if k==previous:
#         count+=1
#       else: # 이렇게 비슷하게 생긴 경우 한문장으로 줄여서 쓸 수 있다는 것 또한 한가지 배움. 실전에서는 줄일 수 있는 곳은 최대한 다 줄여야 코드 구현도 간단해지고 시간도 벌 수 있음.
#         if count==1:
#           answer_s+=previous
#         else:
#           answer_s+=str(count)+previous
#         count=1
#       previous=k

#     # 여기도 마찬가지로 한줄로 줄일 수 있는 부분. 그리고 for문으로 나눠서 썼으면 이부분을 돌려봐서 찾는게 아니라 한번에 남는 부분이 생길 수도 있겠구나 하고 캐치가능한 부분이었음.
#     if count==1:
#       answer_s+=previous
#     else:
#       answer_s+=str(count)+previous

#     answer=min(len(answer_s),answer)
  
#   return answer

# 결국 밑에 처럼 돌려가면서 찾는 버릇을 없애야 함. 이게 시간도 다 잡아먹으면서 찾기도 쉽지 않음. 애초에 확실히 코드를 짤 계획을 세우고 다 짠다음에 머리로 돌려보고 그래도 안되면 돌려야됨.

# print(solution("aaaaa"))
# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
# print(solution("a"))

# # 답안지
# def solution(s):
#   answer=len(s)
#   # 1개 단위(step)부터 압축 단위를 늘려가며 확인
#   for step in range(1,len(s)//2+1):
#     compressed=""
#     prev=s[0:step] # 앞에서부터 step만큼의 문자열 추출
#     count=1
#     # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
#     for j in range(step,len(s),step):
#       # 이전 상태와 동일하다면 압축 횟수(count) 증가
#       if prev==s[j:j+step]:
#         count+=1
#       # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
#       else:
#         compressed+=str(count)+prev if count >= 2 else prev
#         prev = s[j:j+step] # 다시 상태 초기화
#         count = 1
#     # 남아 있는 문자열에 대해서 처리
#     compressed += str(count) + prev if count >= 2 else prev
#     # 만들어지는 압축 문자열이 가장 짧은 것이 정답
#     answer=min(answer,len(compressed))
#   return answer