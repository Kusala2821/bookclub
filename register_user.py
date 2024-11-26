'''import hashlib
from baseObject import baseObject

class User(baseObject):
    def __init__(self):
        self.setup()
        self.tn = 'user' 

    def hash_password(self, password):
        password = password + 'xyz'
        return hashlib.md5(password.encode('utf-8')).hexdigest()

    def verify_new(self, n=0):
        self.errors = []

        # Username validation
        if self.data[n]['username'] == '':
            self.errors.append('Username cannot be blank.')
        else:
            existing_user = User()
            existing_user.get_by_field('username', self.data[n]['username'])
            if len(existing_user.data) > 0:
                self.errors.append('Username already in use.')

        # Password validation
        if len(self.data[n]['password']) < 3:
            self.errors.append('Password needs to be more than 3 chars.')
        elif self.data[n]['password'] != self.data[n]['confirm_password']:
            self.errors.append('Passwords do not match.')
        else:
            self.data[n]['password'] = self.hash_password(self.data[n]['password'])

        return len(self.errors) == 0

    def register_user(self, username, password, confirm_password):
        self.data[0]['username'] = username
        self.data[0]['password'] = password
        self.data[0]['confirm_password'] = confirm_password

        if self.verify_new():
            self.insert()
            return True
        else:
            print(f"Registration errors: {self.errors}")
            return False'''
