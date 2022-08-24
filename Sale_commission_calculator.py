nombre = input("Cual es tu nombre? ")
ventas = input("Anota tus ventas: ")
ventas = float(ventas)
comision = input("Porcetaje de la comissión: ")
comision = float(comision)
print(f"{nombre} tu comissión es de {round(ventas * (comision/100) ,2)}")

#Mohamed_Laaouaj