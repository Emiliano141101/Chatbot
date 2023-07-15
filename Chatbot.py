import nltk
from nltk.chat.util import Chat, reflections

# Definición de los patrones de entrada y respuestas
patrones = [
    [
        r"mi nombre es (.*)",  # Si el usuario dice "mi nombre es [nombre]"
        ["Hola %1, ¿cómo puedo ayudarte?",]  # El chatbot responde saludando con el nombre del usuario
    ],
    [
        r"hola|buenos dias|buenas tardes|buenas noches",  # Si el usuario dice "hola" o saludo similar
        ["¡Hola! ¿En qué puedo ayudarte?",]  # El chatbot responde con un saludo y ofrece su ayuda
    ],
    [
        r"¿Cómo estás?",  # Si el usuario pregunta "¿Cómo estás?"
        ["Estoy bien, gracias. ¿Y tú?",]  # El chatbot responde que está bien y pregunta cómo está el usuario
    ],
    [
        r"bye|chao|adios|diu|hasta luego|Hasta Luego",  # Si el usuario dice "bye" o algo similar
        ["¡Hasta luego! Si necesitas algo más, no dudes en preguntar.",]  # El chatbot se despide y finaliza la conversación
    ],
]

def chatbot():
    print("¡Hola! Soy un chatbot. ¿En qué puedo ayudarte?")
    chat = Chat(patrones, reflections)  # Creación de un objeto Chat con los pares de entrada y respuestas
    chat.converse()  # Inicio de la conversación con el chatbot

if __name__ == "__main__":
    chatbot()  # Llamada a la función principal para iniciar el chatbot
