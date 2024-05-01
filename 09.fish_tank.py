lenght_fish_tank = int(input())
width_fish_tank = int(input())
hеight_fish_tank = int(input())
percent_liter_water = float(input())

volume_fish_tank =lenght_fish_tank*width_fish_tank*hеight_fish_tank
volume_in_liters = (volume_fish_tank)*0.001
occupied_price = (percent_liter_water/100)*volume_in_liters
need_liters = volume_in_liters-occupied_price
print(need_liters)


