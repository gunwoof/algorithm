# 1. park를 list로 만들기
# 2. start 지점 찾기
# 3. routes의 문자열을 list로 만들기
# 4. 칸 옮기기(장애물, 경계 조건)

def solution(park, routes):
    
    # 1. park를 list로 만들기
    new_park=[]
    for i in park:
        new_park.append(list(i))
    
    # 2. start 지점 찾기
    start=[]
    for i in range(len(new_park)):
        for j in range(len(new_park[i])):
            if new_park[i][j] == 'S':
                start.append(i)
                start.append(j)
    
    # 3. routes의 문자열을 list로 만들기
    new_routes=[]
    for i in range(len(routes)):
        x,y = routes[i].split()
        y = int(y)
        new_routes.append([x,y])
    
    # 4. 칸 옮기기(장애물, 경계 조건)
    for route in new_routes:
        if route[0] == "N":
            start=North(new_park,start,route[1])
        if route[0] == "S":
            start=South(new_park,start,route[1])
        if route[0] == "W":
            start=West(new_park,start,route[1])
        if route[0] == "E":
            start=East(new_park,start,route[1])
        
    answer = start
    return answer

def North(new_park,start,cnt):
    coordinate=list(start) # 깊은 복사 해야함
    if -1 < coordinate[0] - cnt : # 경계
        for i in range(cnt): # '장애물'
            if new_park[coordinate[0] - 1][coordinate[1]] != 'X':
                coordinate[0] = coordinate[0] - 1
            else : 
                return start
    else :
        return start
    
    return coordinate
        
            
def South(new_park,start,cnt):
    coordinate=list(start)
    if coordinate[0] + cnt < len(new_park):
        for i in range(cnt):
            if new_park[coordinate[0] + 1][coordinate[1]] != 'X':
                coordinate[0] = coordinate[0] + 1
            else : 
                
                return start
    else :
        return start
    
    return coordinate
            
def West(new_park,start,cnt):
    coordinate=list(start)
    if -1 < coordinate[1] - cnt:
        for i in range(cnt):
            if new_park[coordinate[0]][coordinate[1] - 1] != 'X':
                coordinate[1] = coordinate[1] - 1
            else : 
                return start
    else :
        return start
    
    return coordinate
            
def East(new_park,start,cnt):
    coordinate=list(start)
    if coordinate[1] + cnt < len(new_park[0]):
        for i in range(cnt):
            if new_park[coordinate[0]][coordinate[1] + 1] != 'X':
                coordinate[1] = coordinate[1] + 1
            else : 
                return start
    else :
        return start
    
    return coordinate
