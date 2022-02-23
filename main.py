# -----------------------------------------------------
# Práctica 1: Cifrado de Vernam
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 24/02/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# -----------------------------------------------------

import os

# Limpia la pantalla de la terminal
def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Comprueba si una variables es un string
def isString(mystring):
    if (type(mystring) == str):
        return True
    else:
        return False

# Convertir de string a binario
def stringToBinary(mystring):

    if (isString(mystring)):
        return ''.join(format(ord(i), '08b') for i in mystring)
    else:
        return None

# Comprueba si un string es una cadena binaria
def isABinaryString(bstring):

    if (not(isString(bstring))):
        return False

    for letter in bstring:
        if (letter != '1' and letter != '0'):
            return False
    return True

# Transforma una cadena binaria en un array de cadenas binarias de cierta longitud
def stringToArrayOfStringS(mystring, long = 8):
    
    myarray = []
    aux_string = ""

    if(isABinaryString(mystring)):
        for letter in mystring:
            aux_string += letter
            if (len(aux_string) == long):
                myarray.append(aux_string)
                aux_string = ''

        return myarray
    
    else:
        return None

# Convertir una cadena binaria en cadena ascii
def binaryStringToASCIIString(bstring):

    ascii_string = ''

    if (isABinaryString(bstring)):
        binary_array = stringToArrayOfStringS(bstring)
        ascii_string = ''
        for element in binary_array:
            ascii_string += chr(int(element,2))
    else:
        return None

    return ascii_string

# Operación XOR entre cadenas de binario
def bStringXORBString(bstring1, bstring2):

    if (isABinaryString(bstring1) and isABinaryString(bstring2)):
        numeric_result = int(bstring1, 2) ^ int(bstring2, 2)
        binary_result = '{0:b}'.format(numeric_result)
        while (len(binary_result) != len(bstring1) or len(binary_result) != len(bstring2)):
            binary_result = '0' + binary_result
        return binary_result
    else:
        return None

# Menú principal
def menu():
    
    option = ''
    
    while (option != '0' and option != '1'):
        cleanTerminal()
        print("\n PRÁCTICA: CIFRADO DE VERNAM\n")
        print(" \t[0] Introducir mensaje original.")
        print(" \t[1] Introducir mensaje cifrado.\n")
        option = input(" \t> ")
    
    if (option == '0'):
        option = 'original'
    else:
        option = 'cifrado'
    
    message = input("\n\t >> Mensaje " + option + ": ")
    binary_message = stringToBinary(message)
    print("\t\t-> Mensaje " + option + " en binario: " + binary_message)
    print("\t\t-> Longitud: " + str(len(binary_message)))

    key = ''
    
    while(not(isABinaryString(key)) or len(key) != len(binary_message)):
        key = input("\n\t >> Clave aleatoria: ")

    binary_result = bStringXORBString(binary_message, key)

    print("\n\t >> Mensaje " + option + " en binario: " + binary_result)
    print("\t >> Mensaje " + option + ": " + binaryStringToASCIIString(binary_result))



# Main
menu()