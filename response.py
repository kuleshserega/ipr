class BaseSMTPResponseHandler:
    """Base class responsible for SMTP response handler."""

    def __init__(self):
        self._current_state = 0
        self.states = {
            0: self.ready_for_mailing,
            1: self.is_allowed_mail_from,
            2: self.receive_email_data,
        }
        self.email_msg = ''

    def start_msg(self):
        return 'SMTP banner (Please enter HELO):\n'

    def render_response(self, request):
        return self.states[self._current_state](request)

    def ready_for_mailing(self, request):
        if request == 'HELO':
            self._current_state += 1
            return 'SMTP server ready for mailing.\n'

        return 'Stage HELO failed. Please try again.\n'

    def is_allowed_mail_from(self, request):
        if 'gmail.com' in request:
            self._current_state += 1
            return 'Email address is allowed. Please add DATA:\n'

        return 'Email address is not allowed. Please try another one.\n'

    def receive_email_data(self, request):
        if request == '.':
            self.email_msg += '\n'
            return self.quit()

        self.email_msg = '{} {}\n'.format(self.email_msg, request)
        return ''

    def quit(self):
        self._add_email_entry()
        return 'QUIT\n'

    def _add_email_entry(self):
        with open('emails.txt', 'a') as f:
            f.write(self.email_msg)
