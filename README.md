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

## 🖥️ Estructura del Proyecto

