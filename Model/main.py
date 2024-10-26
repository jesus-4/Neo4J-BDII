from DAO import GestionDao

gestor=GestionDao()
terrenos=[]
#terrenos=gestor.get_terrenos(prov_id="Pro1",zona_id="Z1")
#terrenos=gestor.get_clientes_terrenos(cliente_id="C1",terreno_id="T1")
terrenos=gestor.get_terrenos_propietarios(provincia_id="Pro1",propietario_id="P1")
#terrenos=gestor.get_terrenos_por_precio(min_precio=2000, max_precio=85000)
#gestor.add_nodo_provincia(id_provincia="Pro5",provincia_name="San Juan")
#gestor.add_nodo_zona(zona_id="Z8",name_zona=None, tamano_zona=None)
#gestor.add_nodo_terreno(id_terreno=None,tipo_zona=None,ubicacion=None, precio=None, tamano=None, estado=None, tipo=None, fecha_de_listado=None, descripcion=None)
#gestor.add_nodo_propietario(id_propietario=None, nombre_completo=None, email=None, telefono=None)
#gestor.add_nodo_empleado(id_empleado=None, nombre_empleado=None, email=None, telefono=None)
#gestor.add_nodo_cliente(id_cliente=None, nombre_completo=None, email=None, telefono=None, presupuesto=None)
#gestor.relacion_empleado_zona(id_empleado=None,id_zona=None)
gestor.relacion_zona_provincia(id_zona="Z8", id_provincia="Pro5")
#gestor.relacion_terreno_zona(id_terreno=None, id_zona=None)

print(terrenos)
