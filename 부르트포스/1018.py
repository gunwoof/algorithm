N, M = map(int,input().split())
chess1 = [] # 처음이 W
chess2 = [] # 처음이 B
answerchess=[] # 입력된 체스판
mincnt = 100 # 최소 카운트가 될 값

for i in range(4) :
    chess1.append(list("BWBWBWBW"))
    chess1.append(list("WBWBWBWB"))
        
    chess2.append(list("WBWBWBWB"))
    chess2.append(list("BWBWBWBW"))

for i in range(N) :
    answerchess.append(list(input()))


for n in range(N-7) :
    for m in range(M-7) :
        cnt1 = 0
        cnt2 = 0
        for i in range(8) :
            for j in range(8) :
                if chess1[i][j] != answerchess[n+i][m+j] :
                    cnt1 += 1
                if chess2[i][j] != answerchess[n+i][m+j] :
                    cnt2 += 1
        if mincnt > min(cnt1,cnt2) :
            mincnt = min(cnt1,cnt2)
                    
print(mincnt)

