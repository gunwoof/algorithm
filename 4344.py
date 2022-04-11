allCnt = int(input())
answer=[] # 사람의 수 + 점수들
scores=[] # 각 사람의 점수들
ratioMateriar=[] # 평균보다 큰 점수들


for i in range(allCnt) :
    answer = list(map(int,input().split()))
    number = answer[0]
    scores = answer[1:number+1]
    mean = sum(scores)/number

    for j in range(number) :
        if scores[j] > mean :
            ratioMateriar.append(scores[j])
    print(f"{(len(ratioMateriar)/number)*100:.3f}%")

    ratioMateriar.clear()