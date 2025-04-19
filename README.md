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
        │ • Válvula Solenoide                       │
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
| **Válvula Solenoide**  | Electroválvula        | Controlar el paso de agua hacia cada sección o capa                    | <img src="https://github.com/user-attachments/assets/2213f93a-a60e-418c-8599-002cefb22ace" width="100"> |
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
Cuando una o más capas presentan humedad baja, se activa la bomba de agua y la válvula correspondiente, enfocando el riego solo en las zonas que lo requieren.

### 3. 📏 Medición de Caudal
El sensor YF-S201 registra la cantidad exacta de agua utilizada, permitiendo calcular el consumo y detectar fallas (como flujo insuficiente).

### 4. 🔵 Indicador de Estado por LED RGB
El LED RGB cambia de color según el estado:
- 🟢 Verde: Humedad óptima  
- 🔵 Azul: Riego activo  
- 🔴 Rojo: Falla detectada o bajo caudal

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

<img src="https://github.com/user-attachments/assets/vertigarden-dashboard.png" width="600"/>

---

## 🏗️ Estructura Física

El sistema de riego vertical está construido sobre una estructura modular que incluye:

- Tres niveles de macetas conectadas por un sistema de riego compartido.
- Una válvula solenoide central controlada por ESP32 para distribuir el agua equitativamente.
- Sensores de humedad en cada nivel para monitoreo independiente.
- Bomba de agua conectada al sistema desde el nivel inferior.
- Cableado ordenado y soportes impresos en 3D.

**Imágenes del sistema:**

> <img src="img/riego_vertical_frontal.jpg" width="400"/>  
> <img src="img/soporte_sensor_humedad.jpg" width="400"/>

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
🎥 [Funcionamiento de sensores, bomba y válvula](https://drive.google.com/drive/folders/1GOXApjWNVipbJKVLVaaz4QoqaaGXq0BR?usp=sharing)

### 🌱 Demostración del sistema completo
📹 [Simulación del riego automático](https://drive.google.com/drive/folders/1GOXApjWNVipbJKVLVaaz4QoqaaGXq0BR?usp=sharing)

### 📣 Opiniones de prueba del sistema
📤 [Retroalimentación de usuarios y pruebas](https://drive.google.com/drive/folders/1GOXApjWNVipbJKVLVaaz4QoqaaGXq0BR?usp=sharing)

### 🧪 Evidencia de desarrollo en clase
📝 [Ejercicios prácticos y prototipos](https://drive.google.com/drive/folders/1GOXApjWNVipbJKVLVaaz4QoqaaGXq0BR?usp=sharing)

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
#### CoEvaluación:

### Oropeza Yepiz Cristian Efrín

#### AutoEvaluación:
#### CoEvaluación:

### Salinas Salinas Omar

#### AutoEvaluación:
#### CoEvaluación:


