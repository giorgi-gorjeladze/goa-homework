nums = [1,23,165,2,3,92,10,34,911]
res = []
def func(num):
    for i in nums:
        if i % num == 0:
            res.append (num)

print(res)

def reverse_list(l):
    return l[::-1]

def even_last(numbers): 
    if numbers == []:
        return 0

    sum = 0
    for i in range(0, len(numbers), 2): 
        sum += numbers[i]

    return sum * numbers[-1]
