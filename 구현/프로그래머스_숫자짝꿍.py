# 딕셔너리로 개수 모으기
# 개수를 비교하여 적은 것 추출하기
from collections import Counter as C

def solution(X, Y):
    answer = []
    X=list(map(int,list(str(X))))
    Y=list(map(int,list(str(Y))))
    X_dic=C(X)
    Y_dic=C(Y)
    for i in X_dic:
        if i in Y_dic:
            if X_dic[i] <= Y_dic[i]:
                answer.extend([i for _ in range(X_dic[i])])
            else :
                answer.extend([i for _ in range(Y_dic[i])])
    if len(answer) == 0:
        return "-1"
    if len(set(answer))==1 and list(set(answer))[0]==0:
        return "0"
    answer="".join(map(str,sorted(answer,reverse=1)))
            
    
    
    return answer