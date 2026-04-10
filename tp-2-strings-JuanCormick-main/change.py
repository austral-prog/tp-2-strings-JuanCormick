def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto= float(input("Ingrese el gasto: "))
    dinero= int (input("Ingrese el dinero: "))
    pesos= int(dinero-gasto)
    centavos = (dinero-gasto)-pesos
    print (pesos)
    print(centavos)
