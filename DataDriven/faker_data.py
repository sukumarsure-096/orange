from faker import Faker

class FakeData:

    def __init__(self):
        self.faker = Faker()

    def get_user_name(self):
        return self.faker.user_name()

    def get_password(self):
        return self.faker.password()
    
