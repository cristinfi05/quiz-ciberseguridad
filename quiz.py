print("================================")
print("     QUIZ DE CIBERSEGURIDAD")
print("================================")


preguntas = [
    "¿Cuál es la diferencia entre un virus y un gusano?",
    "¿Puede explicar qué es la autenticación multifactor y por qué es importante?",
    "Describa qué hace un firewall en una red",
    "¿Qué es el cifrado y por qué es esencial en la ciberseguridad?",
    "¿Qué es un ataque DDoS?",
    "¿Qué pasos tomaría si descubriera una brecha de seguridad?"

]

opciones = [
    [ #opciones pregunta 1
        "A) Un virus solo afecta a dispositivos móviles.",
        "B) Un gusano necesita siempre un antivirus para propagarse.",
        "C) Un virus suele necesitar un archivo o programa huésped, mientras que un gusano puede propagarse de forma autónoma por una red.",
        "D) No existe ninguna diferencia entre ambos."
    ],

    [ #opciones pregunta 2
        "A) Es utilizar varias contraseñas diferentes para una misma cuenta.",
        "B) Es utilizar dos o más métodos de verificación para confirmar la identidad de un usuario, aumentando la seguridad.",
        "C) Es compartir una contraseña entre varios usuarios.",
        "D) Es un sistema que elimina la necesidad de utilizar contraseñas."
    ],

    [ #opciones pregunta 3
        "A) Aumenta automáticamente la velocidad de Internet.",
        "B) Crea copias de seguridad de todos los archivos.",
        "C) Controla y filtra el tráfico de red según determinadas reglas de seguridad.",
        "D) Cifra todos los archivos almacenados en un ordenador."
    ],

    [ #opciones pregunta 4
        "A) Es eliminar información para ahorrar espacio.",
        "B) Es convertir la información en un formato que dificulta que personas no autorizadas puedan acceder a ella, protegiendo su confidencialidad.",
        "C) Es crear copias idénticas de los archivos.",
        "D) Es un método para detectar virus automáticamente."
    ],

    [ #opciones pregunta 5
        "A) Un ataque cuyo objetivo es saturar un servicio o servidor con una gran cantidad de tráfico para impedir o dificultar su funcionamiento normal.",
        "B) Un ataque destinado exclusivamente a robar contraseñas.",
        "C) Un programa utilizado para cifrar archivos.",
        "D) Un sistema de autenticación basado en dos factores."
    ],
    [ #opciones pregunta 6
        "A) Ignorarla si aparentemente no afecta a mi ordenador.",
        "B) Intentar ocultarla para evitar problemas.",
        "C) Informar inmediatamente al responsable o equipo de seguridad, contener el incidente y seguir el protocolo establecido.",
        "D) Publicar la información en redes sociales para avisar a otros usuarios."
    ]
]

respuestas_correctas = [
    "C",  "B", "C", "B", "A", "C"

]

puntuacion = 0


for i in range(len(preguntas)):
    print("Pregunta", i + 1, preguntas[i])

    for o in range(len(opciones[i])):
        print(opciones[i][o])

#Para evitar que alguien introduzca una letra incorrecta o un número, utilizaremos while    
    while True:
        respuesta = input("Introduce tu respuesta (A, B, C o D): ").strip().upper() #input() recoge lo que escribe el usuario, .strip() elimina espacios al principio y al final. y .upper() convierte las letras a mayúsculas, así que también acepta a, b, c y d.

        if respuesta in ["A", "B", "C", "D"]:
            break
        else:
            print("Respuesta no válida. Introduce A, B, C o D.")

    if respuesta == respuestas_correctas[i]:
        print("-----------------------")
        print("¡Respuesta correcta!")
        print("-----------------------")
        puntuacion += 1

    else:
        print("-------------------------------------")
        print("Respuesta incorrecta")
        #Para dar la respuesta correcta:
        print("La respuesta correcta era:", respuestas_correctas[i])
        print("-------------------------------------")

print("La puntuación total es de: ", puntuacion,"/",len(preguntas))

nota = puntuacion / len(preguntas) * 10
print("Tu nota sobre 10 es:", nota)
    
    

