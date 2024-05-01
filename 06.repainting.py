SAFETY_NYLON = 1.50
PAINT = 14.50
PAINT_TINNER = 5.00
ADDITIVE_PAINT=0.10
TWO_SQUARE_METER_NYLON= 2
BAGS=0.40

nessesary_amount_nylon = int(input())
nessesary_amount_paint = int(input())
amount_tinner = int(input())
hours = int(input())

sum_nylon = (nessesary_amount_nylon+ TWO_SQUARE_METER_NYLON)*SAFETY_NYLON
sum_paint = (nessesary_amount_paint+ADDITIVE_PAINT*nessesary_amount_paint)*PAINT
sum_tinner = amount_tinner*PAINT_TINNER
sum_bags = BAGS

total_sum_materials = sum_nylon+sum_paint+sum_tinner+BAGS
sum_master = (total_sum_materials*0.3)*hours
total_sum = total_sum_materials+sum_master
format_float = "{:.2f}".format(total_sum) #Python print 2 decimal places
print(f"{format_float} лв.")



