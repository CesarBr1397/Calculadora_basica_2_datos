#Calcuiladora básica
print("""Bienvenido a la calculadora, tenemos las siguientes operaciones
    1. suma
    2. resta
    3. multiplicacion 
    4. division
    5. potencia""")

while True:
    try:
        operación = int(input("¿Qué operación deseas realizar?: "))
#Suma
        if operación == 1:
            numas1=float(input("Ingrese el primer número: "))
            numas2=float(input("Ingrese el segundo número: "))
            suma = numas1 + numas2
            print(f"El resultado es: {suma}")
#Resta
        elif operación == 2:
            numres1 = float(input("Ingrese el primer número: "))
            numres2 = float(input("Ingrese el segundo número: "))
            resta = numres1 - numres2
            print(f"El resultado es: {resta}")
#Multiplicación
        elif operación == 3:
            mul1 = float(input("Ingrese el primer número: "))
            mul2 = float(input("Ingrese el segundo número: "))
            mult = mul1 * mul2
            print(f"El resultado es: {mult}")
#División
        elif operación == 4:
            divi1 = float(input("Ingrese el dividendo: "))
            divi2 = float(input("Ingrese el divisor: "))
            if divi2==0:
                print("No se puede dividir entre cero.")
            else:
                divi = divi1 / divi2
                print(f"El resultado es: {divi}")
#Potencia
        elif operación == 5:
            base = float(input("Ingrese el valor de la base: "))
            expone = int(input("Ingrese el exponente: "))
            poten = base ** expone
            print(f"El resultado es: {poten}")
#Opciones erroneas al escoger el número de la operación
        else:
            print("Opción incorrecta, vuelva a intentarlo.")
#Excepciones
    except (ValueError, TypeError):
        print("Error en los datos ingresados, intentelo nuevamente.")