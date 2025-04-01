nums = [1,4,3,6,9,11,17,13,26,30]
res = 0
res_2 = 0
for i in nums:
    if i % 2 == 0:
        res += i
    else:
        res_2 += 1



nums = [1,2,3]
nums.append(4)


nums = [1,2,3,3,4,5]
nums.pop(2)

nums = [1,2,3,4,6,8,9]
nums.insert(4,5)
nums.insert(6,7)


# append - ამატებს წევრს ლისტის ბოლოს
# pop - შლის მითითებულ წევრს
# insert - ამატებს წევრს მითითებულ პოზიციაზე 