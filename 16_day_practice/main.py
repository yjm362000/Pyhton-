import coffee_maker
import menu
import money_machine

my_money_machine = money_machine.MoneyMachine() #首先把class存进一个variable
my_coffee_make = coffee_maker.CoffeeMaker()
my_menu  = menu.Menu()
drink1 = my_menu.find_drink("latte")
drink2 = my_menu.find_drink("espresso")
drink3 = my_menu.find_drink("cappuccino")

is_on = True 

while is_on:
    check = input("Ingredients  /   order:\n")
    if check.lower() == "ingredients":
        print(f'Latte : {drink1.ingredients}')
        print(f'Espresso : {drink2.ingredients}')
        print(f'Cappuccino : {drink3.ingredients}')
    elif check == "report":
        my_coffee_make.report()
        my_money_machine.report() 
    elif check == "off":
        is_on = False
        
    else:  
        option = my_menu.get_items()
        choice = input(f"please make your choice {option}:")
        if choice == "off":
            is_on = False
        elif choice == "report":
            my_coffee_make.report()
            my_money_machine.report() 
        else:
            drink = my_menu.find_drink(choice)
            print("\n")

            if my_coffee_make.is_resource_sufficient(drink):
                price=drink.cost
                print(f"Total is {price} dollars")
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_make.make_coffee(drink)
            
        



