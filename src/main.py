#   CLASES NECESARIAS
from models.C01_Product import Product
from models.C01A_DigitalProduct import DigitalProduct
from models.C01B_PhysicalProduct import PhysicalProduct
from models.C02_Client import Client
from models.C03_Order import Order
from models.C04_Review import Review

#   MÓDULOS Y LIBRERÍAS
from modules.menu_utils import clear, pause, print_error, menu_options, menu_titles
from modules.menu_functions import generate_input, generate_id


def menu():
    avaible_products = list()
    registred_clients = dict()
    orders_placed = dict()

    # MENÚ PRINCIPAL
    while True:
        clear()
        print(
            menu_options(
                "gestionar clientes",
                "gestionar productos",
                "gestionar pedidos",
                "gestionar reseñas",
            )
        )

        option = input("Elige una de las opciones del menú: ")

        clear()

        match option:
            case "0":
                print("\nHasta luego")
            case "1":
                while True:
                    clear()
                    print(
                        menu_options(
                            "Añadir un Cliente",
                            "Mostrar todos los clientes",
                            name="Gestionar clientes",
                        )
                    )
                    op = input(" -> Elige una de las opciones: ")
                    clear()
                    match op:
                        case "0":
                            break
                        case "1":
                            print(menu_titles("crear un cliente"))
                            #   Generamos la información del nuevo cliente
                            new_id = generate_id("C", registred_clients.keys())
                            client_data = generate_input(
                                "nombre", "email", "dirección de envio"
                            )
                            #   Creamos el objeto
                            registred_clients[new_id] = Client(new_id, *client_data)
                            print(" -> Cliente creado correctamente.")

                        case "2":
                            print(menu_titles("mostrar todos los clientes"))
                            if registred_clients:
                                for c in registred_clients.values():
                                    print(c)
                            else:
                                print_error(
                                    "No se ha registrado ningún cliente por el momento"
                                )
                        case _:
                            print_error("elige una de las opciones del menú")
                    pause()

            case "2":
                while True:
                    clear()
                    print(
                        menu_options(
                            "Añadir un Producto",
                            "Añadir un Producto digital",
                            "Añadir un Producto Físico",
                            "Actualizar stock",
                            "Mostrar todos los productos",
                            name="Gestionar productos",
                        )
                    )
                    prod_option = input(" -> Elige una de las opciones: ")

                    clear()
                    match prod_option:
                        case "0":
                            break
                        case "1":
                            print(menu_titles("agregar producto"))
                            #   Generamos la información del nuevo producto
                            prod_data = generate_input(
                                "Introduce el nombre del producto", "Precio", "Stock"
                            )
                            new_id = generate_id("P", [p.prod_id for p in avaible_products])
                            #   Creamos el objeto en un entorno controlado
                            try:
                                avaible_products.append(Product(new_id, *prod_data))
                            except ValueError as e:
                                print_error(f"Se ha producido un error de tipo: {e}")
                        case "2":
                            print(menu_titles("agregar producto digital"))
                            prod_data = generate_input(
                                "Introduce el nombre del producto", "Precio", "Stock"
                            )
                            #   Generamos la información específica para productos digitales
                            new_id = generate_id("PD", [p.prod_id for p in avaible_products])
                            dig_prod_data = prod_data + generate_input(
                                "Formato", "Tamaño de archivo (solo el número)"
                            )
                            #   Creamos el objeto en un entorno controlado
                            try:
                                avaible_products.append(
                                    DigitalProduct(new_id, *dig_prod_data)
                                )
                            except ValueError as e:
                                print_error(f"Se ha producido un error de tipo: {e}")
                        case "3":
                            print(menu_titles("agregar producto físico"))
                            prod_data = generate_input(
                                "Introduce el nombre del producto", "Precio", "Stock"
                            )
                            #   Generamos la información específica para productos digitales
                            new_id = generate_id("PF", [p.prod_id for p in avaible_products])
                            physical_prod_data = prod_data + generate_input(
                                "Peso", "Dimensiones"
                            )
                            #   Creamos el objeto en un entorno controlado
                            try:
                                avaible_products.append(
                                    PhysicalProduct(new_id, *physical_prod_data)
                                )
                            except ValueError as e:
                                print_error(f"Se ha producido un error de tipo: {e}")
                        case "4":
                            print(menu_titles("actualizar stock de un producto"))
                            prod_id = input(" -> Introduce el ID del producto: ")

                            for p in avaible_products:
                                if prod_id.strip().lower() == p.prod_id:
                                    quantity = input(
                                        " -> Introduce la nueva cantidad: "
                                    )
                                    p.stock = quantity
                                    print(" -> Stock modificado correctamente")
                                    break
                            else:
                                print_error(
                                    "el producto con el ID introducido no existe"
                                )

                        case "5":
                            print(menu_titles("mostrar todos los productos"))
                            if avaible_products:
                                for p in avaible_products:
                                    print(p)
                            else:
                                print_error(
                                    "No se ha agregado ningún producto por el momento"
                                )
                        case _:
                            print_error("elige una de las opciones del menú")
                    pause()
            case "3":
                while True:
                    clear()
                    print(
                        menu_options(
                            "Añadir un Pedido",
                            "Calcular total de un pedido",
                            "Mostrar todos los pedidos",
                            name="Gestionar pedidos",
                        )
                    )
                    ped_option = input(" -> Elige una de las opciones: ")

                    clear()
                    match ped_option:
                        case "0":
                            break
                        case "1":
                            print(menu_titles("añadir un pedido"))
                            #   Generamos la información del nuevo pedido
                            new_id = generate_id(
                                "PED", [o.order_id for o in orders_placed]
                            )
                            client_id = input(" -> Introduce el id del cliente: ").upper()
                            date = input(" -> Fecha de pedido: ")
                            
                            products = input(" -> Introduce los id de los productos separados por comas: ").upper().split(",")
                            
                            ord_prod = [id for id in products if id in [prod.prod_id for prod in avaible_products]]

                            #   Creamos el objeto en un entorno controlado
                            try:
                                orders_placed[new_id] = Order(
                                    new_id, registred_clients[client_id], date, [prod for prod in avaible_products if prod.prod_id.upper() in ord_prod]
                                )
                            except (ValueError, KeyError) as e:
                                print_error(f"Se ha producido un error de tipo: {e}")

                        case "2":
                            print(menu_titles("calcular total de un pedido"))
                            ped_id = input(" -> Introduce el id el pedido: ").upper()
                            try:
                                total = orders_placed[ped_id].calc_total()
                                print(f" Total del pedido con ID {ped_id}: {total}€")
                            except KeyError as e:
                                print_error(f"Se ha producido un error de tipo: {e} (id inexistente)")
                                
                        case "3":
                            print(menu_titles("mostrar todos los productos de un pedido"))
                            if orders_placed:
                                for order in orders_placed.values():
                                    print(order)
                            else:
                                print_error("no se ha añadido ningún pedido todavía")

                        case _:
                            print_error("elige una de las opciones del menú")
                    pause()

            case "4":
                while True:
                    clear()
                    print(
                        menu_options(
                            "Añadir una reseña",
                            "Mostrar todas las reseñas",
                            name="Gestionar reseñas",
                        )
                    )
                    prod_option = input(" -> Elige una de las opciones: ")

                    clear()
                    match prod_option:
                        case "0":
                            break
                        case "1":
                            print(menu_titles("añadir una reseña"))
                            
                        case "2":
                            pass
                        case _:
                            print_error("elige una de las opciones del menú")
            case _:
                print_error("elige una de las opciones del menú")

        pause()


if __name__ == "__main__":
    menu()
