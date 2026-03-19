import socks
import socket
import subprocess
import time 
# unused unless you plan on adding socks


# add more if you want. 

class transport:
    def dns_config(self):
        return {
            "nameserver": "127.0.0.1",
            "port": 9053,
            "timeout": 5,
            "lifetime": 5
        }
    
    def enable_tor(self):
        subprocess.Popen(
        ["cmd", "/c", "start", "Tor", "tor.bat"],
        shell=True
         )
        
        time.sleep(10)

        socks.set_default_proxy(
           socks.SOCKS5,
           "127.0.0.1",
           9050,
            )
        socket.socket = socks.socksocket

    def disable_tor(self):
       socket.socket = socket._socketobject  # restore if needed

    







