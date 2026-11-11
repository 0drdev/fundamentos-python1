# Pedir al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra a mayúsculas
user_word = user_word.upper()

# Recorrer cada letra de la palabra con un bucle for
for letter in user_word:
  # Comprobar si la letra es una vocal
  if letter == 'A':
    continue
  elif letter == 'E':
    continue
  elif letter == 'I':
    continue
  elif letter == 'O':
    continue
  elif letter == 'U':
    continue
  else:
    # Imprimir las letras que no son vocales, cada una en una línea
    print(letter)
