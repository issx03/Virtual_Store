#   CLASES NECESARIAS
from models.C02_Client import Client
from models.C01_Product import Product


#   DEFINICIÓN DE CLASE
class Order:
    def __init__(self, id: str, client: Client, date: str, products: list = []):
        self.__id = self.__strip_lower(id)
        self.__client = client
        self.__date = self.__strip_lower(date)
        self.__products = products

    @property
    def order_id(self):
        return self.__id

    @order_id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, new_client):
        self.__client = new_client

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, new_date):
        self.__date = new_date

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, new_prod):
        self.__products = new_prod

    #   MÉTODOS PRIVADOS DE LA CLASE
    def __str__(self):
        return f" ~ ID_Cliente: {self.client.client_id} ~ Dirección: {self.client.shipping_address} Productos (id): {[p.id for p in self.products]} Total: {self.calc_total()}"

    #   MÉTODOS PÚBLICOS DE LA CLASE
    def add_prod(self, prod: Product):
        self.products.append(prod)

    def calc_total(self):
        #   Sumamos los precios de cada uno de los productos de la lista
        return sum(p.price for p in self.products)
    
    def show_product(self):
        for p in self.products:
            print(p)
            
    def __strip_lower(self, string: str):
        return str(string).strip().lower()
