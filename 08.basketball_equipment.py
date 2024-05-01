annual_fee_basketball_training = int(input())

price_basketball_shoes = annual_fee_basketball_training-0.4*annual_fee_basketball_training
price_basketball_equipment = price_basketball_shoes-0.2*price_basketball_shoes
price_basketball_ball = 0.25*price_basketball_equipment
price_basketball_accesсories = 0.2*price_basketball_ball
total_price_equipment = (annual_fee_basketball_training+price_basketball_shoes+price_basketball_equipment+
                        price_basketball_ball+price_basketball_accesсories)
print(total_price_equipment)