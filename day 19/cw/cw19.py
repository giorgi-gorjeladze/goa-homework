def six_toast(num):
    res = num-6
    if res<0:
        return 0-res
    return res

list1=[1]
list2=[2]
list3=[]
for i in list1:
    list3.append(i)
for i in list2:
    list3.append(i)


def remove_odd(num):
    list = []
    for i in num:
        if num % 2 == 0:
            list.append(num)
    return list


def lists(list):
    for i in list:
        res += str(i)
        return res
    

a = "code"
b = "wa.rs"
name = a + b