# Funciones para crear nodos
def crear_terreno(tx, id_terreno,tipo_zona,ubicacion, precio, tamano, estado, tipo, fecha_de_listado, descripcion):
    query = (
        "CREATE (t:Terreno {"
        "ID_terreno: $id_terreno, "
        "Tipo_zona: $tipo_zona,"
        "Ubicacion: $ubicacion, "
        "Precio: $precio, "
        "Tamaño: $tamaño, "
        "Estado: $estado, "
        "Tipo: $tipo, "
        "Fecha_de_listado: $fecha_de_listado, "
        "Descripcion: $descripcion"
        "})"
    )
    tx.run(query,
           id_terreno=id_terreno,
           ubicacion=ubicacion,
           tipo_zona=tipo_zona,
           precio=precio,
           tamaño=tamano,
           estado=estado,
           tipo=tipo,
           fecha_de_listado=fecha_de_listado,
           descripcion=descripcion)

def crear_zona(tx, id_zona, nombre_zona, tamano_zona):
    query = (
        "CREATE (z:Zona {"
        "ID_zona: $id_zona, "
        "Nombre_zona: $nombre_zona,"
        "Tamaño_zona: $tamano_zona"
        "})"
    )
    tx.run(query,id_zona=id_zona,nombre_zona=nombre_zona,tamano_zona=tamano_zona)

def crear_provincia(tx, id_provincia, nombre_provincia):
    query = (
        "CREATE (p:Provincia {"
        "ID_provincia: $id_provincia, "
        "Nombre_provincia: $nombre_provincia "
        "})"
    )
    tx.run(query,
           id_provincia=id_provincia,
           nombre_provincia=nombre_provincia)

def crear_cliente(tx, id_cliente, nombre_completo, email, telefono, presupuesto):
    query = (
        "CREATE (c:Cliente {"
        "ID_cliente: $id_cliente, "
        "Nombre_completo: $nombre_completo, "
        "Email: $email, "
        "Telefono: $telefono, "
        "Presupuesto: $presupuesto"
        "})"
    )
    tx.run(query, id_cliente=id_cliente, nombre_completo=nombre_completo, email=email, telefono=telefono, presupuesto=presupuesto)

def crear_propietario(tx, id_propietario, nombre_completo, email, telefono):
    query = (
        "CREATE (p:Propietario {"
        "ID_propietario: $id_propietario, "
        "Nombre_completo: $nombre_completo, "
        "Email: $email, "
        "Telefono: $telefono"
        "})"
    )
    tx.run(query, id_propietario=id_propietario, nombre_completo=nombre_completo, email=email, telefono=telefono)

def crear_empleado(tx, id_empleado, nombre_completo, email, telefono):
    query = (
        "CREATE (e:Empleado {"
        "ID_empleado: $id_empleado, "
        "Nombre_completo: $nombre_completo, "
        "Email: $email, "
        "Telefono: $telefono"
        "})"
    )
    tx.run(query, id_empleado=id_empleado, nombre_completo=nombre_completo, email=email, telefono=telefono)