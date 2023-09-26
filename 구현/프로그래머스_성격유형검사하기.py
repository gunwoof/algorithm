# choices를 적용할 때에는 '-4'하고 연산
# 성격을 나누지말고 '-'를 활용하여 하나만 계산

def solution(survey, choices):
    
    key=['RT','CF','JM','AN']
    charactor={}
    for i in key:
        charactor[i]=0
        
    for i in range(len(survey)):
        if survey[i] not in key:
            survey[i]=list(survey[i])
            survey[i][0],survey[i][1]=survey[i][1],survey[i][0]
            survey[i]="".join(survey[i])
            charactor[survey[i]]+=(choices[i]-4)
            print(i)
        else :  
            charactor[survey[i]]+=-(choices[i]-4)
    
    answer = []
    for i,j in charactor.items():
        if j >= 0:
            answer.append(i[0])
        else :
            answer.append(i[1])
    answer="".join(answer)
    
    return answer