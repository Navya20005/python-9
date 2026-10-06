class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if len(password) >= 8:
            self.__password = password
        else:
            print("Password must contain at least 8 characters")

    def login(self, username, password):
        if self.username == username and self.__password == password:
            print("Login successful")
        else:
            print("Invalid username or password")


user = User("navya", "navya1234")
user.login("navya", "navya1234")
user.login("navya", "wrong123")
user.password = "newpass123"
user.login("navya", "newpass123")