from machine import Pin, ADC
from time import sleep
from network import WLAN, STA_IF
from urequests import post

# URL del Google Apps Script WebApp
WEBAPP_URL = "https://script.google.com/macros/s/AKfycbwFp2KwuBzFVTpYkSZkgrHx0cujbDGNYZyxdmdyXApCxdt7oaCuizD7QX3etRcvdab_/exec"

joystick_x = ADC(Pin(32))  # Eje X
joystick_y = ADC(Pin(33))  # Eje Y

# Ajustes del ADC
joystick_x.atten(ADC.ATTN_11DB)
joystick_y.atten(ADC.ATTN_11DB)

# Conectar a WiFi
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

# Enviar valores del joystick
def send_to_sheets(x_val, y_val):
    data = {
        "joystick_x": x_val,
        "joystick_y": y_val
    }
    try:
        response = post(WEBAPP_URL, json=data)
        print("Respuesta:", response.text)
        response.close()
    except Exception as e:
        print("Error al enviar a hoja de cálculo:", e)

# Ejecutar
connect_wifi()

while True:
    try:
        x = joystick_x.read()
        y = joystick_y.read()
        print(f"Joystick X: {x} | Joystick Y: {y}")
        print("-" * 25)
        send_to_sheets(x, y)
    except Exception as e:
        print("Error en lectura del joystick:", e)
    sleep(3)
