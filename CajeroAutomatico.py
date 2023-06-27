#Cajero automatico

import os
os.system("cls")

print ("Bienvenido al Banco de Costa Rica")
print ("\n")

usuario = str(input("Por favor digite su nombre de usuario: "))

if usuario == "fernando":

    print ("Usuario correcto.")
    print ("\n")

    contra = str(input("Por favor digite su contraseña: "))

    if contra == "secreto":

        print ("Acceso permitido. Bienvenido al sistema.")
    
    else:
        
        while contra != "secreto":

            contra = input("Contraseña incorrecta, digitela de nuevo: ")
        
        if contra == "secreto":

            print ("Acceso permitido. Bienvenido al sistemas.")

else:
    
    while usuario != "fernando":

        usuario = input("Usuario incorrecto, por favor intente de nuevo: ")
    
    if usuario == "fernando":

        print ("Usuario correcto.")

        contra = str(input("Por favor digite su contraseña: "))

        while contra == "secreto":
            
            print ("Acceso permitido. Bienvenido al sistema.")


print ("\n")

saldo = 10000 #este monto puede ser cualquiera, coloqué ₡10,000 para empezar

print ("|MENU DE INICIO|")
print ("\n")
print ("1. Depositar dinero a la cuenta")
print ("2. Retirar dinero de la cuenta")
print ("3. Ver saldo disponible")
print ("4. Salir")    

print ("\n")

opcion = int(input("Digite la opcion que desea realizar: "))

if opcion == 1:

    monto = float(input("Digite el monto que desea ingresar -> "))
    saldo += monto
    print ("Dinero en la cuenta: ₡",saldo)

elif opcion == 2:

    retiro = float(input("Digite el monto que desea retirar -> "))

    if retiro > saldo:

        print ("Transacción no disponible. Su cuenta no dispone con la cantidad ingresada.")
    
    else:
        saldo -= retiro
        print ("Dinero en la cuenta: ₡",saldo)

elif opcion == 3:

    print ("Dinero en la cuenta: ₡",saldo)

elif opcion == 4: 

    print ("Gracias por confiar en nostros. ¡Lindo dia!")

else:

    print ("Error. Ha digitado una opcion que no existe.")




