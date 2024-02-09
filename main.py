import time
import troubleshooting


host = {
    '192.168.1.240': 0,
    '192.168.1.250': 0
}
failure = 0

running = True
while running:
    result = troubleshooting.checkhostonline(host)
    if result == 0:
        failure += 1
    # if failure > 3:

    time.sleep(5)