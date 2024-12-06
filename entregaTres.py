# calcula el promedio de las notas
"""
def ingresar_datos():
    suma = 0  
    contador = 0  
    
    while True:  
        nota = input("Ingrese una nota positiva (0 para finalizar): ") 

       
        if nota.replace(".", "").isdigit():
            nota = float(nota)  
            if nota > 0:  
                suma += nota
                contador += 1
            elif nota == 0:  
                print("Finalizando el ingreso de notas...")
                break
            else:  
                print("Por favor, ingrese solo notas positivas.")
        else:
            print("Entrada no válida. Ingrese un número válido.")
    
    return suma, contador


def promedio_notas():
   
    if contador == 0:  # Evitar división por cero si no se ingresaron notas
        print("No se ingresaron notas válidas para calcular el promedio.")
    else:
        promedio = suma / contador  # Calcula el promedio
        print(f"Se ingresaron {contador} notas. El promedio es: {round(promedio, 2)}")  
promedio_notas()
"""
# color primario o no 
"""
def ingresar_color():
    return input("Ingrese un color: ")

def es_color_primario(color):
    return color.lower() in ["azul", "rojo", "amarillo"], color

def mostrar_resultado(resultado):
    print(f"El color {resultado[1]} es primario." if resultado[0] else f"El color {resultado[1]} no es primario.")

mostrar_resultado(es_color_primario(ingresar_color()))

"""
# numero mayor 
"""
def ingresar_numeros():
    mayor = None
    while True:
        numero = input("Ingrese un número (o una letra para finalizar): ")
        
        # Verificar si el usuario ingresó un número
        if numero.replace(".", "").isdigit():
            numero = float(numero)
            if mayor is None or numero > mayor:
                mayor = numero  
        else:
            print("Finalizando el ingreso de datos.")
            break 

    return mayor

def numero_mayor():
    mayor = ingresar_numeros()  # Llamar a la función para obtener el número mayor
    if mayor is None:
        print("No ingresó ningún número válido.")  
    else:
        print(f"El número mayor ingresado es: {mayor}")  

numero_mayor()
"""

#rectangulo 

"""
def ingresar_datos():
    while True:
        alto = input("Ingrese Alto (Solo números enteros): ")
        if alto.isdigit():
            alto = int(alto)
            while True:
                ancho = input("Ingrese Ancho (Solo números enteros y diferente del Alto): ")
                if ancho.isdigit():
                    ancho = int(ancho)
                    if alto != ancho:
                        return alto, ancho
                    else:
                        print("El alto y el ancho no pueden ser iguales.")
                else:
                    print("Valor no válido.")
        else:
            print("Valor no válido.")

def dibujar_rectangulo(valores):
    for _ in range(valores[0]):
        print("*" * valores[1])

dibujar_rectangulo(ingresar_datos())

"""

#factorial positivo

"""
def ingresar_datos():
    while True:
        n = input("Ingrese un número (solo números enteros positivos): ")
        if n.isdigit():
            n = int(n)
            if n > 0:
                return n
            else:
                print("El número debe ser positivo.")
        else:
            print("Valor no válido.")

def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de {n} es: {factorial}")

calcular_factorial(ingresar_datos())

"""