v_1 = 37
v_2 = 99
temp = v_1
v_1 = v_2
v_2 = temp
print("Value of v_1:", v_1)
print("Value of v_2:", v_2)

#или

var_1 = 37
var_2 = 99

var_1, var_2 = var_2, var_1

print("Обновленные переменные:")
print("var_1 =", var_1)
print("var_2 =", var_2)