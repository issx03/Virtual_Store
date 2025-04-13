def generate_input(*data):
    """
    Solicita entradas al usuario para cada parámetro dado y devuelve una lista de respuestas.

    :param data: Parámetros de entrada que serán solicitados al usuario.
    :type data: str
    :return: Lista de respuestas ingresadas por el usuario.
    :rtype: list[str]
    """
    return [input(f" -> {d.capitalize()}: ").strip().lower() for d in data]


def generate_id(prefix: str, list: list):
    """
    Genera un nuevo identificador basado en un prefijo y una lista de IDs existentes.

    Si la lista no está vacía, toma el ID más alto, le suma 1 y lo devuelve con formato de 3 dígitos.
    Si la lista está vacía, retorna el prefijo seguido de "001".

    :param prefix: Prefijo que se usará para generar el ID.
    :type prefix: str
    :param list: Lista de IDs existentes.
    :type list: list[str]
    :return: Nuevo ID generado.
    :rtype: str
    """
    if list:
        return f"{prefix.strip()}{(max([int(id[len(prefix)+1:]) for id in list]) + 1):0>3}"
    
    return f"{prefix}001"
