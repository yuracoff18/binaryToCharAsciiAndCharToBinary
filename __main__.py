"""
Conversiones de binario a caracter y de caracter a binario

Integrantes:
    Yura Hernandez
    Martin Estrada

"""
from cadena_a_binario import cadena_a_binario

def main():
    print("============[Conversiones]============")
    print("""
Seleccione una opcion

1. De binarios a caracter
2. De caracter a binario
3. Salir
""")
    eleccion = int(input("Seleccion: "))
    if eleccion == 1:
        cadena=input("Ingrese el texto a convertir: ")
        print(f"texto inicial: {cadena} conversión: {cadena_a_binario(cadena)}")
    elif eleccion == 2:
        pass
    elif eleccion == 3:
        return 0
    else:
        print("Eleccion no valida\n")


if __name__ == "__main__":
    main()
