from ping3 import ping
import os
import time


class Reconnect(object):
    SO = os.name

    def __init__(self, hostname, wifi_name, interface):
        self.hostname = hostname
        self.network_name = wifi_name
        self.interface_name = interface

    def is_connected(self):
        if ping(self.hostname):
            return True
        else:
            return False

    def stay_connected(self):
        while self.is_connected():
            print("You are connected")
            time.sleep(2)

        else:
            print('Desconectado del WIFI ...')
            print('Ejecutando reconexión en WIFI ...')
            if self.SO == 'nt':
                os.system('netsh wlan connect name="' + self.network_name + '" interface="' + self.interface_name + '"')
            elif self.SO == 'posix':
                os.system()

            time.sleep(1)
            self.stay_connected()


r = Reconnect("10.40.46.4", "Router", "Wi-Fi")

if __name__ == "__main__":
    r.stay_connected()
