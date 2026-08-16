# ingresa un valor flotante para la variable x aquí
x = 1
x = float(x)

# evalúa la fracción continua y asígnala a la variable y
# y = 1 / (x + 1/(x + 1/(x + 1/x)))
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))

print("x =", x)
print("y =", y)
