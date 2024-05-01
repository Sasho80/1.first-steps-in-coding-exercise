PACK_PENS = 5.80
MARKER_PACK = 7.20
PREPARATION_LITER = 1.20

number_pack_pens = int(input())
number_pack_marker = int(input())
liters_chalckboard_cleaner = int(input())
percent_discount = int(input())

price_chemical_packeges = number_pack_pens*PACK_PENS
price_preparation = liters_chalckboard_cleaner*PREPARATION_LITER
price_pack_marker = number_pack_marker*MARKER_PACK

price_all_materials = price_chemical_packeges+price_preparation+price_pack_marker
price_with_discount = price_all_materials-(price_all_materials*(percent_discount/100))

print(price_with_discount)
