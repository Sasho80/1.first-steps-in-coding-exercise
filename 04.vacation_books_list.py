from math import floor

number_pages_current_book = int(input())
page_for_one_hour = int(input())
number_days_for_read_all_book = int(input())

total_time_to_read_book = number_pages_current_book/page_for_one_hour
required_hour_per_day = total_time_to_read_book/number_days_for_read_all_book
print(floor(required_hour_per_day))
