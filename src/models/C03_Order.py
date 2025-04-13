from models.C02_Client import Client
from models.C01_Product import Product


class Order:
    """
    Representa una orden de compra realizada por un cliente, incluyendo la lista de productos y la fecha.
    """

    def __init__(self, id: str, client: Client, date: str, products: list = []):
        """
        Inicializa una nueva orden.

        :param id: Identificador único de la orden.
        :type id: str
        :param client: Cliente que realiza la orden.
        :type client: Client
        :param date: Fecha de la orden.
        :type date: str
        :param products: Lista de productos en la orden.
        :type products: list[Product]
        """
        self.__id = self.__strip_lower(id)
        self.__client = client
        self.__date = self.__strip_lower(date)
        self.__products = products

    @property
    def order_id(self):
        """
        Obtiene el ID de la orden.

        :return: ID de la orden.
        :rtype: str
        """
        return self.__id

    @order_id.setter
    def id(self, new_id):
        """
        Establece un nuevo ID para la orden.

        :param new_id: Nuevo ID.
        :type new_id: str
        """
        self.__id = new_id

    @property
    def client(self):
        """
        Obtiene el cliente asociado a la orden.

        :return: Cliente.
        :rtype: Client
        """
        return self.__client

    @client.setter
    def client(self, new_client):
        """
        Establece un nuevo cliente para la orden.

        :param new_client: Cliente.
        :type new_client: Client
        """
        self.__client = new_client

    @property
    def date(self):
        """
        Obtiene la fecha de la orden.

        :return: Fecha.
        :rtype: str
        """
        return self.__date

    @date.setter
    def date(self, new_date):
        """
        Establece una nueva fecha para la orden.

        :param new_date: Fecha.
        :type new_date: str
        """
        self.__date = new_date

    @property
    def products(self):
        """
        Obtiene la lista de productos en la orden.

        :return: Lista de productos.
        :rtype: list[Product]
        """
        return self.__products

    @products.setter
    def products(self, new_prod):
        """
        Establece una nueva lista de productos para la orden.

        :param new_prod: Lista de productos.
        :type new_prod: list[Product]
        """
        self.__products = new_prod

    def __str__(self):
        """
        Representación en cadena de la orden, con cliente, dirección, productos y total.

        :return: Descripción completa de la orden.
        :rtype: str
        """
        return f" ~ ID_Cliente: {self.client.client_id} ~ Dirección: {self.client.shipping_address} Productos (id): {[p.id for p in self.products]} Total: {self.calc_total()}"

    def add_prod(self, prod: Product):
        """
        Agrega un producto a la orden.

        :param prod: Producto a agregar.
        :type prod: Product
        """
        self.products.append(prod)

    def calc_total(self):
        """
        Calcula el total del precio de todos los productos en la orden.

        :return: Total del precio.
        :rtype: float
        """
        return sum(p.price for p in self.products)

    def show_product(self):
        """
        Muestra por consola los productos contenidos en la orden.
        """
        for p in self.products:
            print(p)

    def __strip_lower(self, string: str):
        """
        Normaliza una cadena eliminando espacios y convirtiéndola a minúsculas.

        :param string: Cadena a procesar.
        :type string: str
        :return: Cadena normalizada.
        :rtype: str
        """
        return str(string).strip().lower()
