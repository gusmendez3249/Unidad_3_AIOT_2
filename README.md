# 🌿 VERTIGARDEN - Sistema Inteligente de Riego para Jardines Verticales

**VERTIGARDEN** es un sistema inteligente de automatización de riego diseñado especialmente para jardines verticales urbanos. Utiliza sensores distribuidos por capas, inteligencia artificial embebida y una arquitectura IoT basada en microcontroladores ESP32 para optimizar el uso del agua y mejorar la salud de las plantas.

## 📌 Descripción General

Este proyecto integra múltiples sensores y actuadores conectados a través de una red de ESP32, coordinados mediante Node-RED. Incluye visualización gráfica del sistema, control manual desde un dashboard web y almacenamiento de datos históricos en PostgreSQL.

### ⚙️ Características principales

- Medición de humedad por capas (3 sensores).
- Control del flujo de agua con válvulas solenoides y bomba.
- Visualización en pantalla LCD integrada.
- Indicador RGB para mostrar el estado del sistema (riego activo, alerta, humedad óptima, etc).
- Control manual y visualización en tiempo real a través de Node-RED.
- Almacenamiento de datos en PostgreSQL para análisis y trazabilidad.

## 🎯 Objetivos del Proyecto

- Automatizar el riego eficiente en jardines verticales mediante sensores de humedad y flujo.
- Diseñar una solución IoT escalable basada en múltiples nodos ESP32.
- Adaptar el riego automáticamente según condiciones climáticas obtenidas por geolocalización.
- Visualizar el estado del sistema y controlar el riego desde una interfaz web.
- Registrar datos históricos en una base de datos PostgreSQL.
- Desarrollar una maqueta física con componentes reales e impresión 3D.

## 🧠 Tecnologías Utilizadas

| Tecnología         | Descripción                                          |
|--------------------|----------------------------------------------------- |
| **ESP32**          | Microcontroladores para lectura y actuación          |
| **Node-RED**       | Plataforma de automatización y dashboard web         |
| **PostgreSQL**     | Base de datos para almacenamiento de datos           |
| **Python**         | Scripts de backend y análisis de datos               |
| **MQTT**           | Protocolo de mensajería entre nodos ESP32 y Node Red |
| **Impresión 3D**   | Estructuras físicas y mecanismos personalizados      |


## 🧠 Arquitectura del Sistema – VertiGarden 🌿

```plaintext
                  [ESP32 Principal]
        ┌───────────────────────────────────────────┐
        │ • Sensor de Humedad Capa 1                │
        │ • Sensor de Humedad Capa 2                │
        │ • Sensor de Humedad Capa 3                │
        │ • Sensor de Flujo de Agua                 │
        │ • Bomba de Agua                           │
        │ • Pantalla TFT LCD 2.8"                   │
        │ • LED RGB (estado del sistema)            │
        └───────────────────────────────────────────┘
                         │
                         ▼
                        MQTT
                         │
                         ▼
                  [🌐 Node-RED ]
        ┌────────────────────────────────────────────┐
        │ • Visualización en tiempo real             │
        │ • Control manual y automático              │       
        └────────────────────────────────────────────┘
                         │
                         ▼
               [🗄️ Base de Datos PostgreSQL]
        ┌────────────────────────────────────────────┐
        │ • Registro histórico de humedad y riego    │
        │ • Datos para análisis y reportes           │
        └────────────────────────────────────────────┘
```

## 🧹 **Tabla de Actuadores**

| **Nombre**             | **Tipo**              | **Uso**                                                                 | **Imagen** |
|------------------------|-----------------------|------------------------------------------------------------------------|------------|
| **Bomba de Agua 12V**  | Electromecánico       | Activar el flujo de agua hacia el jardín vertical                      | <img src="https://github.com/user-attachments/assets/28352478-d119-49cb-a753-c356e652d453" width="100"> |
| **Pantalla LCD 2.8”**  | Visualización         | Mostrar información de humedad, estado de riego y alertas del sistema | <img src="https://github.com/user-attachments/assets/abba870c-b2ca-45a9-a737-c8653a4ad93c" width="100"> |
| **LED RGB**            | Indicador Visual      | Mostrar estado general del sistema (óptimo, regando, alerta, etc.)     | <img src="https://github.com/user-attachments/assets/b1393576-9d7f-4fde-a678-2a730e94959d" width="100"> |

---

## 🌱 **Tabla de Sensores**

| **Nombre**                      | **Tipo**              | **Uso**                                                                   | **Imagen** |
|----------------------------------|-----------------------|----------------------------------------------------------------------------|------------|
| **Sensor de Humedad Capacitivo** | Humedad del sustrato  | Medir el nivel de humedad en distintas capas del jardín vertical           | <img src="https://github.com/user-attachments/assets/e8c09489-97b0-481a-9177-c06eb030c0c3" width="100"> |
| **Sensor de Flujo YF-S201**      | Caudalímetro          | Medir el caudal de agua que pasa por el sistema de riego                   | <img src="https://github.com/user-attachments/assets/2281917f-7c69-4482-82fe-e7befda65064" width="100"> |

---

## ⚙️ **Funcionalidad del Sistema**

El sistema **VERTIGARDEN** automatiza el riego de un jardín vertical mediante sensores y actuadores estratégicamente integrados. Su funcionalidad principal se organiza en los siguientes procesos:

### 1. 🌡️ Monitoreo Multicapa de Humedad
Sensores capacitivos instalados en tres capas del jardín vertical permiten conocer en tiempo real el nivel de humedad en cada sección.

### 2. 💧 Activación Inteligente del Riego
Cuando una o más capas presentan humedad baja, se activa la bomba de agua correspondiente, enfocando el riego solo en las zonas que lo requieren.

### 3. 📏 Medición de Caudal
El sensor YF-S201 registra la cantidad exacta de agua utilizada, permitiendo calcular el consumo y detectar fallas (como flujo insuficiente).

### 4. 🔵 Indicador de Estado por LED RGB
El LED RGB cambia de color según el estado:
- 🟢 Verde: Humedad óptima  
- 🔵 Azul: Exceso de Humedad
- 🟣 Morado: Seco

### 5. 🖥️ Visualización 
Desde una pantalla LCD se pueden visualizar los datos del sistema en tiempo real. Además, una interfaz en Node-RED permite activar el riego manualmente o revisar datos históricos.



---

## 🌿 Interfaz Gráfica DashBoard

La interfaz fue desarrollada en **Node-RED** utilizando **DashBoard** y permite:

- Visualizar en tiempo real los niveles de humedad de cada maceta.
- Visualizar gráficas históricas de humedad por maceta.
- Ver el estado actual del sistema (Riego activo/inactivo).
- Recibir alertas cuando se detecta baja humedad en alguna maceta.
- Registrar métricas del tiempo de riego de las últimas 10 sesiones.

**Ejemplo de interfaz:**
![Imagen de WhatsApp 2025-04-22 a las 23 09 35_f5490c59](https://github.com/user-attachments/assets/bab17c56-17e9-4bb0-81ba-01251313786b)


<img src="https://github.com/user-attachments/assets/0dba65ac-ebac-4846-ad4a-836fa12f9298" width="600"/>

---

## 🏗️ Estructura Física

El sistema de riego vertical está construido sobre una estructura modular que incluye:

- Tres niveles de macetas conectadas por un sistema de riego compartido.
- Una válvula solenoide central controlada por ESP32 para distribuir el agua equitativamente.
- Sensores de humedad en cada nivel para monitoreo independiente.
- Bomba de agua conectada al sistema desde el nivel inferior.
- Cableado ordenado y soportes impresos en 3D.

**Imágenes del sistema:**

> <img src="https://github.com/user-attachments/assets/96738964-06de-4835-9b8d-ed0fa96cb9e0" width="400"/>  
> <img src="https://github.com/user-attachments/assets/dfa6b504-4453-4814-a701-03ff2f32cf39" width="400"/>

---


## 🏠 Diagramas de las Placas

Visualiza el diagrama completo de conexiones y componentes utilizados en el sistema **VERTIGARDEN** desde la siguiente plataforma:

🔗 **Proyecto en Cirkit Designer**  
[Haz clic aquí para ver el diagrama interactivo](https://app.cirkitdesigner.com/project/68e0465e-dece-4ab6-84fe-c091308ddfd5)

<p align="center">
  <img src="https://github.com/user-attachments/assets/209ee904-8123-4615-80f6-1fa2f4705cbb" alt="Diagrama del sistema" width="600">
</p>

---

## 🌿 Almacenamiento de Datos

Todos los datos generados por los sensores de humedad son registrados en una base de datos **PostgreSQL**, lo que permite:

- Consultar los niveles de humedad.
- Analizar el comportamiento del sistema de riego a lo largo del tiempo.
- Enviar reportes de uso eficiente del agua a correo electronico.
- Conectar con otras herramientas para análisis externo.

---

## 🔧 Expansión y Notificaciones

El sistema fue desarrollado con una estructura flexible que permite:

- Añadir nuevas macetas y sensores.
- Configurar alertas automáticas vía **correo electrónico** cuando el nivel de humedad cae por debajo del mínimo.
- Posibilidad de incluir nuevos módulos como sensores de clima, caudalímetros o predicción de riego.
- Integración futura con asistentes virtuales y apps móviles.

---

## 🎬 Material Multimedia

### 🔍 Videos por componentes
🎥 [Funcionamiento de sensores, bomba y válvula](https://drive.google.com/drive/folders/1TCuIVjoKcGJ-OH3HvJeOxbSiyeZHVh73?usp=sharing)

### 🌱 Demostración del sistema completo
📹 [Simulación del riego automático](https://drive.google.com/drive/folders/1ZkmVhPTaFoO9hK0RorH6tKAx9eoci6xr?usp=sharing)

### 🧪 Evidencia de desarrollo en clase
📝 [Ejercicios prácticos y prototipos](https://drive.google.com/drive/folders/1UCjZf1Dyts2afRVda1kKaeM01rc2cGyx?usp=sharing)

---

## 🧠 Conclusión del Proyecto

**VERTI-GARDEN SYSTEM** es una solución tecnológica de bajo consumo enfocada en la automatización del riego en espacios verticales. Reduce el desperdicio de agua, facilita el mantenimiento de plantas en áreas urbanas y puede ser gestionado desde cualquier lugar con acceso a red. Combina electrónica, software y sostenibilidad en un mismo sistema.

---

## 📦 Organización del Proyecto

```text
/vertical-irrigation-system/
├── images/              # Fotografías y diagramas del sistema
├── documentation/       # Guías técnicas, PDF y diagramas
├── nodered-flows/       # Flujos exportados de Node-RED
├── firmware-esp32/      # Código en MicroPython para sensores y actuadores
├── sql-db/              # Scripts de inicialización de PostgreSQL
├── notifications/       # WebApp para alertas automáticas
├── README.md            # Documentación principal
└── ...                  # Otros recursos (scripts, configuraciones, etc.)


```
## ✍️ Autores

- **Nombre del equipo**: VERTIGARDEN
- **Integrantes**:
  - Cruz Méndez Juan Gustavo Ángel
  - Oropeza Yepiz Cristian Efrín
  - Salinas Salinas Omar

---

## 📌 Autoevaluación y coevaluación

### Cruz Méndez Juan Gustavo Ángel

#### AutoEvaluación:

**¿Qué hice bien?**

Durante el desarrollo del proyecto VERTIGARDEN, me desempeñé eficazmente en la integración de los sensores de humedad por capas y su calibración. Fui constante en las pruebas de hardware y aseguré la estabilidad de los datos obtenidos. También destaqué en habilidades blandas como la organización y responsabilidad, cumpliendo con los plazos y manteniendo una comunicación clara con el equipo en cada etapa del proyecto.

**¿Qué hice mal?**

Uno de los errores que reconozco fue no registrar detalladamente las configuraciones electrónicas y los cambios en el firmware del ESP32. Esto dificultó la comprensión de mis avances por parte del equipo. Además, por momentos me costó tomar iniciativa para resolver ciertos problemas, lo que afectó ligeramente la fluidez de nuestro desarrollo conjunto durante las semanas intermedias del proyecto.

**¿Qué puedo mejorar?**

Considero que puedo mejorar en la documentación técnica, ya que registrar adecuadamente cada avance puede facilitar el mantenimiento del sistema en el futuro. Además, quiero fortalecer mi proactividad y liderazgo, participando con mayor decisión en las fases de análisis y proponiendo soluciones cuando surjan obstáculos técnicos o de organización dentro del equipo.

#### CoEvaluación:

***Sobre Cristian Oropeza***

**¿Qué hizo bien?**

Cristian se desempeñó muy bien en el diseño y programación de la interfaz gráfica del sistema en la pantalla TFT. Logró que la presentación de los datos fuera clara, ordenada y visualmente atractiva. Su constancia y enfoque técnico permitieron que el sistema fuera más intuitivo para el usuario, lo cual fue clave para la funcionalidad general del proyecto.

**¿Qué hizo mal?**

A pesar de su buen trabajo en el área visual, en algunas ocasiones no participó de manera activa en las reuniones grupales donde se tomaban decisiones técnicas importantes. Esto generó cierta desconexión con los avances del resto del equipo, lo que en algunos momentos provocó trabajos duplicados o mal sincronizados con los demás módulos del sistema.

**¿Qué puede mejorar?**

Puede mejorar su participación en las decisiones generales del equipo, especialmente cuando los avances de su área afectan a otros integrantes. Si logra involucrarse más en el flujo de comunicación y en la planeación conjunta, su impacto será aún mayor y se podrán evitar retrasos o confusiones al momento de integrar los distintos elementos del sistema.

***Sobre Omar Salinas***

**¿Qué hizo bien?**
Omar mostró un alto nivel de compromiso en el desarrollo de la lógica de riego automático. Estuvo a cargo de implementar el comportamiento del sistema en función de la lectura de los sensores de humedad y se destacó por encontrar soluciones técnicas a problemas que surgieron en la etapa de pruebas. Su iniciativa fue importante para el avance del equipo.

**¿Qué hizo mal?**
Uno de los aspectos negativos fue que, en algunas ocasiones, Omar trabajó de manera muy independiente en la parte del código de control, sin comunicar adecuadamente sus avances. Esto generó dificultades al momento de integrar todos los módulos, ya que no siempre coincidían los criterios de diseño o las estructuras de datos entre su parte y la de los demás.

**¿Qué puede mejorar?**
Podría enfocarse en compartir sus avances con más regularidad y buscar la opinión de los compañeros para asegurar que todo esté alineado. Mejorar su comunicación dentro del equipo le permitirá no solo facilitar la integración, sino también enriquecer su trabajo con nuevas ideas que puedan surgir de la colaboración constante.

### Oropeza Yepiz Cristian Efrín

#### AutoEvaluación:

**¿Qué hice bien?**

Mi mayor aporte al proyecto fue el desarrollo de la interfaz gráfica en pantalla, donde mostré habilidades técnicas de diseño, visualización de datos y control de estado del sistema. Además, destaqué por mi constancia, actitud colaborativa y disposición para resolver errores de software. A nivel de habilidades blandas, mantuve buena comunicación con el equipo y estuve disponible para apoyar en tareas fuera de mi asignación directa.

**¿Qué hice mal?**

En algunas fases del proyecto me faltó organización y no documenté adecuadamente ciertos fragmentos de código. También tardé en familiarizarme con el entorno de Thonny y la placa ESP32, lo cual provocó retrasos en la parte inicial del desarrollo. Finalmente, reconozco que pude involucrarme más en la parte de análisis del sistema y aportar ideas desde el enfoque funcional y no solo visual.

**¿Qué puedo mejorar?**

Debo mejorar la planificación personal de mis tareas y optimizar el uso del tiempo para evitar acumulación de trabajo. También quiero fortalecer mis habilidades de documentación y aportar más en fases de toma de decisiones técnicas. En próximos proyectos, buscaré participar de forma más integral y proponer ideas que abarquen tanto la lógica como la presentación del sistema.

#### CoEvaluación:

***Sobre Juan Gustavo Ángel Cruz***

**¿Qué hizo bien?**

Juan Gustavo tuvo un rol fundamental en la instalación y calibración de los sensores de humedad, logrando lecturas estables y útiles para la lógica del sistema. Fue muy dedicado en las pruebas de campo y mostró responsabilidad al encargarse de tareas críticas del sistema. Su actitud de apoyo al equipo también fue constante durante todo el desarrollo del proyecto.

**¿Qué hizo mal?**

En algunas etapas avanzó por su cuenta sin notificar en qué parte del sistema estaba trabajando, lo que provocó pequeños conflictos de integración. A veces le faltó consultar ciertas decisiones técnicas que afectaban el funcionamiento conjunto, especialmente cuando se trataba de conexiones o pruebas que impactaban otras áreas del hardware.

**¿Qué puede mejorar?**

Podría mejorar su participación en las sesiones de coordinación, comunicando con mayor claridad los avances y dificultades que enfrenta. Esto no solo mejoraría la sincronización del equipo, sino que también le permitiría recibir apoyo o ideas que complementen sus soluciones. Su trabajo es bueno, pero con más colaboración sería aún más eficiente.

***Sobre Omar Salinas***

**¿Qué hizo bien?**

Omar se destacó por desarrollar una lógica de riego automática muy efectiva, que respondió correctamente a los distintos niveles de humedad. Mostró seguridad al programar y una actitud muy resolutiva cuando surgieron errores en las pruebas. Además, siempre se mantuvo motivado y fue un gran impulsor del progreso del equipo en los momentos de mayor presión.

**¿Qué hizo mal?**

En algunos momentos tomó decisiones técnicas sin alinearlas con el resto del equipo, especialmente en el diseño del flujo de riego. Esto llevó a ajustes de último momento para que sus soluciones encajaran con la estructura general del sistema, generando trabajo adicional para el grupo en la integración final.

**¿Qué puede mejorar?**

Puede enfocarse en fortalecer la comunicación con el equipo, explicando con más detalle qué hace y por qué lo hace. También sería útil que documente mejor su código y sus decisiones, de modo que cualquier miembro pueda entender e intervenir en su módulo si es necesario. Su liderazgo técnico mejoraría aún más con estas prácticas.

### Salinas Salinas Omar

#### AutoEvaluación:

**¿Qué hice bien?**

Participé activamente en el desarrollo de la lógica de riego automático basada en la lectura de sensores de humedad. Logré que el sistema respondiera correctamente ante diferentes niveles, optimizando el uso del agua. Además, ayudé en la integración de componentes electrónicos y resolución de errores. Me destaqué por mantener una buena actitud, promover el orden en el equipo y apoyar en momentos clave del trabajo colaborativo.

**¿Qué hice mal?**

En ocasiones me enfoqué demasiado en el desarrollo del código de control sin comunicarlo oportunamente al equipo, lo que complicó la integración con otras partes del sistema, como la interfaz o la validación de datos. También cometí errores en la conexión inicial de algunos componentes, por falta de revisar datasheets con más atención. Esto provocó algunos retrasos en las pruebas de campo.

**¿Qué puedo mejorar?**

Necesito mejorar la comunicación constante con el equipo, especialmente al trabajar en módulos que dependen de otros compañeros. También debo organizar mejor mis tiempos para equilibrar pruebas prácticas con documentación técnica. Finalmente, me gustaría desarrollar más habilidades de presentación, para explicar de forma sencilla el funcionamiento técnico de los componentes a mis compañeros y facilitar el trabajo en conjunto.


#### CoEvaluación:

***Sobre Juan Gustavo Ángel Cruz***

**¿Qué hizo bien?**

Juan Gustavo tuvo un excelente desempeño en la parte de sensores. Fue muy preciso al momento de instalar, probar y validar el comportamiento de cada uno. Además, fue de los primeros en tener lista su parte, lo cual permitió que el equipo pudiera avanzar en fases posteriores con una base sólida de datos y funcionamiento real del sistema.

**¿Qué hizo mal?**
A veces trabajaba en silencio sin compartir los detalles de lo que había probado o ajustado. Esto generaba dudas sobre el estado real del sistema y dificultaba que el resto del equipo pudiese coordinar acciones en conjunto. Aunque sus resultados eran buenos, la falta de actualizaciones al grupo complicaba un poco la organización general.

**¿Qué puede mejorar?**
Podría mejorar su participación en la comunicación diaria del equipo, informando con claridad qué avances tiene y qué problemas ha encontrado. Esto permitiría tomar decisiones más rápidas y con información completa. Además, compartir sus ideas con el equipo podría enriquecer aún más el enfoque técnico que está desarrollando.

***Sobre Cristian Oropeza***

**¿Qué hizo bien?**

Cristian realizó un gran trabajo diseñando la interfaz del sistema. La visualización fue clara, funcional y permitió interpretar fácilmente los datos. También fue muy paciente y receptivo ante las sugerencias, ajustando la presentación para que se adaptara bien a las necesidades de todos los usuarios del sistema. Fue una pieza clave para dar una presentación profesional al proyecto.

**¿Qué hizo mal?**

En algunas ocasiones se limitó solamente a su área de diseño y no mostró mucho interés por entender otras partes del sistema, como el manejo de datos o la lógica de riego. Esto redujo su participación en discusiones más técnicas donde su perspectiva podría haber sido valiosa para mejorar la cohesión del proyecto.

**¿Qué puede mejorar?**

Podría involucrarse más allá de su módulo visual, aprendiendo un poco sobre cómo funciona la lógica del sistema completo. Esto le permitiría anticipar mejor lo que necesita mostrar en pantalla y proponer mejoras más conectadas con el funcionamiento interno. También enriquecería su conocimiento técnico general, que siempre es valioso para futuros proyectos.
