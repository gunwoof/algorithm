from sys import stdin as s

def quick_array(arr,start,end):
    if start>=end:
        return
    
    pivat=start
    left=start
    right=end
   
    while left<right :
        while left<end and arr[left]<=arr[pivat]: # 피벗보다 같거나 작다면 넘기기-> 큰 것만 찾으라는 이야기
            left +=1
        while right>start and arr[right]>=arr[pivat]: # 피벗보다 같거나 크다면 넘기기-> 작은 것만 찾으라는 이야기
            right -=1
            
        if left >= right : # 엇갈리면 작은것과 피벗을 교환
            arr[pivat],arr[right] = arr[right],arr[pivat]
        else : # 엇갈린게 아니면 left와 right자리바꿈
            arr[left],arr[right] = arr[right],arr[left]
    
    quick_array(arr,start,right-1) # start+1이 이난것은 맨 앞자리에 제일 작은수가 아닐 수도 있기 때문
    quick_array(arr,right+1,end)



N = int(s.readline())
number=[]

for i in range(N):
    number.append(int(s.readline()))

quick_array(number,0,len(number)-1)
'''for i in number:
    print(i)'''
print(number)
