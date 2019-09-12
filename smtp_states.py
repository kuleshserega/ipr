from abc import ABCMeta, abstractmethod


class BaseSMTPState(metaclass=ABCMeta):
    """Base SMTP response State class."""
    @abstractmethod
    def send_response(self, request):
        pass


class SMTPHelloState(BaseSMTPState):

    def send_response(self, request):
        if request == 'HELO':
            return 'SMTP server ready for mailing.\n'

        return 'Stage HELO failed. Please try again.\n'


class SMTPMailFromState(BaseSMTPState):

    def send_response(self, request):
        if 'gmail.com' in request:
            return 'Email address is allowed. Please add DATA:\n'

        return 'Email address is not allowed. Please try another one.\n'


class SMTPMailFromState(BaseSMTPState):
    email_msg = ''

    def send_response(self, request):
        if request == '.':
            self.email_msg += '\n'
            return self._quit()

        self.email_msg = '{} {}\n'.format(self.email_msg, request)
        return ''

    def _quit(self):
        self._add_email_entry()
        return 'QUIT\n'

    def _add_email_entry(self):
        with open('emails.txt', 'a') as f:
            f.write(self.email_msg)
