nombre_producto = input("Ingrese el nombre del producto: ")
if nombre_producto == "":
    print("ERROR: ¡El nombre del producto no puede estar vacio!")
else:
    precio_producto = float(input("Ingrese el precio del producto: "))
    if precio_producto == "":
        print("ERROR: ¡El precio del producto no puede estar vacio!")
    else:
        if precio_producto <= 0:
            print("ERROR: ¡El precio del producto no puede ser menor o igual a cero!")
        else:
            descuento_producto = float(input("Ingrese el descuento del producto: "))
            if descuento_producto < 0 and descuento_producto > precio_producto:
                print("ERROR: ¡El descuento del producto no puede ser menor a cero y no puede ser mayor al precio del producto!")
            else:
                total_producto = precio_producto - descuento_producto
                print(f"El producto ingresado es: {nombre_producto} y el precio a pagar es: {total_producto} pesos.")