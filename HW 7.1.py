# Task 1"""Find The Distance Between Two Points"""
def distance(x1, y1, x2, y2):
    dis = round((((x2-x1)**2+(y2-y1)**2)**0.5),2)
    return dis