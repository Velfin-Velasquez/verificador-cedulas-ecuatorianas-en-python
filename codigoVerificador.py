tipo = [2,1,2,1,2,1,2,1,2]
cedula = input("Ingrese número de cédula: ")
acu = 0
for i in range(9):
    dato = int(cedula[i]) * tipo[i] 
    if dato > 9:
        dato -= 9
    acu += dato
print('acu: ',acu)
while acu > 0:
    acu-=10
print('reducción de acu: ',abs(acu))
if abs(acu) == int(cedula[-1]):
    print('Dígito verificador ok')
else:
    print('Dígito verificador con ERROR')