'''
===============================================================================
  _                ____       _   
 | |__  _   _     |  _ \ __ _| |_ 
 | '_ \| | | |    | |_) / _` | __|
 | |_) | |_| |    |  __/ (_| | |_ 
 |_.__/ \__, |    |_|   \__,_|\__|
        |___/                     
===============================================================================
'''

import random
from werkzeug.security import generate_password_hash

def generar_contrasenia():
    '''
    PRE: A partir de distintas cadenas se genera una contraseña.
    POS: Retorna una contraseña generada con ninúsculas, mayúsculas, números
         y símbolos random.
    '''
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = minusculas.upper()
    numeros = "0123456789"
    simbolos = "!#$%&/()=?¡¿*[]{}.-_°|¬@"
    cadena_contrasenia = minusculas + mayusculas + numeros + simbolos
    longitud_contrasenia = 18
    cadena_generada = random.sample(cadena_contrasenia, longitud_contrasenia)
    contrasenia = "".join(cadena_generada)
    return contrasenia
    

def codificador_contrasenia(contrasenia):
    '''
    PRE: Ingresa una contraseña.
    POS: Retorna la contraseña codificada en sha256.
    '''
    return generate_password_hash(contrasenia)


if __name__ == "__main__":
    print("\n==================================================================")
    print("{:>35s}".format("RESULTADOS"))
    print("==================================================================")
    print(f"CONTRASEÑA GENERADA: {generar_contrasenia()}\nCONTRASEÑA ENCRIPTADA sha256: {codificador_contrasenia(generar_contrasenia())[14:]}")
    print("==================================================================")

