def res(num):
    x=0
    for i in str(num):
        x+=int(i)
    return num % x

def even_or_odd(num):
    if num%2==1:
        num += 1
    return num

def calc(num):
    ans=0
    x=0
    if num%2==0:
        x == num=+5
    else:
        x == num*3
    ans=(x+num) % 5
    return ans



name = input()
surname = input()
age = input()
country = input()
print(f'hi, I am {name} {surname}, {age} y.o. I am from {country}')

#num = 2
#print("Hello " + str(num) + " world")
#print("Hello", num, "world")
#print(f'Hello {num} world') 
# "მესამე ვარიანტი ყველაზე მეტად მომწონს, იმიტომ რომ ყველაზე მოკლე და მარტივად გასაგებია"