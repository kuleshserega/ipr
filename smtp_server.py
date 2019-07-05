"""Base class of SMTP Server"""
import socket
from select import select

from settings import HOST, PORT, MSG_SIZE


to_monitor = []


class SMTPServer:
    """SMTP Server"""

    def __init__(self):
        """Init socket"""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
        )
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen()

    def _accept_connection(self, server_socket):
        client_socket, addr = self.server_socket.accept()
        to_monitor.append(client_socket)

    def _send_message(self, client_socket):
        request = client_socket.recv(MSG_SIZE)
        if request:
            response = 'Response from request: %s\n' % request
            client_socket.send(response.encode())
        else:
            client_socket.close()

    def _event_loop(self):
        while True:
            ready_to_read, _, _ = select(to_monitor, [], [])
            for sock in ready_to_read:
                if sock is self.server_socket:
                    self._accept_connection(sock)
                else:
                    self._send_message(sock)

    def start_server(self):
        """Start SMTP server"""
        to_monitor.append(self.server_socket)
        self._event_loop()


if __name__ == '__main__':
    server = SMTPServer()
    server.start_server()
