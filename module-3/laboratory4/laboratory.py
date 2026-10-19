secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

# 1. Definimos el número secreto escogido por el mago
numero_secreto = 777

# 2. Pedimos al usuario que ingrese un número entero por primera vez
numero_usuario = int(input("Ingresa un número entero para escapar del bucle: "))

# 3. El bucle while se ejecutará MIENTRAS el número ingresado sea DIFERENTE al secreto
while numero_usuario != numero_secreto:
    # Si entra aquí, significa que falló. Mostramos el mensaje de atrapado.
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    
    # Le solicitamos que ingrese un número nuevamente para actualizar la condición
    numero_usuario = int(input("Inténtalo de nuevo: "))

# 4. Si el programa sale del bucle, significa que los números coinciden
print(numero_usuario)
print("¡Bien hecho, muggle! Eres libre ahora.")
