from models.C01_Product import Product

class DigitalProduct(Product):
    """
    Representa un producto digital, que hereda de Product, con formato y tamaño de archivo.
    """

    def __init__(
        self,
        id: str,
        name: str,
        price: float,
        stock: int,
        format: str,
        file_size: float,
    ):
        """
        Inicializa un nuevo producto digital.

        :param id: Identificador del producto.
        :type id: str
        :param name: Nombre del producto.
        :type name: str
        :param price: Precio del producto.
        :type price: float
        :param stock: Cantidad de unidades disponibles.
        :type stock: int
        :param format: Formato del archivo digital (ej: PDF, MP3).
        :type format: str
        :param file_size: Tamaño del archivo en MB.
        :type file_size: float
        """
        super().__init__(id, name, price, stock)

        self.__format = self._strip_lower(format)
        self.__file_size = round(float(file_size), 2)

    @property
    def format(self):
        """
        Obtiene el formato del producto digital.

        :return: Formato del archivo.
        :rtype: str
        """
        return self.__format

    @format.setter
    def format(self, new_format):
        """
        Establece un nuevo formato para el producto digital.

        :param new_format: Nuevo formato del archivo.
        :type new_format: str
        """
        self.__format = new_format

    @property
    def file_size(self):
        """
        Obtiene el tamaño del archivo del producto digital.

        :return: Tamaño del archivo en MB.
        :rtype: float
        """
        return self.__file_size

    @file_size.setter
    def file_size(self, new_file_size):
        """
        Establece un nuevo tamaño de archivo.

        :param new_file_size: Nuevo tamaño en MB.
        :type new_file_size: float
        """
        self.__file_size = new_file_size

    def __str__(self):
        """
        Representación en cadena del producto digital, incluyendo atributos heredados y propios.

        :return: Descripción completa del producto digital.
        :rtype: str
        """
        return f"{super().__str__()} ~ Formato: {self.format} ~ Tamaño de archivo: {self.file_size}"

    def _strip_lower(self, string):
        """
        Normaliza una cadena eliminando espacios y convirtiéndola a minúsculas.

        :param string: Cadena a normalizar.
        :type string: str
        :return: Cadena normalizada.
        :rtype: str
        """
        return super()._strip_lower(string)
