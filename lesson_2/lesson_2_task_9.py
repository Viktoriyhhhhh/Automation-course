
var_1 = 37
var_2 = 99
var_1=int(input("Введите значение var_1:  "))
var_2=int(input("Введите значение var_2:  "))
print(f"var_1: {var_1}", f"var_2: {var_2}")
var_1, var_2 = var_2, var_1
print(f"var_1: {var_1}", f"var_2: {var_2}")
