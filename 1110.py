question = list(input()) # 숫자 한 자리씩 한 방에 넣어 둠
answer = 0
oriQuestion = 0
newQuestion =0
cnt =0

while 1 :
    if len(question) == 1:
        question.append(int(question[0]))
        question[0] = 0
    question =  list(map(int,question))

    oriQuestion = question 
    
    answer = list(str(sum(question)))
    if len(answer) == 1:
        answer.append(answer[0])
        answer[0] =0
    answer = list(map(int,answer))

    newQuestion = question[1]+answer[1]

    # if newQuestion 과     oriQuestion의 타입을 같게해야함


print(question,answer)