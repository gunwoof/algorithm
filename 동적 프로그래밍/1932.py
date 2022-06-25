from sys import stdin as s

n = int(s.readline())
tri_angle_cash=[] # 입력받은 값에 dp를 적용시켜 수정해 나갈 것임
for _ in range(n):
    tri_angle_cash.append(list(map(int,s.readline().split())))


# 핵심 : 자식 노드의 최대값을 찾는 것이 아닌 부모노드의 최대값을 dp(cash)에 저장해야함
for i in range(1,len(tri_angle_cash)):
    for j in range(len(tri_angle_cash[i])):
        if j == 0:
            up_left=0
        else :
            up_left=tri_angle_cash[i-1][j-1]

        if j==len(tri_angle_cash[i])-1:
            up_right=0
        else :
            up_right=tri_angle_cash[i-1][j]

        tri_angle_cash[i][j] += max(up_left,up_right)


print(max(tri_angle_cash[-1]))

