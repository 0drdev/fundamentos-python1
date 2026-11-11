# Lectura de la cantidad de bloques
blocks = int(input("Ingresa el número de bloques: "))

height = 0
in_layer = 1

# El bucle continúa mientras tengamos suficientes bloques para completar la siguiente capa
while blocks >= in_layer:
    blocks -= in_layer  # Usamos los bloques necesarios para esta capa
    height += 1         # Incrementamos la altura de la pirámide
    in_layer += 1       # La siguiente capa requerirá un bloque más que la actual

print("La altura de la pirámide es:", height)