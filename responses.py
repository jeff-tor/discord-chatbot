import random
import datetime

def handle_response(self, message: str = None):

    self.message = message

    parse_message = self.message.lower()

    if parse_message == 'hello':
        return 'hey there'

    if parse_message == 'roll':
        return str(random.randint(1,100))

    if parse_message == 'current time':
        return datetime.datetime.utcnow()


