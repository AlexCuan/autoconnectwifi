import requests
from ping3 import ping
import os
import time

hostname = '192.168.43.1'  # router's ip
wifi_name = 'Alquenda'
interface_name = 'Wi-Fi'  # Wi-Fi, Ethernet, etc

while True:
    i = 1
    count_ok_connect = 0
    count_ok_connect_total = 0
    while i <= 4:
        p = ping(hostname)

        if p:
            estado_conexion = "Connected"
            count_ok_connect = count_ok_connect + 1
        else:
            estado_conexion = "error"

        print("Estado de conexion del WIFI : ", estado_conexion)
        i = i + 1
        time.sleep(1)

    print("4 ping enviados : ", count_ok_connect, " recibidos")
    if count_ok_connect == 0:
        print('Desconectado del WIFI ...')
        print('Ejecutando reconexión en WIFI ...')
        response = os.system('netsh wlan connect name="' + wifi_name + '" interface="' + interface_name + '"')
    else:
        print('Conectado al WIFI ...')
