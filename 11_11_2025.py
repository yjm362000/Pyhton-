import random

def fans():
    number_of_fans = random.choice(range(100,10000))
    return number_of_fans

def name():
    return {
        "Charile": fans(),
        "Mindy":fans(),
        "Randy":fans(),
        "Rachel":fans(),
        "Tim":fans(),
        "Rose":fans(),
        "Curry":fans(),
        "Stephen":fans(),
        "Windy":fans()
    }

def main_function():
    score = 0
    stars = name()
    print("Welcome to the 'higher or lower' games! ")
    list_name = []
    for i in stars.keys():
        list_name.append(i) 
    while True:
        while True:
            key_name1 =random.choice(list_name)
            key_value1 = stars[key_name1]
            key_name2 = random.choice(list_name)
            key_value2 = stars[key_name2]
            if key_name1 != key_name2 and key_value1 != key_value2:
                break

        print(f"Compare A : {key_name1}")
        print(f"Compare B : {key_name2}")
        guess = input("Which one has higher fans: A/B \n")
        if guess.lower() == "a" and key_value1 > key_value2:
            print("Correct You Win!")
            score += 1
            print("\n" * 30)
            print(f'Your score is {score}!')
        elif guess.lower() == "a" and key_value1 < key_value2:
            print("incorrect, game over")
            print(f'Final score is {score}!')
            break
        elif guess.lower() == "b" and key_value1 > key_value2:
            print("incorrect, game over")
            print(f'Final score is {score}!')
            break
        else:
            print("Correct You win!")    
            score += 1
            print("\n" * 30)
            print(f'Your score is {score}!')
            

        


main_function()