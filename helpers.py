import random
import string

class Helpers:
    def random_email(self):
        return str(random.randint(100, 9999)) + '@testemails.kl'

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
