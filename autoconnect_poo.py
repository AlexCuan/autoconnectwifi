from ping3 import ping
import os
import time


class Reconnect(object):
    SO = os.name

    def __init__(self, hostname, wifi_name, interface):
        self.hostname = hostname  # router's ip
        self.network_name = wifi_name
        self.interface_name = interface  # Wi-Fi, Ethernet, etc

    def is_connected(self):
        """
        Keeps sending ping and returning a boolean value
        """
        if ping(self.hostname):
            return True
        else:
            return False

    def stay_connected(self):
        """
        Information about connection state and reconnection
        """
        while self.is_connected():
            print("You are connected")
            time.sleep(2)

        else:
            print('Desconectado del WIFI ...')
            print('Ejecutando reconexión en WIFI ...')
            if self.SO == 'nt':
                os.system('netsh wlan connect name="' + self.network_name + '" interface="' + self.interface_name + '"')
            # elif self.SO == 'posix':
            #     os.system()
            # Need some linux programmer who helps me with connection stuff on linux

            time.sleep(1)
            self.stay_connected()


r = Reconnect("10.40.46.4", "Router", "Wi-Fi")

if __name__ == "__main__":
    r.stay_connected()
