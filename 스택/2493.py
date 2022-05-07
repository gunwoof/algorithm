from sys import stdin as s
N=int(s.readline())
towers_height=list(map(int,s.readline().split()))

tower_stack=[] # 스택에는 기준이 되는 높이를 내림차순으로 넣어야 함
stack_index=-1

towers_numbers=[0 for i in range(N)]

def push(i):
    global stack_index
    tower_stack.append([towers_height[i],i])
    stack_index += 1

def pop():
    global stack_index
    tower_stack.pop()
    stack_index -= 1


for i in range(N):
    if stack_index == -1: # 스택이 비었으면 무조건 push
        push(i)
        
    else :
        if towers_height[i] > tower_stack[stack_index][0]: # 스택의 값이 탑의 높이보다 작음
            while tower_stack[stack_index][0] < towers_height[i] : # 탑의 높이보다 큰 스택의 값이 나오도록 pop을 반복
                pop()
                if stack_index == -1:
                    break
            push(i)

            if stack_index == 0:
                towers_numbers[i] = 0
            else:
                towers_numbers[i]=tower_stack[stack_index-1][1]+1  #탑의 번호가 1부터 시작하기 때문

        elif towers_height[i] == tower_stack[stack_index][0]: # 스택의 값이 탑의 높이와 같으면 타워자리 index만 갱신해줌
            towers_numbers[i] = tower_stack[stack_index][1]+1 
            tower_stack[stack_index][1]=i

        else : # 스택의 값이 탑의 높이보다 큼
            towers_numbers[i] = tower_stack[stack_index][1]+1 
            push(i)

for i in towers_numbers:
    print(i, end=" ")






