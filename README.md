# Asistente Virtual Automotriz

Este proyecto implementa un asistente virtual basado en la API de Google Generative AI para una empresa automotriz. El asistente está diseñado para proporcionar soporte al cliente relacionado con vehículos, incluyendo mantenimiento, financiamiento, programación de citas y actualizaciones sobre pedidos de vehículos. 

Además, se puede integrar una base de datos que almacene información relevante como precios de vehículos, stock de vehículos, historial de reparaciones, y otros datos específicos de la empresa, lo que permitirá ofrecer respuestas más personalizadas y en tiempo real.

El asistente virtual en este proyecto ofrece un alto grado de personalización, permitiendo adaptar las respuestas y comportamientos de la IA según las necesidades específicas de la empresa. A través de la configuración detallada del modelo, como las instrucciones del sistema y la integración de una base de datos con información exclusiva de la empresa (precios, stock, historial de reparaciones, etc.), el asistente puede ofrecer respuestas precisas y contextualizadas, mejorando la experiencia del cliente y optimizando las operaciones de soporte.

## Características

- **Asistencia en mantenimiento de vehículos:** Responde preguntas sobre procedimientos de mantenimiento preventivo, como cambios de aceite y revisión de frenos.
- **Opciones de financiamiento:** Brinda información sobre planes de pago a plazos, tasas de interés y requisitos para obtener un crédito.
- **Programación de citas:** Ayuda a los usuarios a agendar citas para reparaciones o servicios.
- **Actualizaciones sobre pedidos de vehículos:** Proporciona información sobre el estado de los pedidos, tiempos de entrega y opciones de personalización.
- **Consultas generales sobre vehículos:** Responde preguntas sobre los vehículos disponibles, características, precios y opciones de prueba de manejo.

## Requisitos

Asegúrate de tener instalado el SDK de Google Generative AI. Si no lo tienes, puedes instalarlo con:

```bash
pip install google-generativeai
```

## Configuración
- API Key: Configura tu clave API de Google Generative AI directamente en el código, reemplazando "Ingrese su APIKEY aqui" con tu clave de API.
- Instrucciones del sistema: El asistente está configurado con un conjunto de instrucciones predefinidas que definen cómo debe comportarse en diferentes situaciones.

## Uso
- Una vez configurado, ejecuta el siguiente script para interactuar con el modelo de IA:
```python
python asistente_virtual.py
```
Esto iniciará una sesión de chat donde puedes interactuar con el modelo. Escribe tus consultas y el modelo te responderá de manera contextual.

¡Gracias por usar el Asistente Virtual Automotriz!

## Autor
Agustin Maretto

