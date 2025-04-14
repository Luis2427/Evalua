# Objetivo: Evaluacion Parcial
# Nombre: COBEÑAS BLANCO, Victor Luis
# Fecha: 13/04/2025

while(True): 
    menu =  int(input("""
    ====== MENU DE OPCIONES ====== 
    1. AUTENTICARSE
    2. REGISTRAR DONACIONES
    3. CALCULADORA
    4. REPORTE TOTAL
    5. SALIR DEL PROGRAMA                                   
    """))
    if(menu == 1):
        while(True):
            dato = "COBEÑAS BLANCO VICTOR LUIS"
            dato = str(input("Ingresar Usuario: "))
            contraseña = "75006556"
            varIngresa = str(input("Ingrese contraseña: "))
            if(varIngresa == contraseña):
                print("Bienvenido")
            else:
                print("ERROR INGRESAR USUARIO Y CONTRASEÑA")
            break
    while(True):
        menu = int(input("""
        \t====== MENU DE OPCIONES ====== 
        2. REGISTRAR DONACIONES
        3. CALCULADORA
        4. REPORTE TOTAL
        5. SALIR DEL PROGRAMA                                   
        """))
        if(menu == 2):
            while(True):
                opcionIngresado = str(input("Ingrese la seccion (A) (B) (C) (D): "))
                cantEstu = int(input("Ingresar cantidad de Alumnos: "))
                if(cantEstu > 0):
                    print("Digite la siguiente opcion")
                else:
                    print("Ingrese numeros positivos")
                break
            while(True):
                datEstu = str(input("Ingrese datos del estudiante: "))
                dni = str(input("Ingrese DNI del estudiante: "))
                opcionGen = str(input("Ingrese Genero (M) (F): "))
                lentes= str(input("Usa lentes "))