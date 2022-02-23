# -----------------------------------------------------
# Práctica 1: Cifrado de Vernam
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 24/02/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# -----------------------------------------------------

# Convertir de string a binario
def stringToBinary(mystring):

    if (type(mystring) == str):
        return ''.join(format(ord(i), '08b') for i in mystring)
    else:
        return None

# Comprueba si un string es una cadena binaria
def isABinaryString(bstring):
    for letter in bstring:
        if (letter != '1' and letter != '0'):
            return False
    return True

# Menú principal
def menu():
    print(" PRÁCTICA: CIFRADO DE VERNAM\n")
    print(" \t[0] Introducir mensaje original.")
    print(" \t[1] Introducir mensaje crifrado.")
    option = input(" \t> ")


#original_m = input("Mensaje a cifrar > ")

#mensaje = stringToBinary(original_m)
#mensaje = binaryToString(original_m)
#print ("MENSAJE = " + mensaje)

#binary_string = "0101001101010011"
#binary_array = list(binary_string)
#print(binary_array)
#ascii_string = ""
#for value in binary_array:
#    integer = int(value,2)
#    ascii_character = chr(integer)
#    ascii_string+= ascii_character

#print(ascii_string)

mensaje = input(" > ")
print(isABinaryString(mensaje))