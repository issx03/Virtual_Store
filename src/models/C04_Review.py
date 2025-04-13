#   CLASES NECESARIAS
from models.C01_Product import Product
from models.C02_Client import Client

#   DEFINICIÓN DE CLASE
class Review(Product, Client):
    def __init__(
        self,
        review_id: str,
        product: Product,
        client: Client,
        commentary: str,
        rating: int,
    ):
        #   Llamada al constructor de la clase padre Product
        Product.__init__(
            self, product.prod_id, product.prod_name, product.price, product.stock
        )
        #   Llamada al constructor de la clase padre Client
        Client.__init__(
            self,
            client.client_id,
            client.client_name,
            client.email,
            client.shipping_address,
        )

        #   ATRIBUTOS DE LA CLASE
        self.__id_reseña = Product._strip_lower(self, review_id)
        self.__commentary = Product._strip_lower(self, commentary)
        #   Normalizamos la puntuación
        if 0 <= rating <= 5:
            self.__rating = int(rating) 
        elif rating <= 0:
            self.__rating = 1
        else:
            self.__rating = 5

    #   GETTERS Y SETTERS DE LOS ATRIBUTOS
    @property
    def review_id(self):
        return self.__id_reseña

    @review_id.setter
    def review_id(self, new_id):
        self.__id_reseña = new_id

    @property
    def commentary(self):
        return self.__commentary

    @commentary.setter
    def commentary(self, new_comment):
        self.__commentary = new_comment

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, new_rate):
        self.__rating = new_rate

    #   MÉTODOS PRIVADOS DE LA CLASE
    def __str__(self):
        return f" ~ ID_Reseña: {self.review_id} ~ ID_Cliente: {self.client_id} ~ ID_Producto: {self.prod_id} ~ Comentario: {self.commentary} ~ Puntuación: {self.rating}"

    #   MÉTODOS PÚBLICOS DE LA CLASE
