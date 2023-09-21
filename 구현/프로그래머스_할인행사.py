# want,number로 딕셔너리 만들기(zip 사용)
# discount의 각각 원소의 개수를 체크(set()사용하여 unique뽑기) or 모듈사용
# 비교

def solution(want, number, discount):
    
    # want,number로 딕셔너리 만들기(zip 사용)
    favorite={}
    for i, j in zip(want,number):
        favorite[i]=j
    
    
    cnt=0
    for i in range(len(discount)-9):
        
        # discount의 각각 원소의 개수를 체크(set()사용하여 unique뽑기)
        market={}
        for j in set(discount[i:i+10]):
            market[j]=discount[i:i+10].count(j)
            
        # 비교
        if favorite==market:
            cnt+=1
    answer = cnt
    return answer