def is_leap_year(year):
    return year % 4 == 0
year = int(input("Введите год: "))
if is_leap_year(year):
    print(f"год: {year}, True")
else:
    print(f"год: {year}, False")