from oauthlib.common import UNICODE_ASCII_CHARACTER_SET
from oauthlib.common import generate_client_id as oauthlib_generate_client_id

class BaseHashGenerator(object):
    def hash(self):
        raise NotImplementedError()
    
class ClientIDGenerator(BaseHashGenerator):
    def hash(self):
        length = 40
        chars = UNICODE_ASCII_CHARACTER_SET
        return oauthlib_generate_client_id(length=length, chars=chars)

class ClientSecretGenerator(BaseHashGenerator):
    def hash(self):
        length = 40
        chars = UNICODE_ASCII_CHARACTER_SET
        return oauthlib_generate_client_id(length=length, chars=chars)

def generate_client_id():
    client_id_generator = ClientIDGenerator()
    return client_id_generator.hash()

def generate_client_secret():
    client_secret_generator = ClientSecretGenerator()
    return client_secret_generator.hash()

    