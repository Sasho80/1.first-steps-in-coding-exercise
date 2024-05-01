CHICKEN_MENU = 10.35
MENU_FISH = 12.40
VEGAN_MENU = 8.15
DESSERT_DISCOUNT = 0.2
PRICE_DELIVERY = 2.50

num_chicken_menus = int(input())
num_fish_menus = int(input())
num_vegan_menus = int(input())

price_chicken_menus = num_chicken_menus*CHICKEN_MENU
price_fish_menus = num_fish_menus*MENU_FISH
price_vegan_menus = num_vegan_menus*VEGAN_MENU
total_price_menus = price_chicken_menus+price_fish_menus+price_vegan_menus
price_dessert = DESSERT_DISCOUNT*total_price_menus
total_price_order = total_price_menus+price_dessert+PRICE_DELIVERY
format_float = "{:.2f}".format(total_price_order)
print(format_float)



