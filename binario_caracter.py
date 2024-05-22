"""

Modulo de conversion de binario a caracter con ascii

Creador:
    Yura Hernandez

"""
def fromBinToChar(binarios):
    
    final = ""
    code = binarios.split()
    
    for i in range(len(code)):
        
        binario = int(code[i])
        decimal = 0
        ii = 0
        while (binario > 0):
            digito  = binario % 10
            binario = int(binario // 10)
            decimal = decimal + digito *(2 ** ii)
            ii = ii+1
        
        caracter = chr(decimal)
        final += f"{caracter}-{decimal}/ "
        
    return final
