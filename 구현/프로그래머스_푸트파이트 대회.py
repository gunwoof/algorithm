def solution(food):
    answer = []
    for i in range(1,len(food)):
        for j in range(food[i]//2):
            answer.append(str(i))
            
    answer.append('0')
    
    rev=answer[-2::-1] # 핵심
    for i in rev:
        answer.append(str(i))
    answer="".join(answer)
    return answer