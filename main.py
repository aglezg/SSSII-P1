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


# Menú principal
def menu():
    print(" PRÁCTICA: CIFRADO DE VERNAM\n")
    print(" \t[0] Introducir mensaje original.")
    print(" \t[1] Introducir mensaje crifrado.")
    option = input(" \t> ")


original_m = input("Mensaje a cifrar > ")

mensaje = stringToBinary(original_m)
print ("MENSAJE = " + mensaje)