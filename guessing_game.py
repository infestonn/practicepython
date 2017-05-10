import random

def user_answer():
    return raw_input("[H/L/right]: ")


def calculate(ans1, ans2):
    l = range(ans1, ans2)
    return l[len(l)/2]


def calculate_low(ans1, ans3):
    l = range(ans1,ans3)
    return l[len(l)/2]


print(random.randint(0,100))  #debug
ans1 = 0
ans2 = 100
ans3 = 50
direction = ""
counter = 0

while direction != "right":
    try:
        print("Is it %d?" % ans3)
        counter += 1
        direction = user_answer()
        if direction == "H":
            ans1 = ans3
            ans3 = calculate(ans3, ans2)
        elif direction == "L":
            ans2 = ans3
            ans3 = calculate_low(ans1, ans3)
        elif direction == "right":
            print("Yeaaah! I guessed your number with %d tries:" % counter)
        else:
            break
    except IndexError:
        print("You are liar!")
        exit()
exit()
