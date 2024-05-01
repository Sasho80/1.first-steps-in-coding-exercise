deposit_sum = float(input())
term_deposit_months = int(input())
annual_interest_rate = float(input())

accrued_interest = deposit_sum*((annual_interest_rate)/100)
interest_one_month = accrued_interest/12
amount_ens_deposit_period = deposit_sum+term_deposit_months*interest_one_month

print(f"{amount_ens_deposit_period } лв.")
