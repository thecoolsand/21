import random

cho = input("Do you want to give first?(Y/N): ")
last_num, c_num, num = 0, 0, 0
game_on = True


def check(number: int) -> bool:
    if number in range(last_num+1, last_num+4) and number <= 21:
        return True
    else:
        return False


if cho == 'Y':
    while game_on:
        while not check(num):
            num = int(input("Enter number: "))
        if num == 21:
            print("YOU LOST!!!")
            exit()
        last_num = num

        while not check(c_num):
            c_num = random.randint(last_num + 1, last_num + 4)
        if c_num == 21:
            print("YOU WON!!!")
            exit()
        last_num = c_num
        print(f"Computer chose: {c_num}")


else:
    while game_on:
        while not check(c_num):
            c_num = random.randint(last_num + 1, last_num + 4)

        if c_num == 21:
            print("YOU WON!!!")
            exit()
        last_num = c_num
        print(f"Computer chose: {c_num}")
        while not check(num):
            num = int(input("Enter number: "))
        if num == 21:
            print("YOU LOST!!!")
            exit()
        last_num = num
