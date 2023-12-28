# 이것이 취업을 위한 코딩테스트다 part03 '09. 문자열 압축'과 동일

def solution(s):
  s_len=len(s)
  answer=s_len
  
  for i in range(1,s_len//2+1):
    cut_line=i
  
    whole_len=0
  
    same=1
    for j in range(0,s_len-cut_line,cut_line):
      if s[j:j+cut_line]==s[j+cut_line:j+2*cut_line]:
        same+=1
      else:
        if same!=1:
          whole_len+=cut_line+len(str(same))
        else:
          whole_len+=cut_line
        same=1
    if same!=1:
      whole_len+=cut_line+len(str(same))
    else:
      whole_len+=s_len-(j+cut_line)
    answer=min(whole_len,answer)
  
  return answer