import requests
import os
import time

hostname = 'http://192.168.100.3'
wifiname = '(0__0)'
interfacename = 'wlan2'

while 1 == 1:
        i = 1
        countokconnect = 0
        countokconnecttotal = 0
        while i <= 4:
                try: 
                        session = requests.Session()
                        response = session.get( hostname )
                        estado = response.status_code
                        
                        if estado == 200:
                                estado_script = "200"
                                countokconnect = countokconnect + 1
                except:
                        estado_script = "error"     

                print( "Estado de Conexion del WIFI : ", estado_script )
                i = i + 1
                time.sleep(1)

        print( "4 HTTP GET CONNECT enviados : ", countokconnect ," resividos" )      
        if countokconnect == 0:
                print('Desconectado del WIFI ...')
                print('Ejecutando reconexion en WIFI ...')
                response = os.system("netsh wlan connect name='"+wifiname+"' interface='"+interfacename+"'' ")
        else:
                print('Conectado al WIFI ...')
