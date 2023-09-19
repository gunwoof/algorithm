# in 사용
# 알파벳 26개
# 1. 알파벳 뭉치 만들기(skip을 제외하면서+아스키코드 사용)
# 2. 비교

def solution(s, skip, index):
    
    # 알파벳 뭉치 만들기
    alpha=[]
    for i in range(26):
        if chr(i+97) not in list(skip):
            alpha.append(chr(i+97)) # 아스키코드
    
    # 비교
    s=list(s) 
    for i in range(len(s)):
        for j in range(len(alpha)):
            if s[i] == alpha[j]: 
                idx=(j+index)%len(alpha) # 수 넘어가면 다시 돌아오는 것을 나머지로 처리
                s[i]=alpha[idx] # str은 변수[idx]=값 형태로 못 넣음
                break
    
    answer = "".join(s)
    return answer