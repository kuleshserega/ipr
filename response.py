class BaseSMTPResponseHandler:
    """Base class responsible for SMTP response handler."""

    def __init__(self):
        self._current_state = 0
        self.states = {
            0: self.init_connection,
            1: self.ready_for_mailing,
            2: self.is_allowed_mail_from,
            3: self.receive_email_data,
        }
        self.email_msg = ''

    def render_response(self, request):
        return self.states[self._current_state](request)

    def init_connection(self, request):
        self._current_state += 1
        return 'SMTP banner (Please enter HELO):'

    def ready_for_mailing(self, request):
        if request == 'HELO':
            self._current_state += 1
            return 'SMTP server ready for mailing.'

        return 'Stage HELO failed. Please try again.'

    def is_allowed_mail_from(self, request):
        if 'gmail.com' in request:
            self._current_state += 1
            return 'Email address is allowed. Please add DATA:'

        return 'Email address is not allowed. Please try another one.'

    def receive_email_data(self, request):
        if request == '.':
            self.email_msg += '\n'
            return self.quit()

        self.email_msg = '{} {}\n'.format(self.email_msg, request)

    def quit(self):
        self._add_email_entry()
        return 'QUIT'

    def _add_email_entry(self):
        with open('emails.txt', 'a') as f:
            f.write(self.email_msg)
