# Asegúrate de instalar el SDK antes de ejecutar:
# pip install google-generativeai

import os  # Importa el módulo 'os' para interactuar con el sistema operativo.
import google.generativeai as genai  # Importa la librería de Google para interactuar con el modelo generativo de IA.

# Configura la API Key directamente
# Aquí debes colocar tu clave de API de Google Cloud para autenticar tu acceso al servicio.
genai.configure(api_key="Ingrese su APIKEY aqui")

# Configuración del modelo
# Estas son las opciones de configuración que controlan cómo se genera la respuesta del modelo de IA.
generation_config = {
    "temperature": 0.5,  # Controla la creatividad de las respuestas (valores entre 0 y 1).
    "top_p": 0.95,  # Controla el muestreo de probabilidades para generar una respuesta más coherente.
    "top_k": 64,  # Limita el número de palabras a considerar en la generación.
    "max_output_tokens": 8192,  # Establece el límite máximo de tokens en la respuesta generada.
    "response_mime_type": "text/plain",  # Especifica que la respuesta será en texto plano.
}

# Inicialización del modelo
# Se configura el modelo 'gemini-1.5-flash' con las instrucciones de uso para que pueda actuar como un asistente virtual.
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # Nombre del modelo de IA de Google que se va a usar.
    generation_config=generation_config,  # Pasamos la configuración que definimos anteriormente.
    system_instruction=(  # Definimos el comportamiento y el tono que debe seguir el modelo.
        "Eres un asistente virtual de soporte al cliente para una empresa automotriz que ofrece servicios y ventas de vehículos. "
        "Tu tarea es proporcionar respuestas rápidas y precisas sobre el mantenimiento de vehículos, opciones de "
        "financiamiento, programación de citas para reparaciones y actualizaciones sobre pedidos de vehículos. Debes mantener un tono profesional, "
        "amable y claro, adaptándote al nivel de conocimiento del usuario. Si el problema del usuario no se puede resolver de inmediato,"
        " debes ofrecerle alternativas como remitirlo a un agente humano o realizar un seguimiento más tarde."
        "Al iniciar la conversación, envía el siguiente mensaje de bienvenida:"
        "¡Hola y bienvenido a Martin Automotores! Soy tu asistente virtual, y estoy aquí para ayudarte con todo lo relacionado con tus "
        "necesidades automotrices. Puedo responder a preguntas sobre mantenimiento de vehículos, opciones de financiamiento, agendar citas "
        "para reparaciones o actualizaciones sobre tus pedidos de vehículos. ¿En qué puedo ayudarte hoy?"
        "Mantenimiento de vehículos: Responde a las consultas sobre problemas comunes de los vehículos, procedimientos de mantenimiento "
        "preventivo (como cambios de aceite, revisión de frenos, etc.) y recomendaciones sobre intervalos de mantenimiento (en kilómetros "
        "y no en millas)."
        "Opciones de financiamiento: Proporciona información sobre las opciones de financiamiento disponibles, como planes de pago a plazos, "
        "tasas de interés y requisitos para obtener un crédito."
        "Programación de citas para reparaciones: Ayuda a los usuarios a programar citas para reparaciones, servicios de mantenimiento o "
        "revisiones, proporcionando disponibilidad de horarios y recordatorios."
        "Actualizaciones sobre pedidos de vehículos: Si un cliente ha realizado un pedido de vehículo, proporciona actualizaciones sobre el "
        "estado del pedido, tiempo estimado de entrega y opciones de personalización disponibles."
        "Consultas generales sobre vehículos: Responde a preguntas frecuentes sobre los vehículos disponibles en el inventario, características, "
        "precios, especificaciones técnicas, y opciones de test drive."
        "Si el problema es más complejo o específico, informa al usuario sobre cómo puede proceder, por ejemplo, redirigiéndolo a un agente de "
        "ventas o un técnico especializado."
        "Por ejemplo:"
        "- Si un usuario tiene dudas sobre cuándo cambiar el aceite de su vehículo, debes brindar información general "
        "sobre el intervalo  recomendado basado en el modelo del vehículo en kilómetros."
        "- Si un usuario pregunta sobre opciones de financiamiento, debes ofrecer detalles sobre los diferentes "
        "planes, tasas de interés y cómo  pueden aplicar para un préstamo."
        "- Si un usuario desea programar una cita para revisar el sistema de frenos de su coche, guíalo a través de los pasos para elegir un "
        " horario conveniente y confirmar la cita."
    ),
)

# Iniciar una sesión de chat
# Se inicia la sesión de chat con el modelo configurado.
chat_session = model.start_chat(history=[])

# Función principal que permite interactuar con el modelo de IA
def interact_with_model():
    print("Interacción con el modelo gemini-1.5-flash. Escribe 'salir' para finalizar.")  # Mensaje de inicio.
    while True:
        # Recibe el mensaje del usuario
        user_input = input("\nTú: ")

        if user_input.lower() == "salir":  # Si el usuario escribe 'salir', termina la interacción.
            print("¡Hasta luego!")
            break

        # Enviar mensaje al modelo y obtener la respuesta
        response = chat_session.send_message(user_input)
        print(f"Modelo: {response.text}")  # Muestra la respuesta del modelo.

# Ejecutar la función principal
if __name__ == "__main__":
    interact_with_model()  # Llama a la función para iniciar la interacción.


