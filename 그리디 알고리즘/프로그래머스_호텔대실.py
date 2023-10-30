# 시작시간으로 정렬
# ':'을 없애고 4자리 자연수로 변환
# 사이 시간 10분 고려
# 초가 0~60 넘어가는 경우 처리
def solution(book_time):
    book_time.sort()
    for i in range(len(book_time)):
        for j in range(len(book_time[i])):
            book_time[i][j]=book_time[i][j].replace(':','')
            book_time[i][j]=int(book_time[i][j])
    
    room=[]
    for i in range(len(book_time)):
        # room을 추가해야 하는 경우 1로 변경
        check=0
        # 초 부분에 10을 뺐을때 0보다 작은경우 분에서 1뺀다
        ten_ready=book_time[i][0]-10
        if (book_time[i][0])%100-10< 0:
            ten_ready=book_time[i][0]-50
        
        # room의 시간 모두 비교
        for j in range(len(room)):
            
            if ten_ready>=room[j][1]:
                
                room[j][1]=book_time[i][1]
                check=1
                break
        # check == 0이면 room을 추가해야 한다
        if check == 0:
            room.append(book_time[i])
        
    
    answer = len(room)
    return answer