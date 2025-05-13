def func1(li1,li2):
    li3 = li1 + li2
    li3.sort

def func2(li1, li2):
    sum1 = sum(li1)
    sum2 = sum(li2)
    if sum1 > sum2:
        return sum1
    if sum2 > sum1:
        return sum2

def func3(li1,li2):
    li3=[]
    li4=[]
    for i in li1:
        if i > 0:
            li3.append(i)
        if i < 0:
            li4.append(i)
    for i in li2:
        if i > 0:
            li3.append(i)
        if i < 0:
            li4.append(i)
    return sum(li3) , len(li4)

def func4(li):
    for i in li:
        if i % 3 == 0:
            li.pop(i)
    return li

def func5(li):
    li2 = []
    for i in li:
        li2.append(i*2)
    return li2
