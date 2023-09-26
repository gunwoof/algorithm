# 각 가로와 세로의 min,max값 파일을 찾음
# 각 min, max파일을 활용하여 격자값 찾음
def solution(wallpaper):
    print(wallpaper)
    
    row=[]
    column=[]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                row.append(i)
                column.append(j)
                
    left=min(row)
    right=max(row)+1
    up=min(column)
    down=max(column)+1
    answer = [left,up,right,down]
    return answer