from models.C01_Product import Product
from models.C02_Client import Client


class Review(Product, Client):
    """
    Representa una reseña hecha por un cliente sobre un producto.

    Hereda de:
        - Product: para asociar la reseña al producto evaluado.
        - Client: para asociar la reseña al cliente que la realiza.
    """

    def __init__(
        self,
        review_id: str,
        product: Product,
        client: Client,
        commentary: str,
        rating: int,
    ):
        """
        Inicializa una reseña con información del producto, cliente, comentario y puntuación.

        :param review_id: Identificador único de la reseña.
        :type review_id: str
        :param product: Producto evaluado.
        :type product: Product
        :param client: Cliente que realiza la reseña.
        :type client: Client
        :param commentary: Comentario del cliente.
        :type commentary: str
        :param rating: Puntuación de la reseña (0 a 5).
        :type rating: int
        """
        Product.__init__(
            self, product.prod_id, product.prod_name, product.price, product.stock
        )
        Client.__init__(
            self,
            client.client_id,
            client.client_name,
            client.email,
            client.shipping_address,
        )

        self.__id_reseña = Product._strip_lower(self, review_id)
        self.__commentary = Product._strip_lower(self, commentary)
        self.__rating = (
            int(rating)
            if 0 <= rating <= 5
            else 1
            if rating <= 0
            else 5
        )

    @property
    def review_id(self):
        """
        Obtiene el ID de la reseña.

        :return: ID de la reseña.
        :rtype: str
        """
        return self.__id_reseña

    @review_id.setter
    def review_id(self, new_id):
        """
        Establece un nuevo ID para la reseña.

        :param new_id: Nuevo ID.
        :type new_id: str
        """
        self.__id_reseña = new_id

    @property
    def commentary(self):
        """
        Obtiene el comentario de la reseña.

        :return: Comentario.
        :rtype: str
        """
        return self.__commentary

    @commentary.setter
    def commentary(self, new_comment):
        """
        Establece un nuevo comentario para la reseña.

        :param new_comment: Comentario nuevo.
        :type new_comment: str
        """
        self.__commentary = new_comment

    @property
    def rating(self):
        """
        Obtiene la puntuación de la reseña.

        :return: Puntuación (entre 1 y 5).
        :rtype: int
        """
        return self.__rating

    @rating.setter
    def rating(self, new_rate):
        """
        Establece una nueva puntuación para la reseña.

        :param new_rate: Nueva puntuación (entre 1 y 5).
        :type new_rate: int
        """
        self.__rating = new_rate

    def __str__(self):
        """
        Representación en cadena de la reseña.

        :return: Descripción de la reseña con ID, cliente, producto, comentario y puntuación.
        :rtype: str
        """
        return f" ~ ID_Reseña: {self.review_id} ~ ID_Cliente: {self.client_id} ~ ID_Producto: {self.prod_id} ~ Comentario: {self.commentary} ~ Puntuación: {self.rating}"
