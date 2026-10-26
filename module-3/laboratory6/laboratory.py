palabra_secreta = "chupacabra"
while True:
    palabra_usuario = input("Ingrese una palabra: ")
    
    if palabra_usuario == palabra_secreta:
        break

print("¡Has dejado el bucle con éxito!")