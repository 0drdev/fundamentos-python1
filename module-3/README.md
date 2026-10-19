# Valores booleanos, ejecución condicional, bucles, listas y su procesamiento, operadores lógicos y de bit a bit

## Preguntas y respuestas

Un programador escribe un programa y el programa hace preguntas.

Una computadora ejecuta el programa y proporciona las respuestas. El programa debe ser capaz de reaccionar de acuerdo con las respuestas recibidas.

Afortunadamente, las computadoras solo conocen dos tipos de respuestas:

- Si, es cierto.
- No, esto es falso.
  Nunca obtendrás una respuesta como Déjame pensar..., no lo sé, o probablemente sí, pero no lo sé con seguridad.

Para hacer preguntas, Python utiliza un conjunto de operadores muy especiales. Revisemos uno tras otro, ilustrando sus efectos en algunos ejemplos simples.

## Comparación: operador de igualdad

Pregunta: ¿Son dos valores iguales?

Para hacer esta pregunta, se utiliza el == operador (igual igual).

No olvides esta importante distinción:

- = es un operador de asignación, por ejemplo, a = b assigna a la varable a el valor de b.
- == es una pregunta ¿Son estos valores iguales? así que a == b compara a y b.
  Es un operador binario con enlazado del lado izquierdo. Necesita dos argumentos y verifica si son iguales.

## Igualdad: El operador igual a (==)

El operador == (igual a) compara los valores de dos operandos. Si son iguales, el resultado de la comparación es True. Si no son iguales, el resultado de la comparación es False.

Observa la comparación de igualdad a continuación: ¿Cuál es el resultado de esta operación?

`var == 0`

Toma en cuenta que no podemos encontrar la respuesta si no sabemos qué valor está almacenado actualmente en la variable var.

Si la variable se ha cambiado muchas veces durante la ejecución del programa, o si se ingresa su valor inicial desde la consola, Python solo puede responder a esta pregunta en el tiempo de ejecución del programa.

Ahora imagina a un programador que sufre de insomnio, y tiene que contar las ovejas negras y blancas por separado siempre y cuando haya exactamente el doble de ovejas negras que de las blancas.

La pregunta será la siguiente:

`black_sheep == 2 * white_sheep`

Debido a la baja prioridad del operador ==, la pregunta será tratada como la siguiente:

`black_sheep == (2 * white_sheep)`

Entonces, vamos a practicar la comprensión del operador == - ¿Puedes adivinar la salida del código a continuación?

```python
var = 0   # asignando 0 a var
print(var == 0)

var = 1  # asignando 1 a var
print(var == 0)
```

## Desigualdad: el operador no es igual a (!=)

El operador != (no es igual a) también compara los valores de dos operandos. Aquí está la diferencia: si son iguales, el resultado de la comparación es False. Si no son iguales, el resultado de la comparación es True.

Ahora echa un vistazo a la comparación de desigualdad a continuación: ¿Puedes adivinar el resultado de esta operación?

```python
var = 0 # asignando 0 a var
print(var != 0)

var = 1 # asignando 1 a var
print(var != 0)
```

Ejecuta el código y comprueba si tenías razón.

## Operadores de comparación: mayor que

También se puede hacer una pregunta de comparación usando el operador > (mayor que).

Si deseas saber si hay más ovejas negras que blancas, puedes escribirlo de la siguiente manera:

`black_sheep > white_sheep  # mayor que`

True lo confirma; False lo niega.

## Operadores de comparación: mayor o igual que

El operador mayor que tiene otra variante especial, una variante no estricta, pero se denota de manera diferente que la notación aritmética clásica: >= (mayor o igual que).

Hay dos signos subsecuentes, no uno.

Ambos operadores (estrictos y no estrictos), así como los otros dos que se analizan en la siguiente sección, son operadores binarios con enlace del lado izquierdo, y su prioridad es mayor que la mostrada por == y !=.

Si queremos saber si tenemos que usar un gorro o no, nos hacemos la siguiente pregunta:

`centigrade_outside ≥ 0.0  # mayor o igual que`

## Operadores de comparación: menor o igual que

Como probablemente ya hayas adivinado, los operadores utilizados en este caso son: El operador < (menor que) y su hermano no estricto: <= (menor o igual que).

Observa este ejemplo simple:

```python
current_velocity_mph < 85  # Menor que
current_velocity_mph ≤ 85  # Menor o igual que
```

Vamos a comprobar si existe un riesgo de ser multados por la ley (la primera pregunta es estricta, la segunda no).

Existen al menos dos posibilidades: primero, puedes memorizarlo (almacenarlo en una variable) y utilizarlo más tarde. ¿Cómo haces eso? Bueno, utilizarías una variable arbitraria como esta:

`answer = number_of_lions >= number_of_lionesses`

El contenido de la variable te dirá la respuesta a la pregunta.

La segunda posibilidad es más conveniente y mucho más común: puedes utilizar la respuesta que obtengas para tomar una decisión sobre el futuro del programa.

Necesitas una instrucción especial para este propósito, y la discutiremos muy pronto.

Ahora necesitamos actualizar nuestra tabla de prioridades, y poner todos los nuevos operadores en ella. Ahora se ve como a continuación:

## Condiciones y ejecución condicional

Ya sabes como hacer preguntas a Python, pero aún no sabes como hacer un uso razonable de las respuestas. Se debe tener un mecanismo que le permita hacer algo si se cumple una condición, y no hacerlo si no se cumple.

Es como en la vida real: haces ciertas cosas o no cuando se cumple una condición específica, por ejemplo, sales a caminar si el clima es bueno, o te quedas en casa si está húmedo y frío.

Para tomar tales decisiones, Python ofrece una instrucción especial. Debido a su naturaleza y su aplicación, se denomina instrucción condicional (o sentencia condicional).

Existen varias variantes de la misma. Comenzaremos con la más simple, aumentando la dificultad lentamente.

La primera forma de una sentencia condicional, que puede ver a continuación, está escrita de manera muy informal pero figurada:

```python
if true_or_not:
    do_this_if_true
```

Esta sentencia condicional consta de los siguientes elementos, estrictamente necesarios en este orden:

- La palabra clave reservada if.
- Uno o más espacios en blanco.
- Una expresión (una pregunta o una respuesta) cuyo valor se interpretar únicamente en términos de True (cuando su valor no sea cero) y False (cuando sea igual a cero).
- Unos dos puntos seguido de una nueva línea.
- Una instrucción con sangría o un conjunto de instrucciones (se requiere absolutamente al menos una instrucción); la sangría se puede lograr de dos maneras: insertando un número particular de espacios (la recomendación es usar cuatro espacios de sangría), o usando el tabulador; nota: si hay mas de una instrucción en la parte con sangría, la sangría debe ser la misma en todas las líneas; aunque puede parecer lo mismo si se mezclan tabuladores con espacios, es importante que todas las sangrías sean exactamente iguales Python 3 no permite mezclar espacios y tabuladores para la sangría.

¿Cómo funciona esta sentencia?

- Si la expresión true_or_not representa la verdad (es decir, su valor no es igual a cero), las sentencias con sangría se ejecutarán.
- Si la expresión true_or_not no representa la verdad (es decir, su valor es igual a cero), las sentencias con sangría se omitirán , y la siguiente instrucción ejecutada será la siguiente al nivel de la sangría original.

En la vida real, a menudo expresamos un deseo:

si el clima es bueno, saldremos a caminar

después, almorzaremos

Como puedes ver, almorzar no es una actividad condicional y no depende del clima.

Sabiendo que condiciones influyen en nuestro comportamiento y asumiendo que tenemos las funciones sin parámetros go_for_a_walk() y have_lunch(), podemos escribir el siguiente fragmento de código:

```python
if the_weather_is_good:
    go_for_a_walk()
have_lunch()
```

## Ejecución condicional: la sentencia if

Si un determinado desarrollador de Python sin dormir se queda dormido cuando cuenta 120 ovejas, y el procedimiento de inducción del sueño se puede implementar como una función especial llamada `sleep_and_dream()`, el código toma la siguiente forma:

```python
if sheep_counter >= 120: # #evalúa una expresión condicional
    sleep_and_dream() #se ejecuta si la expresión condicional es True
```

Puedes leerlo como sigue: si sheep_counter es mayor o igual que 120, entonces duerme y sueña (es decir, ejecuta la función sleep_and_dream).

Hemos dicho que las sentencias condicionales deben tener sangría. Esto crea una estructura muy legible, demostrando claramente todas las rutas de ejecución posibles en el código.

Analiza el siguiente código:

```python
if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
feed_the_sheepdogs()
```

Como puedes ver, tender la cama, tomar una ducha y dormir y soñar se ejecutan condicionalmente, cuando sheep_counter alcanza el límite deseado.

Alimentar a los perros, sin embargo, siempre se hace (es decir, la función feed_the_sheepdogs() no tiene sangría y no pertenece al bloque if, lo que significa que siempre se ejecuta).

Ahora vamos a discutir otra variante de la sentencia condicional, que también permite realizar una acción adicional cuando no se cumple la condición.

## Ejecución condicional: la sentencia if-else

Comenzamos con una frase simple que decía: Si el clima es bueno, saldremos a caminar.

Nota: no hay una palabra sobre lo que sucederá si el clima es malo. Solo sabemos que no saldremos al aire libre, pero no sabemos que podríamos hacer. Es posible que también queramos planificar algo en caso de mal tiempo.

Podemos decir, por ejemplo: Si el clima es bueno, saldremos a caminar, de lo contrario, iremos al cine.

Ahora sabemos lo que haremos si se cumplen las condiciones, y sabemos lo que haremos si no todo sale como queremos. En otras palabras, tenemos un "Plan B".

Python nos permite expresar dichos planes alternativos. Esto se hace con una segunda forma, ligeramente mas compleja, de la sentencia condicional, la sentencia if-else:

```python
if true_or_false_condition:
    perform_if_condition_true
else:
    perform_if_condition_false
```

Por lo tanto, hay una nueva palabra: else - esta es una palabra clave reservada.

La parte del código que comienza con else dice que hacer si no se cumple la condición especificada por el if (observa los dos puntos después de la palabra).

La ejecución de if-else es la siguiente:

- Si la condición se evalúa como True (su valor no es igual a cero), la instrucción perform_if_condition_true se ejecuta, y la sentencia condicional llega a su fin.
- Si la condición se evalúa como False (es igual a cero), la instrucción perform_if_condition_false se ejecuta, y la sentencia condicional llega a su fin.

## La sentencia if-else: más sobre ejecución condicional

Al utilizar esta forma de sentencia condicional, podemos describir nuestros planes de la siguiente manera:

```python
if the_weather_is_good:
    go_for_a_walk()
else:
    go_to_a_theater()
have_lunch()
```

Si el clima es bueno, saldremos a caminar. De lo contrario, iremos al cine. No importa si el clima es bueno o malo, almorzaremos después (después de la caminata o después de ir al cine).

Todo lo que hemos dicho sobre la sangría funciona de la misma manera dentro de la rama else :

```python
if the_weather_is_good:
    go_for_a_walk()
    have_fun()
else:
    go_to_a_theater()
    enjoy_the_movie()
have_lunch()
```

## Sentencias if-else anidadas

Ahora, analicemos dos casos especiales de la sentencia condicional.

Primero, considera el caso donde la instrucción colocada después del if es otro if.

Lee lo que hemos planeado para este Domingo. Si hay buen clima, saldremos a caminar. Si encontramos un buen restaurante, almorzaremos allí. De lo contrario, vamos a comer un sandwich. Si hay mal clima, iremos al cine. Si no hay boletos, iremos de compras al centro comercial más cercano.

Escribamos lo mismo en Python. Considera cuidadosamente el código siguiente:

```python
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()
```

elif se usa para verificar más de una condición, y para detener cuando se encuentra la primera sentencia verdadera.

Nuestro siguiente ejemplo se parece a la anidación, pero las similitudes son muy leves. Nuevamente, cambiaremos nuestros planes y los expresaremos de la siguiente manera: si hay buen clima, saldremos a caminar, de lo contrario, si obtenemos entradas, iremos al cine, de lo contrario, si hay mesas libres en el restaurante, vamos a almorzar; si todo falla, regresaremos a casa y jugaremos ajedrez.

¿Has notado cuantas veces hemos usado la palabra de lo contrario? Esta es la etapa en la que la palabra clave reservada elif desempeña su función.

Escribamos el mismo escenario empleando Python:

```python
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

```

La forma de ensamblar las siguientes sentencias if-elif-else a veces se denomina cascada.

Observa de nuevo como la sangría mejora la legibilidad del código.

Se debe prestar atención adicional a este caso:

- No debes usar else sin un if precedente.
- else siempre es la última rama de la cascada, independientemente de si has usado elif o no.
- else es una parte opcional de la cascada, y puede omitirse.
- Si hay una rama else en la cascada, solo se ejecuta una de todas las ramas.
- Si no hay una rama else, es posible que no se ejecute ninguna de las opciones disponibles.

Esto puede sonar un poco desconcertante, pero ojalá que algunos ejemplos simples ayuden a comprenderlo mejor.

## Analizando ejemplos de código

Ahora te mostraremos algunos programas simples pero completos. No los explicaremos a detalle, porque consideramos que los comentarios (y los nombres de las variables) dentro del código son guías suficientes.

Todos los programas resuelven el mismo problema: encuentran el número mayor de una serie de números y lo imprimen.

**Ejemplo 1:**

Comenzaremos con el caso más simple: ¿Cómo identificar el mayor de los dos números?

```python
#Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)
```

El fragmento de código anterior debe estar claro: lee dos valores enteros, los compara y encuentra cuál es el más grande.

**Ejemplo 2:**

Ahora vamos a mostrarte un hecho intrigante. Python tiene una característica interesante, mira el código a continuación:

```python
#Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande

if number1 > number2: larger_number = number1
else: larger_number = number2

# Imprime el resultado

print("El número más grande es:", larger_number)
```

Nota: si alguna de las ramas de if-elif-else contiene una sola instrucción, puedes codificarla de forma más completa (no es necesario que aparezca una línea con sangría después de la palabra clave), pero solo continúa la línea después de los dos puntos.

Sin embargo, este estilo puede ser engañoso, y no lo vamos a usar en nuestros programas futuros, pero definitivamente vale la pena saber si quieres leer y entender los programas de otra persona.

No hay otras diferencias en el código.

**Ejemplo 3:**

Es hora de complicar el código: encontremos el mayor de los tres números. ¿Se ampliará el código? Un poco.

Suponemos que el primer valor es el más grande. Luego verificamos esta hipótesis con los dos valores restantes.

Observa el siguiente código:

```python
# Se leen tres números

number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número

# es el más grande.

# Lo verificaremos pronto.

largest_number = number1

# Comprobamos si el segundo número es más grande que el mayor número actual

# y actualiza el número más grande si es necesario.

if number2 > largest_number:
largest_number = number2

# Comprobamos si el tercer número es más grande que el mayor número actual

# y actualiza el número más grande si es necesario.

if number3 > largest_number:
largest_number = number3

# Imprime el resultado.

print("El número más grande es:", largest_number)
```

Este método es significativamente más simple que tratar de encontrar el número más grande comparando todos los pares de números posibles (es decir, el primero con el segundo, el segundo con el tercero y el tercero con el primero). Intenta reconstruir el código por ti mismo.

## Pseudocódigo e introducción a los bucles (ciclos)

Ahora deberías poder escribir un programa que encuentre el mayor de cuatro, cinco, seis o incluso diez números.

Ya conoces el esquema, por lo que ampliar el tamaño del problema no será particularmente complejo.

¿Pero qué sucede si te pedimos que escribas un programa que encuentre el mayor de doscientos números? ¿Te imaginas el código?

Necesitarás doscientas variables. Si doscientas variables no son lo suficientemente complicadas, intenta imaginar la búsqueda del número más grande de un millón.

Imagina un código que contiene 199 sentencias condicionales y doscientas invocaciones de la función input(). Por suerte, no necesitas lidiar con eso. Hay un enfoque más simple.

Por ahora ignoraremos los requisitos de la sintaxis de Python e intentaremos analizar el problema sin pensar en la programación real. En otras palabras, intentaremos escribir el algoritmo, y cuando estemos contentos con él, lo implementaremos.

En este caso, utilizaremos un tipo de notación que no es un lenguaje de programación real (no se puede compilar ni ejecutar), pero está formalizado, es conciso y se puede leer. Se llama pseudocódigo.

Veamos nuestro pseudocódigo a continuación:

```python
largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Ir a la línea 02
```

¿Qué está pasando en él?

En primer lugar, podemos simplificar el programa si, al principio del código, le asignamos a la variable largest_number un valor que será más pequeño que cualquiera de los números ingresados. Usaremos -999999999 para ese propósito.

En segundo lugar, asumimos que nuestro algoritmo no sabrá por adelantado cuántos números se entregarán al programa. Esperamos que el usuario ingrese todos los números que desee; el algoritmo funcionará bien con cien y con mil números. ¿Cómo hacemos eso?

Hacemos un trato con el usuario: cuando se ingresa el valor-1, será una señal de que no hay más datos y que el programa debe finalizar su trabajo.

De lo contrario, si el valor ingresado no es igual a -1, el programa leerá otro número, y así sucesivamente.

El truco se basa en la suposición de que cualquier parte del código se puede realizar más de una vez, precisamente, tantas veces como sea necesario.

La ejecución de una determinada parte del código más de una vez se denomina bucle. El significado de este término es probablemente obvio para ti.

Las líneas 02 a 08 forman un bucle. Los pasaremos tantas veces como sea necesario para revisar todos los valores ingresados.

¿Puedes usar una estructura similar en un programa escrito en Python? Si, si puedes.

**Información Adicional**

Python a menudo viene con muchas funciones integradas que harán el trabajo por ti. Por ejemplo, para encontrar el número más grande de todos, puede usar una función incorporada de Python llamada max(). Puedes usarlo con múltiples argumentos. Analiza el código de abajo:

```python
# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number

largest_number = max(number1, number2, number3)

# Imprime el resultado.
print("El número más grande es:", largest_number)
```

De la misma manera, puedes usar la función min() para devolver el número más pequeño. Puedes reconstruir el código anterior y experimentar con él en Sandbox.

Vamos a hablar sobre estas (y muchas otras) funciones pronto. Por el momento, nuestro enfoque se centrará en la ejecución condicional y los bucles para permitirte ganar más confianza en la programación y enseñarte las habilidades que te permitirán comprender y aplicar los dos conceptos en tu codigo. Entonces, por ahora, no estamos tomando atajos.

## Puntos Clave

1. Los operadores de comparación (o también denominados operadores relacionales) se utilizan para comparar valores. La siguiente tabla ilustra cómo funcionan los operadores de comparación, asumiendo que x=0, y=1 y z=0:

| Operador | Descripción                                                                                                                       | Ejemplo                                                   |
| -------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `==`     | Devuelve `True` si los valores de los operandos son iguales, y `False` de lo contrario.                                           | `x == y  # False`<br>`x == z  # True`                     |
| `!=`     | Devuelve `True` si los valores de los operandos no son iguales, y `False` de lo contrario.                                        | `x != y  # True`<br>`x != z  # False`                     |
| `>`      | Devuelve `True` si el valor del operando izquierdo es mayor que el valor del operando derecho, y `False` de lo contrario.         | `x > y  # False`<br>`y > z  # True`                       |
| `<`      | Devuelve `True` si el valor del operando izquierdo es menor que el valor del operando derecho, y `False` de lo contrario.         | `x < y  # True`<br>`y < z  # False`                       |
| `>=`     | Devuelve `True` si el valor del operando izquierdo es mayor o igual que el valor del operando derecho, y `False` de lo contrario. | `x >= y  # False`<br>`x >= z  # True`<br>`y >= z  # True` |
| `<=`     | Devuelve `True` si el valor del operando izquierdo es menor o igual que el valor del operando derecho, y `False` de lo contrario. | `x <= y  # True`<br>`x <= z  # True`<br>`y <= z  # False` |

2. Cuando deseas ejecutar algún código solo si se cumple una determinada condición, puedes usar una sentencia condicional:

Una única sentencia if, por ejemplo:

```
x = 10

if x == 10: # condición
print("x es igual a 10") # Ejecutado si la condición es Verdadera.
```

Una serie de sentencias if, por ejemplo:

x = 10

if x > 5: # primera condición
print("x es mayor que 5") # Ejecutado si la primera condición es Verdadera.

if x < 10: # segunda condición
print("x is less than 10") # Ejecutado si la segunda condición es Verdadera.

if x == 10: # tercera condición
print("x is equal to 10") # Ejecutado si la tercera condición es Verdadera.

```
x = 10

if x > 5: # primera condición
    print("x es mayor que 5")  # Ejecutado si la primera condición es Verdadera.

if x < 10: # segunda condición
    print("x is less than 10")  # Ejecutado si la segunda condición es Verdadera.

if x == 10: # tercera condición
    print("x is equal to 10")  # Ejecutado si la tercera condición es Verdadera.

```

- Cada sentencia if se prueba por separado.

- Cada sentencia if se prueba por separado.

```
x = 10

if x < 10:  # Condición
    print("x es menor que 10")  # Ejecutado si la condición es Verdadera.

else:
    print("x es mayor o igual a 10")  # Ejecutado si la condición es Falsa.

```

- Una serie de sentencias if seguidas de un else, por ejemplo:

```
x = 10

if x > 5:  # True
    print("x > 5")

if x > 8:  # True
    print("x > 8")

if x > 10:  # False
    print("x > 10")

else:
    print("se ejecutará el else")

```

Cada if se prueba por separado. El cuerpo de else se ejecuta si el último if es False.

- La sentencia if-elif-else, por ejemplo:

```
x = 10

if x == 10:  # True
    print("x == 10")

if x > 15:  # False
    print("x > 15")

elif x > 10:  # False
    print("x > 10")

elif x > 5:  # True
    print("x > 5")

else:
    print("else no será ejecutado")

```

Si la condición para if es False, el programa verifica las condiciones de los bloques elif posteriores: el primer elif que sea True es el que se ejecuta. Si todas las condiciones son False, se ejecutará el bloque else.

- Sentencias condicionales anidadas, ejemplo:

```
x = 10

if x > 5:  # True
    if x == 6:  # False
        print("anidado: x == 6")
    elif x == 10:  # True
        print("anidado: x == 10")
    else:
        print("anidado: else")
else:
    print("else")
```

## Bucles (ciclos) en el código con while

¿Estás de acuerdo con la sentencia presentada a continuación?

```
mientras haya algo que hacer
    hazlo
```

Toma en cuenta que este registro también declara que, si no hay nada que hacer, nada ocurrirá.

En general, en Python, un bucle se puede representar de la siguiente manera:

```
while conditional_expression:
    instruction
```

Si observas algunas similitudes con la instrucción if, está bien. De hecho, la diferencia sintáctica es solo una: usa la palabra while en lugar de la palabra if.

La diferencia semántica es más importante: cuando se cumple la condición, if realiza sus sentencias sólo una vez; while repite la ejecución siempre que la condición se evalúe como True.

Nota: todas las reglas relacionadas con sangría también se aplican aquí. Te mostraremos esto pronto.

Observa el algoritmo a continuación:

```
while conditional_expression:
    instruction_one
    instruction_two
    instruction_three
    :
    :
    instruction_n
```

Ahora, es importante recordar que:

- Si deseas ejecutar más de una sentencia dentro de un while, debes (como con if) poner sangría a todas las instrucciones de la misma manera.
- Una instrucción o conjunto de instrucciones ejecutadas dentro del while se llama el cuerpo del bucle.
  Si la condición es False (igual a cero) tan pronto como se compruebe por primera vez, el cuerpo no se ejecuta ni una sola vez (ten en cuenta la analogía de no tener que hacer nada si no hay nada que hacer).
- El cuerpo debe poder cambiar el valor de la condición, porque si la condición es True al principio, el cuerpo podría funcionar continuamente hasta el infinito. Observa que hacer una cosa generalmente disminuye la cantidad de cosas por hacer.

## Un bucle infinito

Un bucle infinito, también denominado bucle sin fin, es una secuencia de instrucciones en un programa que se repite indefinidamente (bucle sin fin).

Este es un ejemplo de un bucle que no puede finalizar su ejecución:

```python
while True:
    print("Estoy atrapado dentro de un bucle.")
```

`Este bucle imprimirá infinitamente "Estoy atrapado dentro de un bucle". En la pantalla.`

### NOTA

Si deseas obtener la mejor experiencia de aprendizaje al ver cómo se comporta un bucle infinito, inicia IDLE, crea un nuevo archivo, copia y pega el código anterior, guarda tu archivo y ejecuta el programa. Lo que verás es la secuencia interminable de cadenas impresas de "Estoy atrapado dentro de un bucle". en la ventana de la consola de Python. Para finalizar tu programa, simplemente presiona Ctrl-C (o Ctrl-Break en algunas computadoras). Esto provocará la excepción KeyboardInterrupt y permitirá que tu programa salga del bucle. Hablaremos de ello más adelante en el curso.

Volvamos al bosquejo del algoritmo que te mostramos recientemente. Te mostraremos como usar este bucle recién aprendido para encontrar el número más grande de un gran conjunto de datos ingresados.

Analiza el programa cuidadosamente. Localiza donde comienza el bucle (línea 8) y descubre como se sale del cuerpo del bucle:

```python
# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande
print("El número más grande es:", largest_number)

```

Comprueba como este código implementa el algoritmo que te mostramos anteriormente.

## El bucle while: más ejemplos

Veamos otro ejemplo utilizando el bucle while. Sigue los comentarios para descubrir la idea y la solución.

```python
# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Cuenta de números impares:", odd_numbers)
print("Cuenta de números pares:", even_numbers)
```

¿Es más compacto que antes? Un poco. ¿Es más legible? Eso es discutible.

### RECUERDA

No te sientas obligado a codificar tus programas de una manera que siempre sea la más corta y la más compacta. La legibilidad puede ser un factor más importante. Manten tu código listo para un nuevo programador.

## Bucles en tu código con for

Otro tipo de bucle disponible en Python proviene de la observación de que a veces es más importante contar los "giros o vueltas" del bucle que verificar las condiciones.

Imagina que el cuerpo de un bucle debe ejecutarse exactamente cien veces. Si deseas utilizar el bucle while para hacerlo, puede tener este aspecto:

```python
i = 0
while i < 100:
    # do_something()
    i += 1
```

Sería bueno si alguien pudiera hacer esta cuenta aburrida por ti. ¿Es eso posible?

Por supuesto que lo es, hay un bucle especial para este tipo de tareas, y se llama for.

En realidad, el bucle for está diseñado para realizar tareas más complicadas, puede "explorar" grandes colecciones de datos elemento por elemento. Te mostraremos como hacerlo pronto, pero ahora presentaremos una variante más sencilla de su aplicación.

Echa un vistazo al fragmento:

```python
for i in range(100):
    # do_something()
    pass
```

Existen algunos elementos nuevos. Déjanos contarte sobre ellos:

- La palabra reservada for abre el bucle for; nota - No hay condición después de eso; no tienes que pensar en las condiciones, ya que se verifican internamente, sin ninguna intervención.
  Cualquier variable después de la palabra reservada for es la variable de control del bucle; cuenta los giros del bucle y lo hace automáticamente.

- La palabra reservada in introduce un elemento de sintaxis que describe el rango de valores posibles que se asignan a la variable de control.

- La función range() (esta es una función muy especial) es responsable de generar todos los valores deseados de la variable de control; en nuestro ejemplo, la función creará (incluso podemos decir que alimentará el bucle con) valores subsiguientes del siguiente conjunto: 0, 1, 2 .. 97, 98, 99; nota: en este caso, la función range() comienza su trabajo desde 0 y lo finaliza un paso (un número entero) antes del valor de su argumento.

- Nota la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una instrucción vacía : la colocamos aquí porque la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo (por cierto, if, elif, else y while expresan lo mismo).
  Nuestros próximos ejemplos serán un poco más modestos en el número de repeticiones de bucle.

Echa un vistazo al fragmento de abajo. ¿Puedes predecir su salida?

```python
for i in range(10):
    print("El valor de i es actualmente", i)
```

Ejecuta el código para verificar si tenias razón.

Nota:

- El bucle se ha ejecutado diez veces (es el argumento de la función range()).
- El valor de la última variable de control es 9 (no 10, ya que comienza desde 0 , no desde 1).

La invocación de la función range() puede estar equipada con dos argumentos, no solo uno:

```python
for i in range(2, 8):
    print("El valor de i es actualmente", i)
```

En este caso, el primer argumento determina el valor inicial (primero) de la variable de control.

El último argumento muestra el primer valor que no se asignará a la variable de control.

Nota: la función range() solo acepta enteros como argumentos y genera secuencias de enteros.

¿Puedes adivinar la salida del programa? Ejecútalo para comprobar si ahora también estabas en lo cierto.

El primer valor mostrado es 2 (tomado del primer argumento de range()).

El último es 7 (aunque el segundo argumento de range() es 8).

## Más sobre el bucle for y la función range() con tres argumentos

La función range() también puede aceptar tres argumentos: Echa un vistazo al código del editor.

El tercer argumento es un incremento: es un valor agregado para controlar la variable en cada giro del bucle (como puedes sospechar, el valor predeterminado del incremento es 1).

¿Puedes decirnos cuántas líneas aparecerán en la consola y qué valores contendrán?

Ejecuta el programa para averiguar si tenías razón.

Deberías poder ver las siguientes líneas en la ventana de la consola:

```
El valor de i es actualmente 2
El valor de i es actualmente 5
```

¿Sabes por qué? El primer argumento pasado a la función range() nos dice cual es el número de inicio de la secuencia (por lo tanto, 2 en la salida). El segundo argumento le dice a la función dónde detener la secuencia (la función genera números hasta el número indicado por el segundo argumento, pero no lo incluye). Finalmente, el tercer argumento indica el paso, que en realidad significa la diferencia entre cada número en la secuencia de números generados por la función.

2 (número inicial) → 5 (2 incremento por 3 es igual a 5 - el número está dentro del rango de 2 a 8) → 8 (5 incremento por 3 es igual a 8 - el número no está dentro del rango de 2 a 8, porque el parámetro de parada no está incluido en la secuencia de números generados por la función).

Nota: si el conjunto generado por la función range() está vacío, el bucle no ejecutará su cuerpo en absoluto.

Al igual que aquí, no habrá salida:

```python
for i in range(1, 1):
    print("El valor de i es actualmente", i)
```

Nota: el conjunto generado por range() debe ordenarse en un orden ascendente. No hay forma de forzar el range() para crear un conjunto en una forma diferente. Esto significa que el segundo argumento de range() debe ser mayor que el primero.

Por lo tanto, tampoco habrá salida aquí:

```python
for i in range(2, 1):
    print("El valor de i es actualmente", i)
```

Echemos un vistazo a un programa corto cuya tarea es escribir algunas de las primeras potencias de dos:

```python
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2
```

La variable expo se utiliza como una variable de control para el bucle e indica el valor actual del exponente. La propia exponenciación se sustituye multiplicando por dos. Dado que 2 0 es igual a 1, después 2 × 1 es igual a 21, 2 × 21 es igual a 22, y así sucesivamente. ¿Cuál es el máximo exponente para el cual nuestro programa aún imprime el resultado?

Ejecuta el código y verifica si la salida coincide con tus expectativas.
