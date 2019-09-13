from abc import ABCMeta, abstractmethod


class BaseSMTPState(metaclass=ABCMeta):
    """Base SMTP response State class."""
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def get_response(self, request):
        pass


class SMTPHelloState(BaseSMTPState):

    def get_response(self, request):
        if request == 'HELO':
            self.context.set_state(SMTPMailFromState())
            return 'SMTP server ready for mailing.\n'

        return 'Stage HELO failed. Please try again.\n'


class SMTPMailFromState(BaseSMTPState):

    def get_response(self, request):
        if 'gmail.com' in request:
            self.context.set_state(SMTPGetTextState())
            return 'Email address is allowed. Please add DATA:\n'

        return 'Email address is not allowed. Please try another one.\n'


class SMTPGetTextState(BaseSMTPState):
    email_msg = ''

    def get_response(self, request):
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
