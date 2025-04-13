# LIBRERÍAS
import os

# FUNCIONES
def clear():
    os.system('clear')

def pause():
    input('\nPulsa ENTER para continuar...')

def print_error(text: str):
    print(f'\n !-> {text.capitalize()}')

def generate_border(length):
    return "+" * (length + 10)

def menu_options(*options:str, name="menu") -> str:
    border = generate_border(len(name))
    #   Creamos el título del menú
    menu = f"""
        {border}
        +    {name.strip(" ").upper()}    +
        {border}
    """

    #   Le agregamos la opción SALIR como opción cero siempre
    menu += "\n\t0. SALIR"
    #   Recorremos los valores de la opción y su número
    for num,option in enumerate(options,start=1):
        #   Agregamos cada una de las opciones al menú
        menu += f"\n\t{num}. {option.strip().upper()}"

    menu += "\n"

    return menu

def menu_titles(name: str) -> str:
    #   Bucamos la longitud para saber el borde del título del menú
    border = generate_border(len(name))
    # Creamos el título formateado
    name = f"""
        {border}
        +    {name.strip().upper()}    +
        {border}
    """

    return name
