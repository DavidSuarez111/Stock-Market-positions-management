def agregar_posicion(acciones, accion, cantidad):
    """_summary_
    Actualiza el diccionario de registro ligero de acciones y sus cantidades agregando posiciones.
    Args:
        acciones (Diccionario): Sostiene los nombres de las acciones y sus cantidades.
        accion (Clave): Nombre de la acción a agregar.
        cantidad (Valor): Cantidad de acciones a agregar.
        
    """
    if accion in acciones.keys():
        acciones[accion] += cantidad
    else:
        acciones[accion] = cantidad
    
    