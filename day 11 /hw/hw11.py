def calculator(x, y, op):
    if type(x) != int or type(y) != int:
        return "unknown value"
    elif op == "+" :
        return x + y
    elif op == "-" :
        return x - y
    elif op == "*" :
        return x * y
    elif op == "/" :
        return x / y
    else:
        return "unknown value"

def count_char_occurrences(strng, char):
    count = 0
    for i in strng:
        if i == char:
            count += 1
    return count