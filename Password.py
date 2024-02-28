#Crear una password random

#Importamos la libreria 'random'
import random 

#Creamos una funcion haciendo uso de la variable 'longitud'
def generar_contraseña(longitud):

    #Creamos una variable que contenga todos los posibles caracteres
    caracteres = "abcdefghijklmnñopqrstuvxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789.+-*/,.-{}´+¿'|;:_[]*¨¡?=)(/&%$#!°"

    #Creamos una variable que tomara aleatoriamente la cantidad de caracteres que especificamos
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

    #Regresamos la variable 'contraseña' con el valor
    return contraseña

#Creamos la variable que pedira al usuario introducir la 'longitud' de la contraseña
longitud = int(input('Ingresa la longitud de la contraseña: '))

#Ejecutamos la funcion 
contraseña = generar_contraseña(longitud)

#Finalmente imprimimos la contraseña generada
print('La contraseña generada es: ', contraseña)
