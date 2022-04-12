number = int(input())
num= [number//10,number%10] 

cnt = 0

while 1 :
    if cnt == 0 :
        orinum = num

    answer = [num[0]+num[1]]
    answer = [answer[0]//10,answer[0]%10]

    newnum = [num[1],answer[1]]
    cnt += 1

    if orinum == newnum :
        break
    else : 
        num = newnum

print(cnt)



# 처음 만든 쓰레기 코드(결국 안돌아감)
'''question = list(input()) # 숫자 한 자리씩 한 방에 넣어 둠
answer = []
oriQuestion = [] # 첫 숫자
newQuestion =[] # 새로운 수(두자리 숫자를 쪼개서 방에 한 자리씩 넣음)
cnt =0

while 1 :
    if len(question) == 1:
        question.append(int(question[0]))
        question[0] = 0
    else : # 이곳이 문제
        question =  list(map(int,question))
        print(question,type(question[1]))
        
    if cnt == 0 :
        oriQuestion = question # 첫 숫자 저장
    

    answer.append(sum(question))
    if len(answer) == 1:
        answer.append(int(answer[0]))
        answer[0] =0
    else :
        answer = [answer[0]//10,answer[0]%10]
    print(answer)

    newQuestion.append(question[1]+answer[1])
    newQuestion = [newQuestion[0]//10,newQuestion[0]%10]
    print(newQuestion)
    cnt += 1

    if newQuestion == oriQuestion: # 첫 숫자와 새로운 숫자가 같을때 까지 반복
        break
    
    
    question = newQuestion
    answer.clear()
    newQuestion.clear()
    
print(cnt)'''
