def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    """No recibe parámetros. Valida que sea un entero entre 1 y 6.
    Maneja excepciones si el dato ingresado no es un entero."""
    opcion_valida = False
    opcion = None

    while not opcion_valida:  
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                opcion_valida = True
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

    return opcion




def cupos_tipo(tipo, planes, inscripciones):
    """Recibe el tipo de plan, no retorna nada, imprime el resultado."""
    tipo = tipo.strip().lower()
    total = 0

    for codigo in planes:  
        tipo_plan = planes[codigo][1]
        if tipo_plan.lower() == tipo:
            total += inscripciones[codigo][1]  

    print(f"El total de cupos disponibles es: {total}")



def busqueda_precio(p_min, p_max, planes, inscripciones):
    """Recibe precio mínimo y máximo (ya validados en main). No retorna
    nada, imprime el resultado directamente."""
    resultados = []

    for codigo in inscripciones: 
        precio = inscripciones[codigo][0]
        cupos = inscripciones[codigo][1]
        if p_min <= precio <= p_max and cupos != 0:
            nombre = planes[codigo][0]
            resultados.append(f"{nombre}--{codigo}")

    resultados.sort() 
    if resultados:
        print(f"Los planes encontrados son: {resultados}")
    else:
        print("No hay planes en ese rango de precios.")



def buscar_codigo(codigo, diccionario):
    """Retorna True si el código existe en el diccionario (sin distinguir
    mayúsculas/minúsculas), False si no."""
    return codigo.strip().upper() in diccionario


def actualizar_precio(codigo, nuevo_precio, inscripciones):
    """Verifica existencia con buscar_codigo. Actualiza el precio y
    retorna True, o retorna False si el código no existe."""
    codigo = codigo.strip().upper()
    if buscar_codigo(codigo, inscripciones):
        inscripciones[codigo][0] = nuevo_precio
        return True
    return False



def validar_codigo(codigo, planes):
    codigo = codigo.strip()
    if codigo == "":
        return False
    return not buscar_codigo(codigo, planes)


def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_tipo(tipo):
    return tipo.strip().lower() in ("mensual", "trimestral", "anual")


def validar_duracion(duracion_str):
    try:
        valor = int(duracion_str)
        return valor > 0
    except ValueError:
        return False


def validar_sn(valor):
    return valor.strip().lower() in ("s", "n")


def validar_horario(horario):
    return horario.strip() != ""


def validar_precio(precio_str):
    try:
        valor = int(precio_str)
        return valor > 0
    except ValueError:
        return False


def validar_cupos(cupos_str):
    try:
        valor = int(cupos_str)
        return valor >= 0
    except ValueError:
        return False


def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina,
                  incluye_clases, horario, precio, cupos,
                  planes, inscripciones):
    """Agrega el registro en ambos diccionarios. Retorna True si se
    agregó, False si el código ya existía."""
    codigo = codigo.strip().upper()
    if buscar_codigo(codigo, planes):
        return False

    planes[codigo] = [nombre, tipo, duracion, acceso_piscina,
                       incluye_clases, horario]
    inscripciones[codigo] = [precio, cupos]
    return True




def eliminar_plan(codigo, planes, inscripciones):
    """Verifica existencia con buscar_codigo. Elimina el registro de
    ambos diccionarios y retorna True, o retorna False si no existe."""
    codigo = codigo.strip().upper()
    if buscar_codigo(codigo, planes):
        del planes[codigo]
        del inscripciones[codigo]
        return True
    return False


def main():
    planes = {
        'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
        'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
        'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
        'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
        'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
        'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
    }

    inscripciones = {
        'F001': [14990, 30],
        'F002': [22990, 10],
        'F003': [39990, 0],
        'F004': [35990, 6],
        'F005': [159990, 2],
        'F006': [18990, 15],
    }

    opcion = 0

    while opcion != 6: 
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            tipo = input("Ingrese tipo de plan a consultar: ")
            cupos_tipo(tipo, planes, inscripciones)

        elif opcion == 2:
           
            valores_validos = False
            p_min = p_max = 0

            while not valores_validos:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min < 0 or p_max < 0 or p_min > p_max:
                        print("Debe ingresar valores enteros")
                    else:
                        valores_validos = True
                except ValueError:
                    print("Debe ingresar valores enteros")

            busqueda_precio(p_min, p_max, planes, inscripciones)

        elif opcion == 3:
            continuar = "s"
            while continuar == "s":
                codigo = input("Ingrese código del plan: ")

                precio_valido = False
                nuevo_precio = 0
                while not precio_valido:
                    try:
                        nuevo_precio = int(input("Ingrese nuevo precio: "))
                        if nuevo_precio > 0:
                            precio_valido = True
                        else:
                            print("El precio debe ser un entero positivo")
                    except ValueError:
                        print("El precio debe ser un entero positivo")

                if actualizar_precio(codigo, nuevo_precio, inscripciones):
                    print("Precio actualizado")
                else:
                    print("El código no existe")

                continuar = input(
                    "¿Desea actualizar otro precio (s/n)?: "
                ).strip().lower()

        elif opcion == 4:
            codigo = input("Ingrese código del plan: ")
            nombre = input("Ingrese nombre del plan: ")
            tipo = input("Ingrese tipo (mensual/trimestral/anual): ")
            duracion_str = input("Ingrese duración (meses): ")
            piscina_str = input("¿Incluye acceso a piscina? (s/n): ")
            clases_str = input("¿Incluye clases grupales? (s/n): ")
            horario = input("Ingrese horario: ")
            precio_str = input("Ingrese precio: ")
            cupos_str = input("Ingrese cupos: ")

            if not validar_codigo(codigo, planes):
                print("El código no es válido o ya existe")
            elif not validar_nombre(nombre):
                print("El nombre no puede estar vacío")
            elif not validar_tipo(tipo):
                print("El tipo debe ser 'mensual', 'trimestral' o 'anual'")
            elif not validar_duracion(duracion_str):
                print("La duración debe ser un entero mayor que cero")
            elif not validar_sn(piscina_str):
                print("Debe ingresar 's' o 'n'")
            elif not validar_sn(clases_str):
                print("Debe ingresar 's' o 'n'")
            elif not validar_horario(horario):
                print("El horario no puede estar vacío")
            elif not validar_precio(precio_str):
                print("El precio debe ser un entero mayor que cero")
            elif not validar_cupos(cupos_str):
                print("Los cupos deben ser un entero mayor o igual a cero")
            else:
                acceso_piscina = piscina_str.strip().lower() == "s"
                incluye_clases = clases_str.strip().lower() == "s"
                duracion = int(duracion_str)
                precio = int(precio_str)
                cupos = int(cupos_str)
                tipo = tipo.strip().lower()

                if agregar_plan(codigo, nombre, tipo, duracion,
                                 acceso_piscina, incluye_clases, horario,
                                 precio, cupos, planes, inscripciones):
                    print("Plan agregado")
                else:
                    print("El código ya existe")

        elif opcion == 5:
            codigo = input("Ingrese código del plan: ")
            if eliminar_plan(codigo, planes, inscripciones):
                print("Plan eliminado")
            else:
                print("El código no existe")

        elif opcion == 6:
            print("Programa finalizado.")


if __name__ == "__main__":
    main()
