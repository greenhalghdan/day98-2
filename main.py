import time
import troubleshooting


host = {
    '192.168.1.240': 0,
    '192.168.1.250': 0
}

running = True
while running:
    troubleshooting.checkhostonline(host)

    time.sleep(5)