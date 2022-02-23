# -----------------------------------------------------
# Práctica 1: Cifrado de Vernam
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 24/02/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# -----------------------------------------------------

from functions import *

# Menú principal

option = ''

while (option != 'exit'):
    
    cleanTerminal()

    while (option != 'o' and option != 'c' and option != 'exit'):
        print("\n PRÁCTICA: CIFRADO DE VERNAM\n")
        print(" \t[o] Introducir mensaje original.")
        print(" \t[c] Introducir mensaje cifrado.")
        print(" \t[exit] Finalizar el programa.\n")
        option = input(" \t> ")
    
    if (option == 'o'):
        option = 'original'
    elif (option == 'c'):
        option = 'cifrado'
    else:
        break
    
    message = input("\n\t >> Mensaje " + option + ": ")
    binary_message = stringToBinary(message)
    print("\t\t-> Mensaje " + option + " en binario: " + binary_message)
    print("\t\t-> Longitud: " + str(len(binary_message)))

    key = ''
    
    while(not(isABinaryString(key)) or len(key) != len(binary_message)):
        key = input("\n\t >> Clave aleatoria: ")
        if (not(isABinaryString(key))):
            print("\t ¡OJO! La clave introducida no es una cadena binaria...")
        elif (len(key) != len(binary_message)):
            print("\t ¡OJO! La clave introducida no es del mismo tamaño que el mensaje...")

    binary_result = bStringXORBString(binary_message, key)

    if (option == 'original'):
        option = 'cifrado'
    else:
        option = 'original'

    print("\n\t >> Mensaje " + option + " en binario: " + binary_result)
    print("\t >> Mensaje " + option + ": " + binaryStringToASCIIString(binary_result))

    input("\n\n\n\t Press Enter to continue...")