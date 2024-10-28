from neo4j.exceptions import Neo4jError
from neo4j import GraphDatabase

from CrearAristas import asignar_empleado_zona, asociar_terreno_zona, cliente_interactua_empleado, cliente_interesado_en_terreno, vincular_terreno_propietario,asociar_zona_provincia
from CrearNodos import crear_cliente, crear_empleado, crear_propietario, crear_terreno, crear_zona,crear_provincia
from Connection import Connection
from Clientes import get_clientes_empleado,get_empleados_cliente,get_empleados_cliente_id,get_interacciones
from Empleados import get_empleados_zona,get_empleados_zonas,get_zonas_empleado
from Terrenos import get_terreno_id,get_prov_zona_id,get,get_prov_id,get_zona_id,get_cliente_id,get_clientes_terreno,get_propietarios_provincia_id,get_terrenos_min_precio,get_terrenos_por_rango_precio,get_terrenos_max_precio,get_todos_terrenos_precio,get_propietario_id,get_propietario_provincia,get_terrenos_disponibles_zona

class GestionDao:
      def __init__(self):
            self.dao = Connection()


      def get_terrenos(self,*,prov_id=None,zona_id=None):
            resul=[]
            if  zona_id is not None and prov_id is not None:
                  #todos los terrenos de la provincia prov_id y de la zona zona_id
                  resul=self.dao.execute_read(get_prov_zona_id,prov_id,zona_id)
            elif prov_id is not None:
                  #todos los terrenos de la provincia prov_id
                  resul=self.dao.execute_read(get_prov_id,prov_id)
            elif zona_id is not None:
                  #todos los terrenos de la zona zona_id
                  resul=self.dao.execute_read(get_zona_id,zona_id)
            else:
                  #todos los terrenos (en caso de no pasar parametros)
                  resul=self.dao.execute_read(get)
            return resul
      
      def get_clientes_terrenos(self,*,cliente_id=None,terreno_id=None):
            resul=[]
            if cliente_id is not None and terreno_id is not None:
                  #todos los terrenos que le interesa al cliente cliente_id y todos los clientes interesados por el terrenos terreno_id
                  resul=self.dao.execute_read(get_cliente_id,cliente_id, terreno_id)
            elif cliente_id is not None:
                  #todos los terrenos que le interesa al cliente cliente_id
                  resul=self.dao.execute_read(get_cliente_id,cliente_id)
            elif terreno_id is not None:
                  #todos los clientes interesados por el terrenos terreno_id
                  resul=self.dao.execute_read(get_terreno_id,terreno_id)
            else:
                  #todos los terrenos con una cantidad de clientes interesados (en caso de no pasar parametros)
                  resul=self.dao.execute_read(get_clientes_terreno)
            return resul

      def get_terrenos_propietarios(self,*,provincia_id=None,propietario_id=None):
            resul=[]
            if propietario_id is not None and provincia_id is not None:
                  #lA cantidad de terenos del propietario propietario_id en la provincia provincia_id
                  resul=self.dao.execute_read(get_propietarios_provincia_id,provincia_id,propietario_id)
            elif provincia_id is not None:
                  #todos los propietaros con su cantidad de terreno en la provincia provincia_id
                  resul=self.dao.execute_read(get_propietarios_provincia_id,provincia_id)
            elif propietario_id is not None:
                  #todos los terrenos de un propietario propietario_id                  #es el mismo que arriba - No seria un metodo de terreno
                  resul=self.dao.execute_read(get_propietario_id,propietario_id)
            else:
                  #todos los propietarios con la cantidad de terenenos en cada provincia(en caso de no pasar parametros)
                  resul=self.dao.execute_read(get_propietario_provincia)
            return resul

      def get_empleados_zonas(self, *, empleado_id=None, zona_id=None):
            resul = []
            if empleado_id is not None:
                  # Todas las zonas asignadas a un empleado empleado_id
                  resul = self.dao.execute_read(get_zonas_empleado,empleado_id)
            elif zona_id is not None:
                  # Todos los empleados asignados a una zona zona_id
                  resul = self.dao.execute_read(get_empleados_zona,zona_id)
            else:
                  # Todos los empleados con la cantidad de zonas asignadas (en caso de no pasar parámetros)
                  resul = self.dao.execute_read(get_empleados_zonas)
            return resul

      def get_clientes_empleados(self, *, cliente_id=None, empleado_id=None):
            resul = []
            if cliente_id is not None and empleado_id is not None:
                  #Todos los terenos que le interesa al cliente 
                  resul = self.dao.execute_read(get_empleados_cliente_id,cliente_id,empleado_id,)
            elif cliente_id is not None:
                  # Todos los empleados con los que interactuó un cliente cliente_id
                  resul = self.dao.execute_read(get_empleados_cliente,cliente_id,)
            elif empleado_id is not None:
                  # Todos los clientes que interactuaron con un empleado empleado_id
                  resul = self.dao.execute_read(get_clientes_empleado,empleado_id)
            else:
                  # Todos los clientes y empleados con sus interacciones (en caso de no pasar parámetros)
                  resul = self.dao.execute_read(get_interacciones)
            return resul

      def get_zonas_con_terrenos_disponibles(self, *, zona_id=None):
            resul = []
            if zona_id is not None:
                  # Todos los terrenos disponibles en la zona zona_id
                  resul = self.dao.execute_read(get_terrenos_disponibles_zona,zona_id)
            else:
                  # Todas las zonas con los terreno disponible
                  resul = self.dao.execute_read(get_terrenos_disponibles_zona,zona_id)
            return resul

      def get_terrenos_por_precio(self, *, min_precio=None, max_precio=None):
            resul = []
            if min_precio is not None and max_precio is not None:
                  # Terrenos cuyo precio está entre min_precio y max_precio
                  resul = self.dao.execute_read(get_terrenos_por_rango_precio,min_precio, max_precio)
            elif min_precio is not None:
                  # Terrenos cuyo precio es mayor o igual a min_precio
                  resul = self.dao.execute_read(get_terrenos_min_precio,min_precio)
            elif max_precio is not None:
                  # Terrenos cuyo precio es menor o igual a max_precio
                  resul = self.dao.execute_read(get_terrenos_max_precio,max_precio)
            else:
                  # Todos los terrenos con sus precios
                  resul = self.dao.execute_read(get_todos_terrenos_precio)
            return resul

      def add_nodo_provincia(self,*,id_provincia=None,provincia_name=None):
            if id_provincia is not None:
                  if provincia_name is not None:
                        self.dao.execute_write(crear_provincia,id_provincia,provincia_name)
                        print("nodo creado correctamente")
                  else:
                        self.dao.execute_write(crear_provincia,id_provincia,provincia_name)
                        print("nodo crea sin nombre")
            else:
                  print("Falta parametros para crear nodo")

      def add_nodo_zona(self,*,zona_id=None,name_zona=None, tamano_zona=None):
            if zona_id is not None:
                  if name_zona is not None and tamano_zona is not None:
                        self.dao.execute_write(crear_zona,zona_id,name_zona,tamano_zona)
                        print("Creacion de nodo correctamente")
                  else:
                        self.dao.execute_write(crear_zona,zona_id,name_zona,tamano_zona)
                        print("Se creo nodo zona con datos faltante")
            else:
                  print("Se nesesita Id_zona como minimo para crear  un nodo zona")

      def add_nodo_terreno(self,*,id_terreno=None,tipo_zona=None,ubicacion=None, precio=None, tamano=None, estado=None, tipo=None, fecha_de_listado=None, descripcion=None):
            if id_terreno is not None:
                  if tipo_zona is not None and ubicacion is not None and precio is not None and tamano is not None and estado is not None and tipo is not None and fecha_de_listado is not None and descripcion is not None:
                        self.dao.execute_write(crear_terreno,id_terreno,tipo_zona,ubicacion, precio, tamano, estado, tipo, fecha_de_listado, descripcion)
                        print("Creacion de nodo correctamente")
                  else:
                        self.dao.execute_write(crear_terreno,id_terreno,tipo_zona,ubicacion, precio, tamano, estado, tipo, fecha_de_listado, descripcion)
                        print("Se creo nodo zona con datos faltante")
            else:
                  print("Se nesesita Id_zona como minimo para crear  un nodo terreno")

      def add_nodo_propietario(self,*,id_propietario=None, nombre_completo=None, email=None, telefono=None):
            if id_propietario is not None:
                  if nombre_completo is not None and email is not None and telefono is not None:
                        self.dao.execute_write(crear_propietario,id_propietario, nombre_completo, email, telefono)
                        print("Creacion de nodo correctamente")
                  else:
                        self.dao.execute_write(crear_propietario,id_propietario, nombre_completo, email, telefono)
                        print("Se creo nodo zona con datos faltante")
            else:
                  print("Se necesita Id_propietario como minimo para crear un Propietario")

      def add_nodo_empleado(self,*,id_empleado=None, nombre_empleado=None, email=None, telefono=None):
            if id_empleado is not None:
                  if nombre_empleado is not None and email is not None and telefono is not None:
                        self.dao.execute_write(crear_empleado,id_empleado, nombre_empleado, email, telefono)
                  else:
                        self.dao.execute_write(crear_empleado,id_empleado, nombre_empleado, email, telefono)
            else:
                  print("Se necesita Id_empleado como minimo para crear un nodo Empleado")

      def add_nodo_cliente(self,*,id_cliente=None, nombre_completo=None, email=None, telefono=None, presupuesto=None):
            if id_cliente is not None:
                  if nombre_completo is not None and email is not None and telefono is not None and presupuesto is not None:
                        self.dao.execute_write(crear_cliente,id_cliente, nombre_completo, email, telefono, presupuesto)
                  else:
                        self.dao.execute_write(crear_cliente,id_cliente, nombre_completo, email, telefono, presupuesto)
            else:
                  print("Se necesita como minimo id_cliente para crear un nodo Cliente")

      def relacion_empleado_zona(self,*,id_empleado=None,id_zona=None):
            if id_empleado is not None and id_zona is not None:
                  self.dao.execute_write(asignar_empleado_zona,id_empleado,id_zona)
                  print("Relacion realisada")
            else:
                  print("Se necesita id_empleado y id_zona para realisar una relacion")

      def relacion_zona_provincia(self,*,id_zona=None, id_provincia=None):
            if id_zona is not None and id_provincia is not None:
                  self.dao.execute_write(asociar_zona_provincia,id_zona,id_provincia)
                  print("Relacion realisada")
            else:
                  print("Se necesita id_zona y id_provincia para realisar una relacion")

      def relacion_terreno_zona(self,*,id_terreno=None, id_zona=None):
            if id_terreno is not None and id_zona is not None:
                  self.dao.execute_write(asociar_terreno_zona,id_terreno,id_zona)
                  print("Relacion realisada")
            else:
                  print("Se necesita id_terreno y id_zona para realisar una relacion")


      def relacion_terreno_propietario(self,*,id_terreno=None, id_propietario=None):
            if id_terreno is not None and id_propietario is not None:
                  self.dao.execute_write(vincular_terreno_propietario,id_terreno,id_propietario)
                  print("Relacion realisada")
            else:
                  print("Se necesita id_terreno y id_propietario para realisar una relacion")


      def relacion_cliente_terreno(self,*,id_cliente=None, id_terreno=None):
            if id_cliente is not None and id_terreno is not None:
                  self.dao.execute_write(cliente_interesado_en_terreno,id_cliente,id_terreno)
                  print("Relacion realisada")
            else:
                  print("Se necesita id_cliente y id_terreno para realisar una relacion")


      def relacion_cliente_empleado(self,*,id_cliente=None, id_empleado=None):
            if id_cliente is not None and id_empleado is not None:
                  self.dao.execute_write(cliente_interactua_empleado,id_cliente,id_empleado)
                  print("Relacion realisada")
            else:
                  print("Se necesita id_cliente y id_empleado para realisar una relacion")

      def modificar_terreno(self, *, terreno_id=None, tipo_zona=None, precio=None,superficie=None, estado=None, descripcion=None, zona_id=None):
            if terreno_id is not None:
                  # Verificar si el terreno existe
                  existe=[]
                  existe = self.dao.dao.execute_read(get_terreno_id,terreno_id)

                  if  len(existe) <= 0:
                        print("No se encontró el terreno con ID: {terreno_id}")
                        return



                  # Construir el diccionario con los atributos a modificar
                  atributos_a_modificar = {
                        "Nombre": tipo_zona,
                        "Precio": precio,
                        "Superficie": superficie,
                        "Estado": estado,
                        "Descripcion": descripcion,
                        "Zona_id": zona_id,
                  }

                  # Filtrar los atributos que no son None
                  atributos_a_modificar = {k: v for k, v in atributos_a_modificar.items() if v is not None}

                  if not atributos_a_modificar:
                        print("No se proporcionaron atributos válidos para modificar.")
                        return

                  # Ejecutar la consulta para modificar el terreno
                  self.dao.dao.execute_write(modificar_terreno,terreno_id, atributos_a_modificar)
                  print(f"Terreno con ID {terreno_id} modificado correctamente.")
            else:
                  print("Debe proporcionar un 'terreno_id' para modificar un terreno")


