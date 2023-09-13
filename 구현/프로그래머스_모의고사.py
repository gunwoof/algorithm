# 1. 수포자 리스트 만들기
# 2. 정답 검사
# 3. 등수 나눔(오름차 순이니까 수포자 1부터 검사)

def solution(answers):
    
    # 1. 수포자 리스트 만들기
    a=[1,2,3,4,5]*2000
    b=[2,1,2,3,2,4,2,5]*1250     
    c=[3,3,1,1,2,2,4,4,5,5]*1000
    
    # 2. 정답 검사
    a_cnt=0
    for i in range(len(answers)):
        if answers[i] == a[i]:
            a_cnt = a_cnt + 1
            
    b_cnt=0
    for i in range(len(answers)):
        if answers[i] == b[i]:
            b_cnt = b_cnt + 1
            
    c_cnt=0
    for i in range(len(answers)):
        if answers[i] == c[i]:
            c_cnt = c_cnt + 1
    
    # 3. 등수 나눔(오름차 순이니까 수포자 1부터 검사)
    answer = []
    if max(a_cnt,b_cnt,c_cnt) == a_cnt:
        answer.append(1)
    if max(a_cnt,b_cnt,c_cnt) == b_cnt:
        answer.append(2)
    if max(a_cnt,b_cnt,c_cnt) == c_cnt:
        answer.append(3)
    
    
    return answer