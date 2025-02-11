print("#1. Variables y Entrada de Datos")
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
print(f"Hola {nombre}, tienes {edad} años.")
#------------------------------------------------
print("#2. Condicionales (if-elif-else)")
calificacion = int(input("Ingresa tu calificación: "))
if calificacion >= 60:
    print("Felicidades, aprobaste.")
else:
    print("Lo siento, reprobaste.")
#------------------------------------------------
print("#3. Listas y Bucles (for)")
frutas = ["Manzana", "Banana", "Cereza", "Naranja"]
for fruta in frutas:
    print(fruta)
#------------------------------------------------
print("#4. Diccionarios y Búsqueda")
capitales = {
    "México": "Ciudad de México",
    "España": "Madrid",
    "Argentina": "Buenos Aires"
}
pais = input("Ingresa un país: ")
print(f"La capital de {pais} es {capitales.get(pais, 'No encontrada')}.")
#------------------------------------------------
print("#5. Funciones en Python")
def suma(a, b):
    return a + b
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print(f"La suma es: {suma(num1, num2)}")
#------------------------------------------------
print("#6. POO (Clases y Objetos)")
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
p1 = Persona("Carlos", 30)
p1.saludar()
#------------------------------------------------
print("#7. Manejo de Archivos (open)")
with open("datos.txt", "w") as archivo:
    archivo.write("Aprendiendo Python con Django")
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
#------------------------------------------------
print("#8. Generar una Lista con range() y Filtrar Números Pares")
numeros = list(range(1, 21))
pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", pares)
#------------------------------------------------
print("#9. Uso de try-except para Manejo de Errores")
try:
    numero = int(input("Ingresa un número: "))
    print(f"Ingresaste el número {numero}")
except ValueError:
    print("Error: Debes ingresar un número válido.")
#------------------------------------------------
print("#10. Uso de Módulos (import)")
import math
num = float(input("Ingresa un número: "))
print(f"La raíz cuadrada es: {math.sqrt(num)}")