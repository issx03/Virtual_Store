#   CLASES NECESARIAS
from models.C01_Product import Product


#   DEFINICIÓN DE CLASE
class DigitalProduct(Product):
    def __init__(
        self,
        id: str,
        name: str,
        price: float,
        stock: int,
        format: str,
        file_size: float,
    ):
        super().__init__(id, name, price, stock)

        self.__format = self._strip_lower(format)
        self.__file_size = round(float(file_size), 2)

    #   GETTERS Y SETTERS DE LOS ATRIBUTOS
    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, new_format):
        self.__format = new_format

    @property
    def file_size(self):
        return self.__file_size

    @file_size.setter
    def file_size(self, new_file_size):
        self.__file_size = new_file_size

    #   MÉTODOS PRIVADOS DE LA CLASE
    def __str__(self):
        return f"{super().__str__()} ~ Formato: {self.format} ~ Tamaño de archivo: {self.file_size}"
    
    def _strip_lower(self, string):
        return super()._strip_lower(string)

    #   MÉTODOS PÚBLICOS DE LA CLASE
