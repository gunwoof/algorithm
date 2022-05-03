from sys import stdin as s

def change(i): 
    if i == ')':
        return '('
    elif i ==']':
        return '['

def stack(arr):
    bracket=[]
    bracket_index =- 1
    for i in arr:
        if i == "(" or i=="[":
            bracket.append(i)
            bracket_index += 1
          
        if (i == ")" or i == "]") :
            if bracket_index == -1: # 처음부터 닫는 괄호 나오면 'no'출력
                print("no")
                return

            j=change(i)
            if j == bracket[bracket_index]:
                bracket.pop()
                bracket_index -= 1
            else : # 다른 괄호 나오면 'no'출력
                print("no")
                return

    if bracket_index == -1 : # 스택이 비었으면 'yes'출력
        print("yes")
    else : # 스택이 남아있으면(괄호가 안 닫혔다면) 'yes'출력
        print("no")
    
sentence=[]

while 1:
    sentence=list(s.readline().rstrip())
    if sentence == ['.']:
        exit()
    stack(sentence)
    sentence.clear()
    



