word_without_vowels = ""

# Pedir al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra a mayúsculas
user_word = user_word.upper()

for letter in user_word:
  # Si la letra es una vocal, la omitimos con continue
  if letter == "A":
    continue
  elif letter == "E":
    continue
  elif letter == "I":
    continue
  elif letter == "O":
    continue
  elif letter == "U":
    continue
  else:
    # Concatenar la letra no consumida a la cadena vacía
    word_without_vowels += letter

# Imprimir la palabra resultante en una sola línea fuera del bucle
print(word_without_vowels)
