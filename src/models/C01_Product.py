#   DEFINICIÓN DE CLASE
class Product:
    """
    Representa un producto con ID, nombre, precio y stock.
    """

    def __init__(self, id: str, name: str, price: float, stock: int):
        """
        Inicializa un nuevo producto.

        :param id: Identificador único del producto.
        :type id: str
        :param name: Nombre del producto.
        :type name: str
        :param price: Precio del producto.
        :type price: float
        :param stock: Cantidad de unidades en stock.
        :type stock: int
        """
        self.__id = self._strip_lower(id)
        self.__name = self._strip_lower(name)
        self.__price = round(float(price), 2)
        self.__stock = round(int(stock), 2)

    #   GETTERS Y SETTERS DE LOS ATRIBUTOS
    @property
    def prod_id(self):
        """
        Obtiene el ID del producto.

        :return: ID del producto.
        :rtype: str
        """
        return self.__id

    @prod_id.setter
    def prod_id(self, new_id):
        """
        Establece un nuevo ID para el producto.

        :param new_id: Nuevo ID del producto.
        :type new_id: str
        """
        self.__id = new_id

    @property
    def prod_name(self):
        """
        Obtiene el nombre del producto.

        :return: Nombre del producto.
        :rtype: str
        """
        return self.__name

    @prod_name.setter
    def prod_name(self, new_name):
        """
        Establece un nuevo nombre para el producto.

        :param new_name: Nuevo nombre del producto.
        :type new_name: str
        """
        self.__name = new_name

    @property
    def price(self):
        """
        Obtiene el precio del producto.

        :return: Precio del producto.
        :rtype: float
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Establece un nuevo precio para el producto.

        :param new_price: Nuevo precio del producto.
        :type new_price: float
        """
        self.__price = new_price

    @property
    def stock(self):
        """
        Obtiene la cantidad de stock del producto.

        :return: Stock disponible.
        :rtype: int
        """
        return self.__stock

    @stock.setter
    def stock(self, new_stock):
        """
        Establece una nueva cantidad de stock para el producto.

        :param new_stock: Nueva cantidad de stock.
        :type new_stock: int
        """
        self.__stock = new_stock

    #   MÉTODOS PRIVADOS DE LA CLASE
    def __str__(self):
        """
        Representación en cadena del producto.

        :return: Cadena con los detalles del producto.
        :rtype: str
        """
        return f" ~ ID: {self.prod_id.upper()} ~ Nombre: {self.prod_name} ~ Precio: {self.price} ~ Stock {self.stock}"

    def _strip_lower(self, string: str):
        """
        Elimina espacios y convierte a minúsculas una cadena.

        :param string: Cadena de texto a procesar.
        :type string: str
        :return: Cadena normalizada (sin espacios y en minúsculas).
        :rtype: str
        """
        return str(string).strip().lower()

    #   MÉTODOS PÚBLICOS DE LA CLASE
    def act_stock(self, quantity: int):
        """
        Actualiza la cantidad de stock del producto.

        :param quantity: Nueva cantidad de stock.
        :type quantity: int
        """
        self.stock = quantity
