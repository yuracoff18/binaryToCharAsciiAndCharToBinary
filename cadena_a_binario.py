"""
Lo que realiza esta función es convertir una cadena de caracteres a binario

Creado por:
  Martín Estrada

"""

def cadena_a_binario(cadena):
  return ' '.join(format(ord(c), '08b') for c in cadena)
