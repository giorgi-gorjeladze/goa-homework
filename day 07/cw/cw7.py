reversed_string = input("enter something: ")
result = " "
for i in reversed_string:
    result = i + result
print(result)

sum = 0
for i in range(101):
   sum += i
print(sum)

res = " "
name = input("please input a word: ")
while not len(name) == 3:
    print("there must be 3 charecters")
    name = input("please input a word")
    for i in name:
        res = i + res
        if res == name:
            print("palindromi")
        else:
            print("ar aris palindromi")
    

for i in range(100,301):
    print(i*i)

for i in range(1000):
    print("True, false")

