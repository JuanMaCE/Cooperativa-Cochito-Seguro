class User:
    def __init__(self, codigo: int, name: str, email: str, password: str, puesto: str):
        self.codigo = codigo
        self.name = name
        self.email = email
        self.__password = password
        self.puesto = puesto
        self.status = False

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    def __str__(self):
        return f'{self.codigo} - {self.name} - {self.email} - {self.password} - {self.puesto}'
