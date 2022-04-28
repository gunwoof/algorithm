from sys import stdin as s
from math import sqrt

number = int(s.readline())
coordinate = []

for i in range(number):
    coordinate = list(map(int,s.readline().split()))
    max_r=max([coordinate[2],coordinate[5]])
    min_r=min([coordinate[2],coordinate[5]])
    distance=sqrt((coordinate[3]-coordinate[0])**2+(coordinate[4]-coordinate[1])**2)
    
    if  coordinate[0]==coordinate[3] and coordinate[1]==coordinate[4]:
        if coordinate[2]==coordinate[5]: # 무한대(좌표와 반지름 모두 같음)
            print(-1)
        else : # 교점 0개(좌표는 같은데 반지름이 다름)
            print(0)
    
    if coordinate[0] != coordinate[3] or coordinate[1] != coordinate[4]:
        if distance < max_r-min_r or distance > max_r+min_r: # 교점 0개(원안에 원이 있던지 두 원이 떨어져 있음)
            print(0)
        
        if distance == max_r-min_r or distance == max_r+min_r: # 교점 1개(원이 내접하던지 외접함)
            print(1)
        
        if max_r-min_r < distance  and distance < max_r+min_r: # 핵심 : 교점 2개
            print(2)
        
       
