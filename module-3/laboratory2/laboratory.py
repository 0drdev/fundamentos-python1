# Capturamos el ingreso anual del usuario
income = float(input("Introduce el ingreso anual: "))

# Si ingreso es menor o igual a 85528, se aplica la tasa del 18% menos 552.02
if income <= 85528:
    # Calculamos el impuesto usando la fórmula proporcionada
    impuesto = income * 0.18 - 552.02
# Si ingreso es mayor a 85528, se calcula el impuesto sobre el excedente
else:
    # Calculamos el excedente sobre 85528
    excedente = income - 85528
    # Calculamos el impuesto usando la fórmula proporcionada para ingresos mayores a 85528
    impuesto = 14839.02 + (excedente * 0.32)  # Se calcula el impuesto sobre el excedente
# Aseguramos que el impuesto no sea negativo    
if impuesto < 0:
    impuesto = 0.0

# Redondeamos el impuesto a 0 decimales
impuesto = round(impuesto, 0)
print("El impuesto es:", impuesto, "pesos")
