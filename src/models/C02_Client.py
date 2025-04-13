class Client:
    """
    Representa un cliente con información de identificación, contacto y dirección de envío.
    """

    def __init__(self, id: str, name: str, email: str, shipping_address: str):
        """
        Inicializa un nuevo cliente.

        :param id: Identificador único del cliente.
        :type id: str
        :param name: Nombre completo del cliente.
        :type name: str
        :param email: Correo electrónico del cliente.
        :type email: str
        :param shipping_address: Dirección de envío del cliente.
        :type shipping_address: str
        """
        self.__id = self.__strip_lower(id)
        self.__name = self.__strip_lower(name)
        self.__email = self.__strip_lower(email)
        self.__shipping_address = self.__strip_lower(shipping_address)

    @property
    def client_id(self):
        """
        Obtiene el ID del cliente.

        :return: ID del cliente.
        :rtype: str
        """
        return self.__id

    @client_id.setter
    def client_id(self, new_id):
        """
        Establece un nuevo ID para el cliente.

        :param new_id: Nuevo ID del cliente.
        :type new_id: str
        """
        self.__id = new_id

    @property
    def client_name(self):
        """
        Obtiene el nombre del cliente.

        :return: Nombre del cliente.
        :rtype: str
        """
        return self.__name

    @client_name.setter
    def client_name(self, new_name):
        """
        Establece un nuevo nombre para el cliente.

        :param new_name: Nuevo nombre del cliente.
        :type new_name: str
        """
        self.__name = new_name

    @property
    def email(self):
        """
        Obtiene el correo electrónico del cliente.

        :return: Email del cliente.
        :rtype: str
        """
        return self.__email

    @email.setter
    def email(self, new_email):
        """
        Establece un nuevo correo electrónico para el cliente.

        :param new_email: Nuevo email del cliente.
        :type new_email: str
        """
        self.__email = new_email

    @property
    def shipping_address(self):
        """
        Obtiene la dirección de envío del cliente.

        :return: Dirección de envío.
        :rtype: str
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, new_shipping_address):
        """
        Establece una nueva dirección de envío para el cliente.

        :param new_shipping_address: Nueva dirección de envío.
        :type new_shipping_address: str
        """
        self.__shipping_address = new_shipping_address

    def __str__(self):
        """
        Representación en cadena del cliente.

        :return: Descripción completa del cliente.
        :rtype: str
        """
        return f" ~ ID_Cliente: {self.client_id} ~ Nombre: {self.client_name} ~ Email: {self.email} ~ Dirección: {self.shipping_address}"

    def __strip_lower(self, string: str):
        """
        Normaliza una cadena eliminando espacios y convirtiéndola a minúsculas.

        :param string: Cadena a procesar.
        :type string: str
        :return: Cadena normalizada.
        :rtype: str
        """
        return str(string).strip().lower()
