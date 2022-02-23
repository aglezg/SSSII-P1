# -----------------------------------------------------
# Práctica 1: Cifrado de Vernam
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 24/02/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# -----------------------------------------------------

import binascii
from ctypes import sizeof
from tokenize import Number

# Convertir de ASCII a binario
def fromASCIIToBinary(ascii):
    
    if (type(ascii) == str):
        
        byte_array = ascii.encode()
        binary_int = int.from_bytes(byte_array, 'big')
        binary_string = bin(binary_int)
    
        binary_string = binary_string.replace('b', '') # ------------------

        while len(binary_string) % 8:
            binary_string = '0' + binary_string        # ------------------ encapsular en función?

        return binary_string

    else:

        return None


# Menú principal

def menu():
    print(" PRÁCTICA: CIFRADO DE VERNAM\n")
    print(" \t[0] Introducir mensaje original.")
    print(" \t[1] Introducir mensaje crifrado.")
    option = input(" \t> ")


original_m = input("Mensaje a cifrar > ")