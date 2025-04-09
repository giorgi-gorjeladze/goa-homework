def manual_remove(l):
    res = []
    if type(l) == list:
        res == []
    return res

def manual_index(l, ind):
    if type(l) == list:
        for i in l:
            if i == ind:
                return l.index(i)


def manual_len(l):
    res = 0
    if type(l) == list:
        for i in l:
            res += 1
    else: 
        for i in str(l):
            res += 1
    return res


def manual_pop(l,ind):
    if type(l) == list:
        for i in l:
            if i == ind:
                return l.pop(i)

def manual_reverse(l):
    return l[::-1]




