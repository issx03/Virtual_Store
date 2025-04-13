#   DEFINICIÓN DE CLASE
class Product:
    def __init__(self, id: str, name: str, price: float, stock: int):
        self.__id = self._strip_lower(id)
        self.__name = self._strip_lower(name)
        self.__price = round(float(price), 2)
        self.__stock = round(int(stock), 2)

    #   GETTERS Y SETTERS DE LOS ATRIBUTOS
    @property
    def prod_id(self):
        return self.__id

    @prod_id.setter
    def prod_id(self, new_id):
        self.__id = new_id

    @property
    def prod_name(self):
        return self.__name

    @prod_name.setter
    def prod_name(self, new_name):
        self.__name = new_name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, new_stock):
        self.__stock = new_stock

    #   MÉTODOS PRIVADOS DE LA CLASE
    def __str__(self):
        return f" ~ ID: {self.prod_id.upper()} ~ Nombre: {self.prod_name} ~ Precio: {self.price} ~ Stock {self.stock}"
    def _strip_lower(self, string: str):
        return str(string).strip().lower()

    #   MÉTODOS PÚBLICOS DE LA CLASE
    def act_stock(self, quantity: int):
        self.stock = quantity
