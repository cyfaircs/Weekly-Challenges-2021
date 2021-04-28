from testing import title, test

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def index_before_exceeding_sum(xs, total):
  sum = 0
  index = 0
  while sum < total and index < len(xs):
    sum += xs[index]
    index += 1
  return index - 1 if index > 0 else index

def get_month_from_day_of_year(day):
    return months[index_before_exceeding_sum(days_in_months, day)]

# TESTING STUFF
title(index_before_exceeding_sum)
test(4, index_before_exceeding_sum, [1, 2, 3, 4, 5, 6, 7, 8], 15)
test(3, index_before_exceeding_sum, [1, 2, 3, 4], 20)
test(0, index_before_exceeding_sum, [50, 30, 20], 20)
test(0, index_before_exceeding_sum, [50, 30, 20], 0)
test(0, index_before_exceeding_sum, [50, 30, 20], -5)

title(get_month_from_day_of_year)
test("January", get_month_from_day_of_year, 31)
test("February", get_month_from_day_of_year, 32)
test("January", get_month_from_day_of_year, 1)
test("January", get_month_from_day_of_year, 0)
test("January", get_month_from_day_of_year, -1)
test("December", get_month_from_day_of_year, 365)
test("December", get_month_from_day_of_year, 364)
test("February", get_month_from_day_of_year, 50)
