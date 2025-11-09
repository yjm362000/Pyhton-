
# letters = [
#     "a", "b", "c", "d", "e", "f", "g",
#     "h", "i", "j", "k", "l", "m", "n",
#     "o", "p", "q", "r", "s", "t", "u",
#     "v", "w", "x", "y", "z"
# ]
# start=input("typle encode to encrypt, type decode to decrypt: \n")
# if start == "encode":
#     message = input("please input your message: \n")
#     shift = int(input("please input your shift: \n"))
#     password = ""
#     for i in message:
#         i_lower = i.lower()
#         if i_lower in letters:
#             number_word = letters.index(i_lower)
#             size = (number_word + shift)%26
#             encoded = letters[size]
#             password += encoded
#         else: 
#             password += i
        
#     print(password)
    
# elif start =="decode":
#     back_message=input("please input your message: \n")
#     back_shift=int(input("please input your shift: \n"))
#     plain_text=""
#     for x in back_message:
#         x_lower = x.lower()
#         if x_lower in letters: 
#             decoded_number_word = letters.index(x_lower)
#             decode_size = (decoded_number_word - back_shift)%26
#             decoded = letters[decode_size]
#             plain_text += decoded
#         else:
#             plain_text += x
#     print(plain_text)

# else: 
#     print(f'please type encode or decode, you type neither of them!')


# word="d"
# print(letters.index(word))
# bid = {}
# while True: 
#     name = input("Please input your name here: ")
#     price = input("Please input your price here: ")
    
#     bid[name] = price
#     while True:
#         last = input("are you the last one? yes/no ")
#         if last.lower()=="yes" or last.lower()=="no":
#             break
#         else:
#             print("Please type yes or no")

#     if last.lower() == "yes":
#         break 
# print(bid)
# price_list = []
# for i in bid:
#     price_list.append(bid[i])
# print(price_list)

# largest = max(map(int,price_list))
# print(f"The largest number is {largest}")

# def format(First_name, Last_name):
#     First_name = First_name.title()
#     Last_name = Last_name.title()
#     return f'Your first name is {First_name}, and your last name is {Last_name}'

# formated = format(First_name="randy",Last_name="you")
# print(formated)

# def leap(year):
#     if year % 4 == 0:
#         if year % 100 ==0:
#             if year % 400 == 0:
#                 return "True" 
#             else:
#                 return "False"
#         else:
#             return "True"
#     else:
#         return "False"

# result = leap(int(input("please input the year :")))
# print(result)

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b


Symbol_list ={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide

}
def calculator():
    num1 = int(input("What's your first number: \n"))
    should_go = True
    while should_go:
        while True:
            symbol = input(f"+\n-\n*\n/\npick an operation: ")
            if symbol in {"+", "-", "*", "/"}:
                break
            else:
                print("please enter a correct symbol")
        
        num2 = int(input("What's the next number: \n"))
        result = Symbol_list[symbol](num1,num2)
        print(f'{num1}{symbol}{num2}={result}')
        go_on = input("Would you like to use the result and go on? y/n: \n")
        if go_on.lower() == "y":
            num1 = result
        else:
            should_go = False
            print("\n"* 20)
            calculator()

calculator()



