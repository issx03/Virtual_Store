import os

def clear():
    """
    Limpia la pantalla de la terminal.

    Utiliza el comando 'clear' de sistema operativo para limpiar la consola. 
    Esto se ejecuta a través de la función `os.system()`.

    :return: None
    """
    os.system('clear')


def pause():
    """
    Pausa la ejecución del programa y espera que el usuario presione ENTER.

    Muestra un mensaje indicando que el usuario debe pulsar ENTER para continuar.

    :return: None
    """
    input('\nPulsa ENTER para continuar...')


def print_error(text: str):
    """
    Imprime un mensaje de error.

    Imprime el texto proporcionado como un mensaje de error, asegurándose de que
    el primer carácter sea mayúscula y agregando un prefijo `!->` para indicar que es un error.

    :param text: Mensaje de error a imprimir.
    :type text: str
    :return: None
    """
    print(f'\n !-> {text.capitalize()}')


def generate_border(length):
    """
    Genera una línea de borde de longitud personalizada.

    Crea una cadena de caracteres `+` de longitud ajustada a la longitud proporcionada
    más un margen adicional de 10 caracteres.

    :param length: Longitud de la línea de borde sin contar el margen.
    :type length: int
    :return: Línea de borde generada.
    :rtype: str
    """
    return "+" * (length + 10)


def menu_options(*options: str, name="menu") -> str:
    """
    Genera un menú con opciones numeradas.

    Crea un menú con las opciones proporcionadas y un título. La opción de salida 
    (0) siempre estará presente como la primera opción.

    :param options: Opciones del menú que se van a mostrar.
    :type options: str
    :param name: Nombre del menú. Por defecto es "menu".
    :type name: str
    :return: Cadena con el menú generado.
    :rtype: str
    """
    border = generate_border(len(name))
    # Creamos el título del menú
    menu = f"""
        {border}
        +    {name.strip(" ").upper()}    +
        {border}
    """

    # Le agregamos la opción SALIR como opción cero siempre
    menu += "\n\t0. SALIR"
    # Recorremos los valores de la opción y su número
    for num, option in enumerate(options, start=1):
        # Agregamos cada una de las opciones al menú
        menu += f"\n\t{num}. {option.strip().upper()}"

    menu += "\n"

    return menu


def menu_titles(name: str) -> str:
    """
    Genera un título de menú con borde.

    Crea un título formateado para el menú con un borde de `+` alrededor del nombre
    proporcionado. La longitud del borde se ajusta al largo del nombre.

    :param name: Nombre del título.
    :type name: str
    :return: Título de menú con borde.
    :rtype: str
    """
    # Bucamos la longitud para saber el borde del título del menú
    border = generate_border(len(name))
    # Creamos el título formateado
    name = f"""
        {border}
        +    {name.strip().upper()}    +
        {border}
    """

    return name
