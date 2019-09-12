from smtp_states import SMTPHelloState


class BaseSMTPResponseHandler:
    """Base class responsible for SMTP response handler."""

    def __init__(self):
        self._current_state = SMTPHelloState()

    def start_msg(self):
        return 'SMTP banner (Please enter HELO):\n'

    def render_response(self, request):
        return self._current_state.send_response(request)
