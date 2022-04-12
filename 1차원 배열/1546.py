number = int(input())
score = list(map(int,input().split()))
newScore = []

for i in range(number) :
    newScore.append(score[i]/max(score)*100)

newMean = sum(newScore)/number

print(newMean)
