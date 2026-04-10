from dataclasses import replace


def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
Linea 2
Linea 3"""

    print(f"strip: {nombre.strip()}")
    print(f"strip: {nombre.lstrip()}")
    print(f"strip: {nombre.rstrip()}")
    print(f"upper: {frase.upper()}")
    print(f"lower: {frase.lower()}")
    print(f"title: {frase.title()}")
    print(f"find: {frase.find("Python")}")
    print(f"find: {frase.find("Java")}")
    print(f"Grace in nombre: {"Grace" in nombre}")
    print(f"replace: {frase.replace('programacion','desarrollo')}")
    print(f"count: {frase.count('a')}")
    print(frase[0:6:1])
    print(frase[0:6:2])
    print(frase[5::-1])
    print(f"{nombre.strip() + " sabe " +frase[0:6]}")
    print(multilinea.strip())


