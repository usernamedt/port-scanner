import socket


class Scanner:
    def __init__(self, timeout=1):
        self.__port_timeout = timeout

    def scan_range(self, host, start, end):
        for port in range(start, end + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.__port_timeout)
                try:
                    sock.connect((host, port))
                    print(f'{host}:{port} OPENED')
                except:
                    print(f'{host}:{port} CLOSED')
