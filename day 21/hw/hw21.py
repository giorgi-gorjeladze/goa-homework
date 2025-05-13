def check_alive(health):
    if health <= 0: 
        return False
    else:
        return True

def repeat_str(repeat, string):
    return repeat * string

def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    if type(x) == int or type(x) == float:
        return "Who ate the last cookie? It was Monica!"
    if type(x) == bool:
        return "Who ate the last cookie? It was the dog!"
    
def century(year):
    if len(str(year)) == 4 and year % 100 != 0:
        return year // 100 + 1
    if year % 100 == 0 and len(str(year)) == 4:
        return year // 100
    if year < 100:
        return 1
    if year > 100 and year < 1000:
        return year // 100 + 1
    
def find_average(nums):
    return sum(nums) / len(nums)