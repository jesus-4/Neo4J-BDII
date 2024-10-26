from DAO import GestionDao

gestor=GestionDao()
terrenos=[]
#carga de nodos
# Crear Provincias
"""
gestor.add_nodo_provincia(id_provincia="Pro1",provincia_name="La Rioja")
gestor.add_nodo_provincia(id_provincia="Pro2",provincia_name="Córdoba")
gestor.add_nodo_provincia(id_provincia="Pro3",provincia_name="Buenos Aires")

#Crear Zona
gestor.add_nodo_zona(zona_id="Z1", name_zona="Chilecito", tamano_zona="350 km²")
gestor.add_nodo_zona(zona_id="Z2", name_zona="Chamical", tamano_zona="250 km²")
gestor.add_nodo_zona(zona_id="Z3", name_zona="Carlos Paz", tamano_zona="900 km²")
gestor.add_nodo_zona(zona_id="Z4", name_zona="Villa Soto", tamano_zona="650 km²")
gestor.add_nodo_zona(zona_id="Z5", name_zona="Merlo", tamano_zona="350 km²")
gestor.add_nodo_zona(zona_id="Z6", name_zona="La Plata", tamano_zona="650 km²")

# Crear Terrenos
gestor.add_nodo_terreno(id_terreno="T1",tipo_zona="Periurbanas",ubicacion="URL",precio=5000, tamano=1500, estado="En Venta", tipo="Residencial", fecha_de_listado="2024-09-01", descripcion="Terreno con vista al parque")
gestor.add_nodo_terreno(id_terreno="T2",tipo_zona="Rural",ubicacion="URL", precio=7500, tamano=2000, estado="En Tramite", tipo="Residencial", fecha_de_listado="2024-08-10", descripcion="Terreno serca del campo")
gestor.add_nodo_terreno(id_terreno="T3",tipo_zona="Centro",ubicacion="URL", precio=50000, tamano=3500, estado="En Venta", tipo="Residencial", fecha_de_listado="2024-07-01", descripcion="Terreno preparado para contrunccion")
gestor.add_nodo_terreno(id_terreno="T4",tipo_zona="Urbana",ubicacion="URL", precio=75000, tamano=4500, estado="En Tramite", tipo="Comercial", fecha_de_listado="2024-06-10", descripcion="Terreno cerca de univercidades")
gestor.add_nodo_terreno(id_terreno="T5",tipo_zona="Urbana",ubicacion="URL", precio=150000, tamano=5500, estado="En Venta", tipo="Comercial", fecha_de_listado="2024-05-01", descripcion="Terreno para negocio")
gestor.add_nodo_terreno(id_terreno="T6",tipo_zona="Urbana",ubicacion="URL", precio=275000, tamano=8000, estado="Vendida", tipo="Comercial", fecha_de_listado="2024-04-10", descripcion="Terreno ideal para negocio")
gestor.add_nodo_terreno(id_terreno="T7",tipo_zona="Urbana",ubicacion="URL", precio=295000, tamano=8000, estado="En Venta", tipo="Comercial", fecha_de_listado="2024-04-10", descripcion="Terreno ideal para negocio")

# Crear Propietarios
gestor.add_nodo_propietario(id_propietario="P1",nombre_completo="Claramonte Jesus",email="jClaramonte@example.com",telefono="123456789")
gestor.add_nodo_propietario(id_propietario="P2",nombre_completo="María García",email="maria@example.com",telefono="987654321")
gestor.add_nodo_propietario(id_propietario="P3",nombre_completo="Nicolas Junin",email="NJ@example.com",telefono="1236789")
gestor.add_nodo_propietario(id_propietario="P4",nombre_completo="Mirta Gomez",email="MG@example.com",telefono="9874321")
gestor.add_nodo_propietario(id_propietario="P5",nombre_completo="Franco Hernandez",email="FH@example.com",telefono="1256789")


# Crear Empleados
gestor.add_nodo_empleado(id_empleado="E1", nombre_empleado="Javier Cordoba",email="Jcordoba@example.com",telefono="555123456")
gestor.add_nodo_empleado(id_empleado="E2", nombre_empleado="Luis Martínez",email="luis@example.com",telefono="555654321")
gestor.add_nodo_empleado(id_empleado="E3", nombre_empleado="Matias Alvares",email="Matias@example.com",telefono="5556543321")
gestor.add_nodo_empleado(id_empleado="E4", nombre_empleado="Franco Colapintos",email="Franco@example.com",telefono="5542324321")
gestor.add_nodo_empleado(id_empleado="E5", nombre_empleado="German Varquez",email="ger@example.com",telefono="5542324321")
gestor.add_nodo_empleado(id_empleado="E6", nombre_empleado="Alfonso Fernanades",email="alf@example.com",telefono="5542324321")
gestor.add_nodo_empleado(id_empleado="E7", nombre_empleado="Sofia Gonzales",email="sof@example.com",telefono="5542324321")

# Crear Clientes
gestor.add_nodo_cliente(id_cliente="C1", nombre_completo="Juan Pérez", email="juan@example.com", telefono="666123456", presupuesto=60000)
gestor.add_nodo_cliente(id_cliente="C2", nombre_completo="Laura Sánchez", email="laura@example.com", telefono="666654321", presupuesto=80000)
gestor.add_nodo_cliente(id_cliente="C3", nombre_completo="Javier Sanchez", email="jav@example.com", telefono="666112312312", presupuesto=160000)
gestor.add_nodo_cliente(id_cliente="C4", nombre_completo="Agustin Gomez", email="agu@example.com", telefono="666113123", presupuesto=260000)
gestor.add_nodo_cliente(id_cliente="C5", nombre_completo="Julio Cesar", email="jul@example.com", telefono="666112345", presupuesto=360000)
gestor.add_nodo_cliente(id_cliente="C6", nombre_completo="Matina Sosa", email="mar@example.com", telefono="66612321312", presupuesto=460000)
gestor.add_nodo_cliente(id_cliente="C7", nombre_completo="David Herrera", email="Dad@example.com", telefono="6661esaasd2", presupuesto=490000)

# Crear Provincia
gestor.relacion_zona_provincia(id_zona="Z1", id_provincia="Pro1")
gestor.relacion_zona_provincia(id_zona="Z2", id_provincia="Pro1")
gestor.relacion_zona_provincia(id_zona="Z3", id_provincia="Pro2")
gestor.relacion_zona_provincia(id_zona="Z4", id_provincia="Pro2")
gestor.relacion_zona_provincia(id_zona="Z5", id_provincia="Pro3")
gestor.relacion_zona_provincia(id_zona="Z6", id_provincia="Pro3")

# Asociar Terrenos a Zonas
gestor.relacion_terreno_zona(id_terreno="T2", id_zona="Z1")
gestor.relacion_terreno_zona(id_terreno="T1", id_zona="Z2")
gestor.relacion_terreno_zona(id_terreno="T3", id_zona="Z3")
gestor.relacion_terreno_zona(id_terreno="T4", id_zona="Z4")
gestor.relacion_terreno_zona(id_terreno="T5", id_zona="Z5")
gestor.relacion_terreno_zona(id_terreno="T6", id_zona="Z6")
gestor.relacion_terreno_zona(id_terreno="T7", id_zona="Z6")

# Asignar Empleados a Zonas
gestor.relacion_empleado_zona(id_empleado="E1",id_zona="Z1")
gestor.relacion_empleado_zona(id_empleado="E2",id_zona="Z2")
gestor.relacion_empleado_zona(id_empleado="E3",id_zona="Z3")
gestor.relacion_empleado_zona(id_empleado="E4",id_zona="Z4")
gestor.relacion_empleado_zona(id_empleado="E5",id_zona="Z5")
gestor.relacion_empleado_zona(id_empleado="E6",id_zona="Z6")
gestor.relacion_empleado_zona(id_empleado="E7",id_zona="Z6")

# Vincular Terrenos a Propietarios id_terreno=None, id_propietario=None
gestor.relacion_terreno_propietario(id_terreno="T1", id_propietario="P1")
gestor.relacion_terreno_propietario(id_terreno="T2", id_propietario="P2")
gestor.relacion_terreno_propietario(id_terreno="T3", id_propietario="P3")
gestor.relacion_terreno_propietario(id_terreno="T4", id_propietario="P4")
gestor.relacion_terreno_propietario(id_terreno="T5", id_propietario="P5")
gestor.relacion_terreno_propietario(id_terreno="T6", id_propietario="P3")
gestor.relacion_terreno_propietario(id_terreno="T7", id_propietario="P5")
# Clientes interesados en Terrenos
gestor.relacion_cliente_terreno(id_cliente="C1", id_terreno="T1")
gestor.relacion_cliente_terreno(id_cliente="C6", id_terreno="T2")
gestor.relacion_cliente_terreno(id_cliente="C3", id_terreno="T3")
gestor.relacion_cliente_terreno(id_cliente="C4", id_terreno="T4")
gestor.relacion_cliente_terreno(id_cliente="C5", id_terreno="T5")
gestor.relacion_cliente_terreno(id_cliente="C2", id_terreno="T6")
gestor.relacion_cliente_terreno(id_cliente="C6", id_terreno="T3")
gestor.relacion_cliente_terreno(id_cliente="C7", id_terreno="T7")

# Clientes interactúan con Empleados
gestor.relacion_cliente_empleado(id_cliente="C1", id_empleado="E2")
gestor.relacion_cliente_empleado(id_cliente="C2", id_empleado="E6")
gestor.relacion_cliente_empleado(id_cliente="C3", id_empleado="E3")
gestor.relacion_cliente_empleado(id_cliente="C4", id_empleado="E4")
gestor.relacion_cliente_empleado(id_cliente="C5", id_empleado="E5")
gestor.relacion_cliente_empleado(id_cliente="C6", id_empleado="E3")
gestor.relacion_cliente_empleado(id_cliente="C6", id_empleado="E1")
gestor.relacion_cliente_empleado(id_cliente="C7", id_empleado="E7")
"""
terrenos=gestor.get_terrenos(prov_id="Pro1",zona_id=None)
#terrenos=gestor.get_clientes_terrenos(cliente_id="C1",terreno_id="T1")
#terrenos=gestor.get_terrenos_propietarios(provincia_id="Pro1",propietario_id="P1")
#terrenos=gestor.get_terrenos_por_precio(min_precio=2000, max_precio=85000)
#gestor.add_nodo_provincia(id_provincia="Pro5",provincia_name="San Juan")
#gestor.add_nodo_zona(zona_id="Z8",name_zona=None, tamano_zona=None)
#gestor.add_nodo_terreno(id_terreno=None,tipo_zona=None,ubicacion=None, precio=None, tamano=None, estado=None, tipo=None, fecha_de_listado=None, descripcion=None)
#gestor.add_nodo_propietario(id_propietario=None, nombre_completo=None, email=None, telefono=None)
#gestor.add_nodo_empleado(id_empleado=None, nombre_empleado=None, email=None, telefono=None)
#gestor.add_nodo_cliente(id_cliente=None, nombre_completo=None, email=None, telefono=None, presupuesto=None)
#gestor.relacion_empleado_zona(id_empleado=None,id_zona=None)
#gestor.relacion_zona_provincia(id_zona="Z8", id_provincia="Pro5")
#gestor.relacion_terreno_zona(id_terreno=None, id_zona=None)

print(terrenos)
