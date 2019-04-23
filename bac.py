import socket

from zeroconf import ServiceInfo, Zeroconf


def registre_mdns(port):
    LOCAL_HOST = "alexa.local"
    LOCAL_PORT = port
    BASE_URL = "http://" + LOCAL_HOST + ":" + str(LOCAL_PORT) + "/"

    def get_local_address():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("www.amazon.com", 80))

        res = s.getsockname()[0]
        s.close()
        return res

    ip = get_local_address()
    print(f"Local IP is {ip}")

    desc = {
        'version': '0.1',
        'base_url': "http://{}:{}/".format(ip, str(LOCAL_PORT)),
        'path': '/'
    }
    info = ServiceInfo("_http._tcp.local.",
                       "Alexa Device._http._tcp.local.",
                       socket.inet_aton(ip), LOCAL_PORT, 0, 0,
                       desc, LOCAL_HOST + ".")

    zeroconf = Zeroconf()
    zeroconf.register_service(info)

    print(f"Local mDNS is started, domain is {LOCAL_HOST}")
    print(f"Local HTTP is {BASE_URL}")
