# #Coffee Shop Project
# # import numbers
# import time
#
# import wrong as wrong
# import yes as yes

print("hellow welcome to coffee shop\n")

name = input("what is your name ?\n\n")

print("\nhello " + name + ",thank you so much for coming in today\n")

menu = 'Black coffee - $6\n''expresso - $10\n''latte - $8\n''cappuccino - $7\n'

coffee_menu = ['Black coffee', 'expresso', 'latte', 'cappuccino']

# file_name = 'text.txt'

coffee_price = ['6', '10', '8', '7']

numbers = range(51)

# order in manu


def main():
    print(name + ", what would you like from our menu ?\n\n" + menu, )
    while True:
        try:
            global order
            order = input()
            if order in coffee_menu:
                idx = coffee_menu.index(order)
                price = coffee_price[idx]
                print("\ngreat choice")
                break
            else:
                print("coffee not in the menu")
        except ValueError:
            continue

    while True:
        try:
            global quantity
            quantity = int(input("\nhow many coffees would you like ? \n\n"))
            if quantity in numbers:
                break
            else:
                print("enter the correct values")
        except ValueError:
            continue

    if order in coffee_menu:
        total = int(price) * int(quantity)
        print("your coffee(s) {} {} costs ${}".format(order, quantity, total))
    else:
        print("")

    print(
        "\nsounds good " + name + ", we'll have you that " + order + "ready for you in a moments \nneed any other "
                                                                     "things ?\n")

    while True:
        try:
            answer = input("please say yes/no ?\n")
            yes = ('yes', 'YES')
            if answer in yes:
                main()
            else:
                print("\nthank you")
                break
        except ValueError:
            break


main()



# with open(file_name, 'w', encoding='utf-8') as file:
#     file.write(order + '\n')
#
# with open(file_name, '+a', encoding='utf-8') as file:
#     file.write(quantity + '\n')
#
# with open(file_name) as order_list:
#     order_text = order_list.read()
#     print(order_text)

# print("\n" + name + ", Thank you for waiting, here's your " + quantity + " " + order + ". welcome back again")
