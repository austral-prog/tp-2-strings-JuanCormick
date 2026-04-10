def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    pass
    nombre= input("Ingrese un nombre: ")
    nombre1= nombre.lower()
    print(f"contiene a: {("a" in nombre1)}")
    print(f"contiene e: {("e" in nombre1)}")
    print(f"contiene i: {("i" in nombre1)}")
    print(f"contiene o: {("o" in nombre1)}")
    print(f"contiene u: {("u" in nombre1)}")
