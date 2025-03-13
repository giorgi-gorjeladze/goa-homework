num1 = int(input())
for i in range(1,101):
    print(i * num1)

num2 = 1234
guess = int(input("enter a number: "))
while guess != num2:
    print("try again")
    guess = int(input("enter a number: "))   
print("correct")