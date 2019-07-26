from response import BaseSMTPResponseHandler
from exceptions import SMTPConnectionClosedException
from settings import MSG_SIZE


class SMTPSession:
    """SMTP Session contains connections with client sockets."""
    def __init__(self):
        self.connection_handlers = dict()
        self.connection_handler = None

    def attach_conection(self, client_socket):
        handler = BaseSMTPResponseHandler()
        start_msg = handler.start_msg()
        client_socket.send(start_msg.encode())
        connection_id = client_socket.fileno()
        self.connection_handlers[connection_id] = handler

    def init_connection(self, client_socket):
        connection_id = client_socket.fileno()
        if connection_id not in self.connection_handlers:
            self.attach_conection(client_socket)

        self.connection_handler = self.connection_handlers[connection_id]

    def _process_request(self, client_socket):
        try:
            request = self._read_request(client_socket)
            cleaned_request = request.decode().replace('\n', '')
            return self.connection_handler.render_response(cleaned_request)
        except SMTPConnectionClosedException as e:
            client_socket.close()
            print(e)

    def _read_request(self, client_socket):
        request = client_socket.recv(MSG_SIZE)
        if request:
            return request

        raise SMTPConnectionClosedException('Connection closed\n')

    def make_response(self, client_socket):
        response = self._process_request(client_socket)
        return response
