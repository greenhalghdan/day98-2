import os
import ping3
import sendemail

def checkhostonline(host):
    for x in host:
        result = ping3.ping(f"{ x }")
        print(x, host[x])
        if result == False:
            host[x] += 1
        if result != False:
            if host[x] != 0:
                host[x] -= 1
    for x in list(host):
        if host[x] == 3:
            sendemail.email(x)
            host.pop(x)
    print(host)
    return host