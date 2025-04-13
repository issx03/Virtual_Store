from models.C01_Product import Product


class PhysicalProduct(Product):
    """
    Representa un producto físico, que hereda de Product, con peso y dimensiones.
    """

    def __init__(
        self,
        id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        dimensions: str,
    ):
        """
        Inicializa un nuevo producto físico.

        :param id: Identificador del producto.
        :type id: str
        :param name: Nombre del producto.
        :type name: str
        :param price: Precio del producto.
        :type price: float
        :param stock: Cantidad de unidades disponibles.
        :type stock: int
        :param weight: Peso del producto en kilogramos.
        :type weight: float
        :param dimensions: Dimensiones físicas del producto (ej. "30x20x15 cm").
        :type dimensions: str
        """
        super().__init__(id, name, price, stock)

        self.__weight = float(weight)
        self.__dimensions = self._strip_lower(dimensions)

    @property
    def weight(self):
        """
        Obtiene el peso del producto.

        :return: Peso en kilogramos.
        :rtype: float
        """
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        """
        Establece un nuevo peso para el producto.

        :param new_weight: Nuevo peso en kilogramos.
        :type new_weight: float
        """
        self.__weight = new_weight

    @property
    def dimensions(self):
        """
        Obtiene las dimensiones del producto.

        :return: Dimensiones físicas del producto.
        :rtype: str
        """
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, new_dimensions):
        """
        Establece nuevas dimensiones para el producto.

        :param new_dimensions: Nuevas dimensiones físicas del producto.
        :type new_dimensions: str
        """
        self.__dimensions = new_dimensions

    def __str__(self):
        """
        Representación en cadena del producto físico, incluyendo atributos heredados y propios.

        :return: Descripción completa del producto físico.
        :rtype: str
        """
        return f"{super().__str__()} ~ Peso: {self.weight} ~ Dimensiones: {self.dimensions}"
