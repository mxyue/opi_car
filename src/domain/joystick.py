import math
#暂时未使用，传入参数已经计算为角度

def angle(x, y):
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            ang = math.atan((y/x))
            return math.degrees(ang)
        elif x < 0 and y > 0:
            ang = math.atan((y/-x))
            return 180 - math.degrees(ang)
        elif x < 0 and y < 0:
            ang = math.atan((y/x))
            return 180 + math.degrees(ang)
        elif x > 0 and y < 0:
            ang = math.atan((-y/x))
            return 360 - math.degrees(ang)
        else:
            print('不知道')
            

def distance(x, y):
    return math.sqrt(x*x + y*y)

