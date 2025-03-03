num1 = int(input())
sum = 0
for i in range(1,num1+1,2):
   sum += i
print(sum)

num2 = int(input())
for i in range(1,num2):
    if num2%i == 0:
        print(i)

password = input("the password has to be over 8 charcters and must contain A:")
tries = 3
while len(password) < 8 and "A" not in password:
    print("please try again: ")
    password = input("input password:")
    tries = tries - 1
    tries == 0
    break
    if len(password) >= 8 and "A" in password:
        print("correct")


name = input()
result = " "
for i in name:
    result = i + result
print(result)
