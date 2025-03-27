def make_negative( number ):
    if number>0:
        return 0 - number
    if number<=0:
        return number
def solution(string):
    new_string = ""
    for i in string:
        new_string = i + new_string
    return new_string 
def number_to_string(num):
    return str(num)