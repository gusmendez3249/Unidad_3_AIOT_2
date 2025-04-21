from machine import Pin
from time import sleep
from network import WLAN, STA_IF
from urequests import post

# URL del WebApp de Google Apps Script
WEBAPP_URL = "https://script.google.com/macros/s/AKfycbwFp2KwuBzFVTpYkSZkgrHx0cujbDGNYZyxdmdyXApCxdt7oaCuizD7QX3etRcvdab_/exec"

pir = Pin(14, Pin.IN)  # Ejemplo: D5 en NodeMCU corresponde a GPIO14

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

def send_to_sheets(motion_detected):
    data = {
        "movimiento": motion_detected  # 1 para movimiento, 0 para inactivo
    }
    try:
        response = post(WEBAPP_URL, json=data)
        print("Respuesta:", response.text)
        response.close()
    except Exception as e:
        print("Error al enviar a hoja de cálculo:", e)

connect_wifi()

while True:
    try:
        estado = pir.value()
        if estado == 1:
            print("Movimiento detectado")
        else:
            print("Sin movimiento")
        print("-" * 20)
        send_to_sheets(estado)
    except Exception as e:
        print("Error en lectura PIR:", e)
    sleep(4)
