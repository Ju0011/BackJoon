x,y,w,h = map(int, input().split())
dis_x = 0
dis_y = 0

if x > w-x:
    dis_x = w-x
elif x < w-x:
    dis_x = x

if y > h-y:
    dis_y = h-y
else:
    dis_y = y

if dis_x > dis_y:
    print(dis_y)
else:
    print(dis_x)