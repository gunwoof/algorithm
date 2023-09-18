# 딕셔너리에 브루트포스로 숫자 넣기(조건: 작은 것을 넣기)


def solution(keymap, targets):
    
    # 딕셔너리에 브루트포스로 숫자 넣기
    alpha={} # 딕셔너리는 enumerate를 꼭 생각하자
    for st in keymap:
        for i,key in enumerate(st): # enumerate (index, key)반환
            if key not in alpha.keys():
                alpha[key]=i+1
            else :
                if alpha[key] > i+1:
                    alpha[key] = i+1
    
    
    answer=[]
    for st in targets:
        cnt, error=0,0
        for key in st:
            if key in alpha.keys():
                cnt+=alpha[key]
            else : 
                error = 1
                break
            
        if error !=1:
            answer.append(cnt)
        else :
            answer.append(-1)
            
                
        
            
    return answer