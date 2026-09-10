nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
descuento_producto = float(input("Ingrese el descuento del producto: "))

total_producto = precio_producto - descuento_producto

print(f"El producto ingresado es: {nombre_producto} y el precio a pagar es: {total_producto} pesos.")