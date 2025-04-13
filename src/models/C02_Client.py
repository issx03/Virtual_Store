#   DEFINICIÓN DE CLASE
class Client:
    def __init__(self, id: str, name: str, email: str, shipping_address: str):
        self.__id = self.__strip_lower(id)
        self.__name = self.__strip_lower(name)
        self.__email = self.__strip_lower(email)
        self.__shipping_address = self.__strip_lower(shipping_address)

    #   GETTERS Y SETTERS DE LOS ATRIBUTOS
    @property
    def client_id(self):
        return self.__id

    @client_id.setter
    def client_id(self, new_id):
        self.__id = new_id

    @property
    def client_name(self):
        return self.__name

    @client_name.setter
    def client_name(self, new_name):
        self.__name = new_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def shipping_address(self):
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, new_shipping_address):
        self.__shipping_address = new_shipping_address

    #   MÉTODOS PRIVADOS DE LA CLASE
    def __str__(self):
        return f" ~ ID_Cliente: {self.client_id} ~ Nombre: {self.client_name} ~ Email: {self.email} ~ Dirección: {self.shipping_address}"

    def __strip_lower(self, string: str):
        return str(string).strip().lower()

    #   MÉTODOS PÚBLICOS DE LA CLASE
