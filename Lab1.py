from random import randrange
from prettytable import PrettyTable
a0 = 1
a1 = 1
a2 = 3
a3 = 2
x1 = [randrange(1,21,1) for _ in range(8)]
x2 = [randrange(1,21,1) for _ in range(8)]
x3 = [randrange(1,21,1) for _ in range(8)]
list_Y = [a0 + a1*x1[i] + a2*x2[i] + a3*x3[i] for i in range(8)]
x01 = (max(x1)+min(x1))/2
x02 = (max(x2)+min(x2))/2
x03 = (max(x3)+min(x3))/2
dx1 = x01-min(x1)
dx2 = x02-min(x2)
dx3 = x03-min(x3)
xn1 = [round((x1[i] - x01)/dx1, 2) for i in range(8)]
xn2 = [round((x2[i] - x02)/dx2, 2) for i in range(8)]
xn3 = [round((x3[i] - x03)/dx3, 2) for i in range(8)]
Y_et = a0 + a1*x01 + a2*x02 + a3*x03
result = max([elem for elem in list_Y if elem < Y_et])
print("a0={} a1={} a2={} a3={}".format(a0, a1, a2, a3))
print("x1: " + str(x1))
print("x2: " + str(x2))
print("x3: " + str(x3))
print("Y: " + str(list_Y))
print("x0: {} {} {}".format(x01, x02, x03))
print("dx: {} {} {}".format(dx1, dx2, dx3))
print("Xн1: {}".format(xn1))
print("Xн2: {}".format(xn2))
print("Xн3: {}".format(xn3))
print("Yэт: {}".format(Y_et))
print("Yэт←: {}".format(result))
print("\nРезультат у вигляді таблиці:")
table_val = [x1, x2, x3, list_Y, xn1, xn2, xn3]
table_val_t_tup = list(zip(*table_val))
table = PrettyTable()
table.field_names = ["№", "x1", "x2", "x3", "Y", "хн1", "хн2", "хн3"]
for x in range(1, len(table_val_t_tup)+1):
    table.add_row([x] + list(table_val_t_tup[x-1]))
table.add_row(["x0", x01, x02, x03, "", "", "", ""])
table.add_row(["dx", dx1, dx2, dx3, "", "", "", ""])
print(table)