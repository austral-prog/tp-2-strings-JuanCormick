def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    precio = int (input("precio: "))
    descuento = float (input("descuento: "))
    cantidad = int (input("cantidad: "))
    precio_final = precio - descuento
    total= precio_final*cantidad
    print(precio_final)
    print(total)

