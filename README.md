# quiz-ciberseguridad
Quiz de ciberseguridad desarrollado en Python para practicar conceptos de programación como condicionales, listas, bucles y validación de respuestas mediante un juego interactivo de preguntas.

# 🔐 Quiz de Ciberseguridad con Python

## Introducción

### ¿Qué voy a construir?

Voy a desarrollar un pequeño juego de preguntas sobre conceptos de ciberseguridad, en el que el usuario tendrá que responder varias preguntas y obtendrá una puntuación al finalizar.

Con este proyecto voy a practicar conceptos fundamentales de Python, como las variables, los condicionales, las listas, los bucles y las funciones.

Aunque se trata de un proyecto sencillo, permite demostrar competencias reales de programación, como la lógica, la organización del código, la validación de datos, el manejo de errores, las pruebas y la documentación técnica.

## 🎯 Objetivos de aprendizaje

Con este proyecto voy a practicar los siguientes conceptos:

- **Python y variables:** almacenar información como las preguntas, las respuestas y la puntuación.
- **Condicionales (`if`, `elif`, `else`):** tomar decisiones según las respuestas del usuario.
- **Listas y diccionarios:** organizar las preguntas, las opciones y las respuestas correctas.
- **Bucles (`for` y `while`):** recorrer las preguntas y validar las respuestas introducidas.
- **Funciones:** dividir el programa en bloques reutilizables y fáciles de mantener.
- **Entrada y salida de datos:** utilizar `input()` y `print()` para interactuar con el usuario.
- **Fundamentos de ciberseguridad:** aprender conceptos como el phishing, el malware, la autenticación multifactor, las contraseñas seguras y las vulnerabilidades.

## 📚 Recursos de Python antes de programar

### 1. Variables y tipos de datos

Una variable es un nombre que utilizamos para almacenar un valor.

En Python podemos trabajar con distintos tipos de datos:

- `str`: almacena texto.
- `int`: almacena números enteros.
- `bool`: almacena valores booleanos, que pueden ser `True` o `False`.

Por ejemplo:

```python
nombre = "Usuario"
puntuacion = 0
respuesta_correcta = True
```

En el juego utilizaremos variables para almacenar las respuestas del usuario y llevar la cuenta de los puntos obtenidos.

### 2. Condicionales

Los condicionales permiten que un programa tome decisiones en función de una condición.

```python
respuesta = "B"

if respuesta == "B":
    print("¡Respuesta correcta!")
else:
    print("Respuesta incorrecta.")
```

En este ejemplo:

- `if` comprueba si se cumple una condición.
- `==` compara dos valores.
- `else` ejecuta el bloque alternativo cuando la condición no se cumple.
- La indentación determina qué instrucciones pertenecen a cada bloque.

**Importante:** `=` asigna un valor, mientras que `==` compara dos valores.

En el juego, los condicionales decidirán si una respuesta es correcta y si debemos sumar un punto.

**¿Qué pasa si...?**

Cambia la respuesta de `"B"` a `"A"` y comprueba cómo cambia el resultado.

### 3. Listas y diccionarios

Una lista permite almacenar varios elementos ordenados. En Python, los índices empiezan en cero.

```python
preguntas = [
    "¿Qué es el phishing?",
    "¿Qué es el malware?"
]

print(preguntas[0])
```

El resultado será:

```text
¿Qué es el phishing?
```

Un diccionario permite asociar información mediante claves y valores. Es útil para representar una pregunta junto con sus opciones y su respuesta correcta.

```python
pregunta = {
    "enunciado": "¿Qué es el phishing?",
    "opciones": [
        "Un antivirus",
        "Una técnica de engaño",
        "Un sistema operativo"
    ],
    "correcta": "B"
}
```

Podemos acceder a sus datos utilizando las claves:

```python
print(pregunta["enunciado"])
print(pregunta["correcta"])
```

Estas estructuras nos ayudarán a organizar la información del cuestionario.

### 4. Funciones

Una función es un bloque de código con un nombre que podemos ejecutar cuando lo necesitemos.

La palabra `def` permite definir una función.

```python
def comprobar_respuesta(respuesta, correcta):
    return respuesta == correcta

resultado = comprobar_respuesta("B", "B")
print(resultado)
```

El resultado será:

```text
True
```

En este ejemplo:

- `respuesta` y `correcta` son parámetros.
- `"B"` y `"B"` son los argumentos que pasamos al llamar a la función.
- `return` devuelve el resultado de la comparación.

Más adelante podremos crear funciones específicas para:

- Mostrar las preguntas.
- Recoger y validar las respuestas.
- Comprobar si el usuario ha acertado.
- Actualizar la puntuación.
- Mostrar el resultado final.

Esto hará que el programa sea más fácil de entender, probar y mantener.

### 5. Entrada y salida de datos

Para interactuar con el usuario utilizaremos `input()` y `print()`.

- `input()` muestra un mensaje y espera a que el usuario introduzca información.
- `print()` muestra información por pantalla.

En el cuestionario pediremos respuestas como `A`, `B` o `C`.

Para aceptar tanto letras mayúsculas como minúsculas, y eliminar espacios innecesarios, podemos utilizar:

```python
respuesta = input("Introduce tu respuesta: ").strip().upper()
```

- `.strip()` elimina los espacios en blanco al principio y al final.
- `.upper()` convierte las letras a mayúsculas.

Esto mejora la experiencia del usuario y simplifica la validación de las respuestas.

## 🧠 Diseñar la lógica del juego

Antes de escribir el programa completo, es importante definir el flujo de ejecución.

1. Mostrar el nombre del proyecto y las instrucciones.
2. Preparar las preguntas, las opciones y las respuestas correctas.
3. Inicializar la puntuación en cero.
4. Recorrer las preguntas mediante un bucle `for`.
5. Mostrar las opciones disponibles para cada pregunta.
6. Solicitar una respuesta y comprobar que sea válida.
7. Comparar la respuesta introducida con la respuesta correcta.
8. Mostrar si la respuesta es correcta o incorrecta.
9. Actualizar la puntuación cuando corresponda.
10. Mostrar la puntuación final al terminar el cuestionario.

Una vez comprendido este flujo, el código será mucho más fácil de desarrollar y explicar.

## 💻 Desarrollo del programa

### 1. Comienzo

El primer paso consiste en mostrar por pantalla el nombre del proyecto y preparar la interacción con el usuario.

### 2. Listas de preguntas y respuestas

Creamos las estructuras necesarias para almacenar:

- Las preguntas.
- Las opciones de respuesta.
- Las respuestas correctas.

También inicializamos una variable llamada `puntuacion`, donde guardaremos el número de respuestas correctas.

### 3. Estructura del programa

Utilizamos un bucle `for` para recorrer las preguntas, mostrar las opciones y esperar la respuesta del usuario.

Si la respuesta es correcta, el programa muestra un mensaje de confirmación y suma un punto. Si es incorrecta, muestra la respuesta correcta.

También incorporamos una validación para impedir que se acepten respuestas que no estén entre las opciones permitidas.

### 4. Primer bucle `for`

El primer bucle recorre todas las preguntas.

Por ejemplo:

```python
for i in range(len(preguntas)):
    print(f"Pregunta {i + 1}: {preguntas[i]}")
```

Sus componentes son:

- `i` representa el índice de la pregunta actual.
- `len(preguntas)` calcula el número total de preguntas.
- `range()` genera los índices que se recorrerán.
- `i + 1` permite mostrar la numeración desde uno, aunque los índices de Python comiencen en cero.

Si hay seis preguntas, `range(len(preguntas))` generará los índices `0, 1, 2, 3, 4, 5`.

### 5. Segundo bucle `for`

El segundo bucle muestra las opciones correspondientes a cada pregunta.

```python
for o in range(len(opciones[i])):
    print(opciones[i][o])
```

En este caso:

- `o` representa el índice de cada opción.
- `len(opciones[i])` calcula cuántas opciones tiene la pregunta actual.
- `opciones[i][o]` obtiene el texto de cada opción.
- `print()` muestra la opción por pantalla.

Así podemos mostrar todas las opciones sin tener que escribir una instrucción `print()` para cada una.

### 6. Bucle `while`: validar las respuestas

Utilizamos un bucle `while` para repetir la solicitud de respuesta hasta que el usuario introduzca una opción válida.

```python
while True:
    respuesta = input("Tu respuesta (A, B, C o D): ").strip().upper()

    if respuesta in ["A", "B", "C", "D"]:
        break
    else:
        print("Respuesta no válida. Inténtalo de nuevo.")
```

Sus componentes son:

- `while True`: mantiene el bucle en ejecución.
- `input()`: solicita una respuesta al usuario.
- `.strip()` y `.upper()`: normalizan el texto introducido.
- `in`: comprueba si la respuesta está dentro de la lista de opciones permitidas.
- `break`: termina el bucle cuando la respuesta es válida.
- `else`: ejecuta el mensaje de error cuando la respuesta no es válida.

De esta forma evitamos procesar respuestas que no correspondan a las opciones disponibles.

### 7. Comprobar las respuestas

Cuando el usuario introduce una respuesta válida, el programa comprueba si coincide con la solución.

Si es correcta:

- Muestra un mensaje de confirmación.
- Incrementa la puntuación en un punto.

Si es incorrecta:

- Muestra un mensaje indicando que la respuesta no es correcta.
- Informa de cuál era la respuesta correcta.

Este proceso se repite hasta que se hayan respondido todas las preguntas.

### 8. Mostrar la puntuación final

Cuando termina el bucle principal, el programa muestra el resultado obtenido.

```python
print("La puntuación total es de: ", puntuacion,"/",len(preguntas))
```

Esta instrucción muestra:

- `puntuacion`: el número de respuestas correctas.
- `len(preguntas)`: el número total de preguntas.

Por ejemplo, si el usuario acierta cuatro de las seis preguntas, el resultado será:

```text
Has conseguido 4 de 6 puntos.
```

## 🧪 Pruebas y mejoras futuras

Para comprobar el funcionamiento del programa, podemos realizar distintas pruebas:

- Introducir una respuesta correcta.
- Introducir una respuesta incorrecta.
- Escribir una letra minúscula.
- Introducir espacios antes o después de la respuesta.
- Introducir una opción no válida.
- Completar todas las preguntas y comprobar la puntuación final.

Como posibles mejoras, se podrían añadir más preguntas, separar la lógica en funciones, calcular el porcentaje de aciertos y permitir repetir el cuestionario.

## ▶️ Cómo ejecutar el proyecto

1. Instalar Python 3.
2. Descargar o clonar este repositorio.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar el archivo principal:

```bash
python quiz.py
```

En algunos sistemas puede ser necesario utilizar `python3 quiz.py`.

## 📌 Conclusión

Este proyecto me permite aplicar los fundamentos de Python mediante un ejemplo práctico relacionado con la ciberseguridad.

Además de aprender a programar, practicaré la organización del código, la validación de entradas, las pruebas y la documentación de un proyecto.

El objetivo es construir una aplicación sencilla, comprensible y ampliable que sirva como base para futuros proyectos.
