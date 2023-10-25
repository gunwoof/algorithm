# Counter로 그리드 하면 됨
# k와 tangerine의 개수가 둘다 1일때만 신경쓰면 됨
from collections import Counter as c
def solution(k, tangerine):
    target=c(tangerine)
    new_target=target.most_common()
    cnt=k
    
    
    for i in range(len(new_target)):
        cnt-=new_target[i][1]
        if cnt < 1:
            return i+1
    
    answer = 0
    return answer