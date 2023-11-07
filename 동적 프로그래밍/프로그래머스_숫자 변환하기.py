def solution(x, y, n):
    dp=set()
    dp.add(x)
    answer = 0
    while dp:
        if y in dp:
            return answer
        
        dp_add=set()
        for i in dp:
            
            if i+n <=y:
                dp_add.add(i+n)
            if i*2 <=y:
                dp_add.add(i*2)
            if i*3 <=y:
                dp_add.add(i*3)
        
        # 갱신하며 저장(dp의 핵심)
        dp=dp_add
        answer+=1
        
        # 더이상 할게 없으면 -1반환
        if len(dp_add)==0:
            return -1
    
    return answer