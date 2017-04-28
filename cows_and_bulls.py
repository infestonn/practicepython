import random


def user_input(messg="Enter the number from 1000 to 9999:"):
    i = raw_input(messg)
    try:
        i = int(i)
    except ValueError:
        pass
    return i if type(i) == int and len(str(i)) == 4 else "nope"


def cows(dig1, dig2):
    dig1 = str(dig1)
    dig2 = str(dig2)
    cow = 0
    for i in range(0,len(dig1)):
        if dig1[i] == dig2[i]:
            cow += 1
    return cow


def bulls(dig1, dig2):
    dig1 = str(dig1)
    dig2 = str(dig2)
    bull = 0
    for i in dig1:
        if i in dig2:
            bull += 1
    return bull


def main_prog():
    digits = random.randrange(1000, 10001, 4)
    print(digits) #for debugging
    g = user_input()
    while digits != g:
        c = cows(digits, g)
        b = bulls(digits, g)
        print("{c} {cow}, {b} {bull}".format(c=c, b=b, cow="cow" if c <= 1 else "cows", bull="bull" if b <= 1 else "bulls"))
        g = user_input()
    print("gz! You win")
    exit()

if __name__ == "__main__":
    main_prog()