class BaseSMTPResponseHandler:
    """Base class responsible for SMTP response handler."""
    _current_state = None

    def __init__(self, state):
        self.set_state(state)

    def set_state(self, state):
        self._current_state = state
        self._current_state.context = self

    def start_msg(self):
        return 'SMTP banner (Please enter HELO):\n'

    def render_response(self, request):
        return self._current_state.get_response(request)
