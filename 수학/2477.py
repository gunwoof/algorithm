from sys import stdin as s

K=int(s.readline())

path_rec=[list(map(int,s.readline().split())) for _ in range(6)]

big_w=0
big_h=0
big_w_idx=0
big_h_idx=0

small_w=0
small_h=0
small_w_idx=0
small_h_idx=0


for i in range(len(path_rec)):
    if path_rec[i][0] == 1 or path_rec[i][0] == 2: 
        if path_rec[i][1] > big_w:
            big_w = path_rec[i][1]
            big_w_idx = i
    else :
        if path_rec[i][1] > big_h:
            big_h = path_rec[i][1]
            big_h_idx = i


# 큰 직사각형의 넓이
big_rec = big_w*big_h


if big_w_idx-big_h_idx == 1 or big_w_idx-big_h_idx == -5:
    small_w_idx = (big_w_idx+2)%6
    small_h_idx = (small_w_idx+1)%6
elif big_h_idx-big_w_idx == 1 or big_h_idx-big_w_idx == -5:
    small_h_idx = (big_h_idx+2)%6
    small_w_idx = (small_h_idx+1)%6

small_rec = path_rec[small_w_idx][1]*path_rec[small_h_idx][1]

rec=big_rec-small_rec
print(K*rec)