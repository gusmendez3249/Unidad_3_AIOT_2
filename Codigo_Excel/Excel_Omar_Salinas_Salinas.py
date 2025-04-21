from machine import Pin, ADC
from time import sleep
from network import WLAN, STA_IF
from urequests import post

# URL del WebApp de Google Apps Script
WEBAPP_URL = "https://script.google.com/macros/s/AKfycbwFp2KwuBzFVTpYkSZkgrHx0cujbDGNYZyxdmdyXApCxdt7oaCuizD7QX3etRcvdab_/exec"

temp_sensor = ADC(Pin(34))  
temp_sensor.atten(ADC.ATTN_11DB)  # Rango de voltaje hasta 3.3V
temp_sensor.width(ADC.WIDTH_12BIT)  # Resolución de 12 bits (0-4095)

# Conexión WiFi
def connect_wifi():
    sta_if = WLAN(STA_IF)
    if not sta_if.active():
        sta_if.active(True)
    if not sta_if.isconnected():
        sta_if.connect("Megacable_RdLp84U", "99uh6AmygyWEqfKzz2")
        print("Conectando a WiFi", end="")
        while not sta_if.isconnected():
            print(".", end="")
            sleep(0.3)
    print("\nWiFi conectado con IP:", sta_if.ifconfig()[0])

# Enviar temperatura a Google Sheets
def send_to_sheets(temp):
    data = {
        "temperatura": temp
    }
    try:
        response = post(WEBAPP_URL, json=data)
        print("Respuesta:", response.text)
        response.close()
    except Exception as e:
        print("Error al enviar a hoja de cálculo:", e)

# Convertir lectura analógica a grados Celsius
def leer_temperatura():
    valor_adc = temp_sensor.read()  # 0 - 4095
    voltaje = valor_adc * (3.3 / 4095)  # Conversión a voltaje (V)
    temperatura_c = voltaje * 100  # LM35: 10 mV por grado -> 1V = 100°C
    return temperatura_c

# Ejecutar
connect_wifi()

while True:
    try:
        temperatura = leer_temperatura()
        print(f"Temperatura: {temperatura:.2f} °C")
        print("-" * 25)
        send_to_sheets(temperatura)
    except Exception as e:
        print("Error en lectura del sensor:", e)
    sleep(5)
