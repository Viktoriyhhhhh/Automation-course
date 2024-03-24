def month_to_season(month):
    if month in (1,2,12):
        return "зима"
    if month in (3,4,5):
        return "весна"
    if month in (6,7,8):
        return "лето"
    if month in (9,10,11):
        return "осень"
    else:
        return "Такого месяца не существует"

print(month_to_season(int(input("Введите номер месяца: "))))

