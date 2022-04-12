pn = int(input()) # 사람의 수
hwc = [[],[],[]] # height, weight, count

for i in range(pn) :
    h,w = map(int,input().split())
    hwc[0].append(h)
    hwc[1].append(w)
    hwc[2].append(1)

for i in range(pn) : 
    for j in range(i+1,pn) :
        if hwc[0][i] < hwc[0][j] and hwc[1][i] < hwc[1][j]:
            hwc[2][i] += 1

for i in range(pn-1,-1,-1) :
     for j in range(i-1,-1,-1) :
        if hwc[0][i] < hwc[0][j] and hwc[1][i] < hwc[1][j]:
            hwc[2][i] += 1
   
for i in range(pn) :
    print(hwc[2][i],end=" ")


# 처음에 작성한 쓰래기 코드(안 돌아감)
# 처음에 "등수"라는 단어에 꽃혀 정렬이라고 생각했는데,  "k명이라면 그 사람의 덩치 등수는 k+1"을 보고 완전탐색 count새는 것 이었다!
'''np = int(input()) # 숫자의 개수
height = []
weight = []
score = []
maintain = 0

for i in range(np) :
    h,w = map(int,input().split())
    height.append(h)
    weight.append(w)

height1 = height
weight1 = weight

for i in range(np) :   
    for j in range(np-i-1) :
        if height[j]<height[j+1] and weight[j]<weight[j+1] :
            height[j],height[j+1] = height[j+1],height[j]
            weight[j],weight[j+1] = weight[j+1],weight[j]

for i in range(np-1):
    if height[i]<height[i+1] and weight[i]<weight[i+1] :
        score[i] = i+1
        maintain = 0
    elif (height[i]<height[i+1] and weight[i]>weight[i+1]) or (height[i]>height[i+1] and weight[i]<weight[i+1]) :    
        if maintain == 0:
            maintain = i+1
        score[i] = maintain

print(height,weight,score)'''


        
