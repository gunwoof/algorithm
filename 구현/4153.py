from sys import stdin as s

while 1 :
    tri_angle=list(map(int,s.readline().split()))
    if tri_angle == [0,0,0]:
        exit()
    max_length=max(tri_angle)
    tri_angle.remove(max_length)

    if tri_angle[0]**2+tri_angle[1]**2==max_length**2:
        print("right")
    else:
        print("wrong")
    