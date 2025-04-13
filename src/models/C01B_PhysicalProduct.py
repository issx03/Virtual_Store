#   CLASES NECESARIAS
from models.C01_Product import Product


#   DEFINICIÓN DE CLASE
class PhysicalProduct(Product):
    def __init__(
        self,
        id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        dimensions: str,
    ):
        super().__init__(id, name, price, stock)

        self.__weight = float(weight)
        self.__dimensions = self._strip_lower(dimensions)

    #   GETTERS Y SETTERS DE LOS ATRIBUTOS
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, new_dimensions):
        self.__dimensions = new_dimensions

    #   MÉTODOS PRIVADOS DE LA CLASE
    def __str__(self):
        return f"{super().__str__()} ~ Peso: {self.weight} ~ Dimensiones: {self.dimensions}"

    #   MÉTODOS PÚBLICOS DE LA CLASE
