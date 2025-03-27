def repeat_str(repeat, string):
    return repeat * string

def say_hello(name):
    return "Hello, " + name

def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    if p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    if p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    if p1 == "rock" and p2 == "paper":
         return "Player 2 won!"
    if p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    if p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    

    
def get_grade(s1, s2, s3):
       score = (s1 + s2 + s3) / 3
       if score <= 100 and score >= 90:
        return "A"
       if score < 90 and score >= 80:
        return "B"
       if score < 80 and score >= 70:
        return "C"
       if score < 70 and score >= 60:
        return "D"
       if score < 60:
        return "F"

       
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    
def name_surname(name, surname):
    name = name[0] + "."
    return name + surname
