#Examen transversal
#Tienda GameHub
####FUNCIONES DE RESULTADOS
def  stock_plataforma(s_juegos, s_inventario):
    busqueda_plataforma = input("Ingrese la plataforma que desea consultar el stock: ").strip().lower()
    contador_stock = 0
    for cod_juegos, valor_juegos in s_juegos.items():
        if valor_juegos[1].lower() == busqueda_plataforma:
            for codigo_inventario, valor_inventario in s_inventario.items():
                if codigo_inventario == cod_juegos:
                    contador_stock += valor_inventario[1]
                    break
    
    if contador_stock > 0:

        print(f"Se han encontrado {contador_stock} de {busqueda_plataforma} en el inventario")
    else:
        print(f"No hay stock disponible de {busqueda_plataforma}")

def busqueda_precio(p_min, p_max,p_inventario,p_juegos):

    lista_busqueda_precio = []
    for cod_inventario, valor_inventario in p_inventario.items():
        if valor_inventario[0]>= p_min and valor_inventario[0]<= p_max:
            for cod_juegos, valor_juegos in p_juegos.items():
                if cod_juegos== cod_inventario:
                    lista_busqueda_precio.append(f"{valor_juegos[0]}--{cod_juegos}")
                    break
    lista_busqueda_precio.sort()
    if lista_busqueda_precio:
        print(f"Se han encontrado {len(lista_busqueda_precio)} resultados")
        for lista in lista_busqueda_precio:
            print(lista)
    else:
        print("No se han encontrado resultados")
def busca_codigo(codigo,b_inventario):

    for cod_inventario, valor_inventario in b_inventario.items():
        if cod_inventario == codigo:
            return True
    return False

def actualizar_precio(a_codigo, a_nuevo_precio,a_inventario):

    retorno_busqueda_codigo = busca_codigo(a_codigo,a_inventario)
    if retorno_busqueda_codigo == True:
        for cod_inventario, valor_inventario in a_inventario.items():
            if a_codigo == cod_inventario:
                valor_inventario[0]= a_nuevo_precio
                return True
    else:
        return False
    
def eliminar_juego(e_codigo,e_inventario,e_juegos):
    
    retorna_busca_cod = busca_codigo(e_codigo,e_inventario)

    if retorna_busca_cod == True:
        e_inventario.pop(e_codigo)
        e_juegos.pop(e_codigo)
        return True
    else:
        return False

##########################################################
#######VALIDA NUEVO JUEGO ################################
def valida_codigo(vcod):
    filtra_cod = vcod.strip()
    if filtra_cod != "":
        return True
    return False
def valida_titulo(vtitulo):
    filtrar_titulo = vtitulo.strip()
    if filtrar_titulo != "":
        return True
    return False
def valida_plataforma(vplataforma):
    filtrar_plataforma = vplataforma.strip()
    if filtrar_plataforma != "":
        return True
    return False
def valida_genero(vgenero):
    filtrar_genero = vgenero.strip()
    if filtrar_genero != "":
        return True
    return False
def valida_clasificacion(vclasificacion):
    filtrar_clasificacion = vclasificacion.strip()
    if filtrar_clasificacion in ("E","T","M"):
        return True
    return False
def valida_multiplayer(vmultiplayer):
    filtrar_multiplayer = vmultiplayer.strip()
    if filtrar_multiplayer in ("s","n"):
        return True
    return False
def valida_editor(veditor):
    filtrar_editor = veditor.strip()
    if filtrar_editor != "":
        return True
    return False
def valida_precio(vprecio):
    try:
        filtrar_precio = int(vprecio)
        if filtrar_precio >0:
            return True
        return False
    except ValueError:
        return False

def valida_stock(vstock):
    try:
        filtrar_stock = int(vstock)
        if filtrar_stock >=0:
            return True
        return False
    except ValueError:
        return False

def agregar_juego(n_codigo, n_titulo, n_plataforma, n_genero, n_clasificacion, n_multiplayer, n_editor, n_precio, n_stock, n_inventario, n_juegos):
    
    revisa_codigo = busca_codigo(n_codigo,n_inventario)

    if revisa_codigo == False:
        
        if n_multiplayer == "s":
            new_multi = True
        else:
            new_multi = False

        n_inventario[n_codigo] = [n_precio, n_stock]
        n_juegos[n_codigo] = [n_titulo,n_plataforma,n_genero,n_clasificacion, new_multi,n_editor]

        return True

    else:
        return False

################FUNCIONES MAIN Y OPCION
def main():
   
    juegos = {
        'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True,
        'NovaStudio'],
        'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False,
        'BrightWorks'],
        'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True,
        'OrionGames'],
        'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True,
        'VelocityLab'],
        'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False,
        'GreenSeed'],
        'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False,
        'IronGate']
    }
    inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2]
    }

    while True: 
            opcion = leer_opcion()

            if opcion == 1:
                stock_plataforma(juegos,inventario)
            elif opcion == 2:
                 while True:
                     try:
                        precio_minimo = int(input("Ingrese el precio minimo : "))
                        precio_maximo = int(input("Ingrese el precio maximo : "))
                        if precio_minimo>0 and precio_minimo < precio_maximo:
                            busqueda_precio(precio_minimo, precio_maximo,inventario,juegos)
                            break
                        else:
                            print("Debe ingresar valores enteros")
                            print("Además el precio minimo no debe ser mayor que el precio maximo")
                            print("-----------------------------------")
                     except ValueError:
                         print("Los precios ingresados no son correctos")
                        

            elif opcion == 3: 
                ejecucion_update = True
                while ejecucion_update:
                    codigo_up = input("Ingrese el codigo que desea buscar : ")

                    while True:
                        try:
                            nuevo_precio = int(input("Ingrese el nuevo precio : "))
                            if nuevo_precio >0:
                                break
                            else:
                                print("El precio a actualizar debe ser un valor entero positivo ")
                        except ValueError:
                            print("El precio a actualizar es incorrecto")
                    retorno_actualiza = actualizar_precio(codigo_up, nuevo_precio, inventario)

                    if retorno_actualiza == True:
                        print("Precio actualizado")
                    else:
                        print("El código no existe")

                    while True:
                        nuevo_update=input("¿Desea volver a actualizar? (s/n)").strip().lower()
                        if nuevo_update in ("s","n"):
                            if nuevo_update == "s":
                                break
                            else:
                                ejecucion_update = False
                                break
                        else: 
                            print("La opción ingresada para continuar actualiando es incorrecta, debe ser Si o No (s/n)")
            elif opcion == 4:
                
                codigo_juego = input("Ingrese el código : ")
                titulo_juego = input("Ingrese el titulo : ")
                plataforma_juego = input("Ingrese la plataforma : ")
                genero_juego = input("Ingrese el genero : ")
                clasificacion_juego = input("Ingrese la clasificación (E/T/M): ")
                multiplayer_juego = input("¿El juego es multiplayer? (s/n) : ")
                editor_juego = input("ingrese el editor del juego : ")
                precio_juego = input("Ingrese el precio del juego : ")
                stock_juego = input("Ingrese el stock del juego : ")

                ret_valida_codigo = valida_codigo(codigo_juego)
                ret_valida_titulo = valida_titulo(titulo_juego)
                ret_valida_plataforma = valida_plataforma(plataforma_juego)
                ret_valida_genero = valida_genero(genero_juego)
                ret_valida_clasificacion = valida_clasificacion(clasificacion_juego)
                ret_valida_multiplayer = valida_multiplayer(multiplayer_juego)
                ret_valida_editor = valida_editor(editor_juego)
                ret_valida_precio = valida_precio(precio_juego)
                ret_valida_stock = valida_stock(stock_juego)

                if ret_valida_codigo == True and ret_valida_titulo == True and ret_valida_plataforma == True and ret_valida_genero == True and ret_valida_clasificacion == True and ret_valida_multiplayer == True and ret_valida_editor == True and ret_valida_precio == True and ret_valida_stock == True:
                    add_game = agregar_juego(codigo_juego.strip(),titulo_juego.strip(),plataforma_juego.strip(),genero_juego.strip(), clasificacion_juego.strip(), multiplayer_juego.strip(),editor_juego.strip(),int(precio_juego),int(stock_juego), inventario, juegos)

                    if add_game == True:
                        print("Juego agregado")
                    else:
                        print("El código ya existe")

            elif opcion == 5:

                eliminar_cod = input("Ingrese el codigo a eliminar : ").strip()

                retorno_elimina = eliminar_juego(eliminar_cod, inventario, juegos)

                if retorno_elimina == True:
                    print("Juego eliminado")
                else:
                    print("El código no existe")
            elif opcion == 6:
                print("Programa finalizado.")
                break
            


def leer_opcion():
    while True:
        try:
            print("========== MENÚ PRINCIPAL ==========")
            print("1. Stock por plataforma")
            print("2. Búsqueda de juegos por rango de precio")
            print("3. Actualizar precio de juego")
            print("4. Agregar juego")
            print("5. Eliminar juego")
            print("6. Salir")
            
            opcion_menu = int(input("Ingrese una opción : "))

            if 0 < opcion_menu <=6:
                return opcion_menu
            else:
                print("La opción ingresada no es correcta debe ser de 1 a 6 ")

        except ValueError:
            print("La opción ingresada es incorrecta")




if __name__ == "__main__":
    main()