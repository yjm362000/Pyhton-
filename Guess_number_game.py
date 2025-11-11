import random

def rand_number():
    number = random.randint(0,100)
    return number


def level_choice():
    while True:
        choice = input("please choose your level: hard or easy: ")
        if choice.lower() == "hard":
            return 5
            break
        elif choice.lower() == "easy":
            return 10
            break
        else:
            print("You type a wrong input! please revise!")

def main_function():
    number = rand_number()
    attmpt = level_choice()
    while True:
        guess = int(input("please input your guess here (must be an integer!) : \n"))
        if guess < number:
            print("Your number is less than the answer")
            attmpt -= 1 
            print(f"attmpt:{attmpt}")
            if attmpt == 0:
                print("You lose!")
                break
        elif guess > number:
            print("Your number is greater than the answer")
            attmpt -= 1
            print(f"attmpt:{attmpt}")
            if attmpt == 0:
                print("You lose!")
                break
        elif guess == number:
            print("Congradulation! You got the answer!")
            break

main_function()
    
    