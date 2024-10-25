from neo4j.exceptions import Neo4jError
from neo4j import GraphDatabase

from CrearAristas import asignar_empleado_zona, asociar_terreno_zona, cliente_interactua_empleado, cliente_interesado_en_terreno, vincular_terreno_propietario,asociar_zona_provincia
from CrearNodos import crear_cliente, crear_empleado, crear_propietario, crear_terreno, crear_zona,crear_provincia
from Qury import get_zonas_provincias,get_terrenos_por_zona,get_propietarios_terrenos,get_empleados_por_zona,get_clientes_by_terreno,get_sentenciageneral,get_consultageneral
from Delet import delet_client_id, delet_zona_id
from Conecction import Conecction
#
class GestionDao:
      dao = Conecction()

      def get_terrenos(self,*,prov_id=None,zona_id=None,):
            resul=[]
            if  zona_id is not None and prov_id is not None:
                  #todos los terrenos de la provincia prov_id y de la zona zona_id
                  resul=self.execute_read(Terrenos.get_prov_zona_id(prov_id,zona_id))
            elif prov_id is not None:
                  #todos los terrenos de la provincia prov_id
                  resul=self.execute_read(Terrenos.get_prov_id(prov_id))
            elif zona_id is not None:
                  #todos los terrenos de la zona zona_id
                  resul=self.execute_read(Terrenos.get_zona_id(zona_id))
            else:
                  #todos los terrenos (en caso de no pasar parametros)
                  resul=self.execute_read(Terrenos.get())
            return resul

      def get_clientes_terrenos(self,*,cliente_id=None,terreno_id=None):
            resul=[]
            if cliente_id is not None and terreno_id is not None:
                  #todos los terrenos que le interesa al cliente cliente_id y todos los clientes interesados por el terrenos terreno_id
                  resul=self.execute_read(Terrenos.get_cliente_id(cliente_id))
            elif cliente_id is not None:
                  #todos los terrenos que le interesa al cliente cliente_id
                  resul=self.execute_read(Terrenos.get_cliente_id(cliente_id))
            elif terreno_id is not None:
                  #todos los clientes interesados por el terrenos terreno_id
                  resul=self.execute_read(Terrenos.get_terreno_id(terreno_id))
            else:
                  #todos los terrenos con una cantidad de clientes interesados (en caso de no pasar parametros)
                  resul=self.execute_read(Terrenos.get_clientes_terreno())
            return resul

      def get_terrenos_propietarios(self,*,provincia_id=None,propietario_id=None):
            resul=[]
            if propietario_id is not None and provincia_id is not None:
                  #todos los propietaros con su cantidad de terreno en la provincia provincia_id y todos los terrenos de un propietario propietario_id
                  resul=self.execute_read(Terrenos.get_propietarios_provincia_id(provincia_id,propietario_id))
            elif provincia_id is not None:
                  #todos los propietaros con su cantidad de terreno en la provincia provincia_id
                  resul=self.execute_read(Terrenos.get_propietarios_provincia_id(provincia_id))
            elif propietario_id is not None:
                  #todos los terrenos de un propietario propietario_id
                  resul=self.execute_read(Terrenos.get_propietario_id(propietario_id))
            else:
                  #todos los propietarios con la cantidad de terenenos en cada provincia(en caso de no pasar parametros)
                  resul=self.execute_read(Terrenos.get_propietario_provincia())
            return resul

      def get_empleados_zonas(self, *, empleado_id=None, zona_id=None):
            resul = []
            if empleado_id is not None:
                  # Todas las zonas asignadas a un empleado empleado_id
                  resul = self.execute_read(Empleados.get_zonas_empleado(empleado_id))
            elif zona_id is not None:
                  # Todos los empleados asignados a una zona zona_id
                  resul = self.execute_read(Empleados.get_empleados_zona(zona_id))
            else:
                  # Todos los empleados con la cantidad de zonas asignadas (en caso de no pasar parámetros)
                  resul = self.execute_read(Empleados.get_empleados_zonas())
            return resul

      def get_clientes_empleados(self, *, cliente_id=None, empleado_id=None):
            resul = []
            if cliente_id is not None and empleado_id is not None:
                  # Todos los empleados con los que interactuó un cliente cliente_id y Todos los clientes que interactuaron con un empleado empleado_id
                  resul = self.execute_read(Clientes.get_empleados_cliente_id(cliente_id,empleado_id))
            elif cliente_id is not None:
                  # Todos los empleados con los que interactuó un cliente cliente_id
                  resul = self.execute_read(Clientes.get_empleados_cliente(cliente_id))
            elif empleado_id is not None:
                  # Todos los clientes que interactuaron con un empleado empleado_id
                  resul = self.execute_read(Clientes.get_clientes_empleado(empleado_id))
            else:
                  # Todos los clientes y empleados con sus interacciones (en caso de no pasar parámetros)
                  resul = self.execute_read(Clientes.get_interacciones())
            return resul

      def get_zonas_con_terrenos_disponibles(self, *, zona_id=None):
            resul = []
            if zona_id is not None:
                  # Todos los terrenos disponibles en la zona zona_id
                  resul = self.execute_read(Terrenos.get_terrenos_disponibles_zona(zona_id))
            else:
                  # Todas las zonas con los terreno disponible
                  resul = self.execute_read(Terrenos.get_zonas_con_disponibilidad())
            return resul

      def get_terrenos_por_precio(self, *, min_precio=None, max_precio=None):
            resul = []
            if min_precio is not None and max_precio is not None:
                  # Terrenos cuyo precio está entre min_precio y max_precio
                  resul = self.execute_read(Terrenos.get_terrenos_por_rango_precio(min_precio, max_precio))
            elif min_precio is not None:
                  # Terrenos cuyo precio es mayor o igual a min_precio
                  resul = self.execute_read(Terrenos.get_terrenos_min_precio(min_precio))
            elif max_precio is not None:
                  # Terrenos cuyo precio es menor o igual a max_precio
                  resul = self.execute_read(Terrenos.get_terrenos_max_precio(max_precio))
            else:
                  # Todos los terrenos con sus precios
                  resul = self.execute_read(Terrenos.get_todos_terrenos_precio())
            return resul

      def crear_nodo_provincia(self,*,id_provincia=None,provincia_name=None):
            if id_provincia is not None:
                  if provincia_name is not None:
                        self.execute_write(crear_provincia,id_provincia,provincia_name)
                        print("nodo creado correctamente")
                  else:
                        self.execute_write(crear_provincia,id_provincia,provincia_name)
                        print("nodo crea sin nombre")
            else:
                  print("Falta parametros para crear nodo")

      def crear_nodo_zona(self,*,zona_id=None,name_zona=None, tamano_zona=None):
            if zona_id is not None:
                  if name_zona is not None and tamano_zona is not None:
                        self.execute_write(crear_zona,zona_id,name_zona,tamano_zona)
                        print("Creacion de nodo correctamente")
                  else:
                        self.execute_write(crear_zona,zona_id,name_zona,tamano_zona)
                        print("Se creo nodo zona con datos faltante")
            else:
                  print("Se nesesita Id_zona como minimo para crear  un nodo zona")

      def crear_nodo_terreno(self,*,id_terreno=None,tipo_zona=None,ubicacion=None, precio=None, tamano=None, estado=None, tipo=None, fecha_de_listado=None, descripcion=None):
            if id_terreno is not None:
                  if tipo_zona is not None and ubicacion is not None and precio is not None and tamano is not None and estado is not None and tipo is not None and fecha_de_listado is not None and descripcion is not None:
                        self.execute_write(crear_terreno,id_terreno,tipo_zona,ubicacion, precio, tamano, estado, tipo, fecha_de_listado, descripcion)
                        print("Creacion de nodo correctamente")
                  else:
                        self.execute_write(crear_terreno,id_terreno,tipo_zona,ubicacion, precio, tamano, estado, tipo, fecha_de_listado, descripcion)
                        print("Se creo nodo zona con datos faltante")
            else:
                  print("Se nesesita Id_zona como minimo para crear  un nodo terreno")

      def crear_nodo_propietario(self,*,id_propietario=None, nombre_completo=None, email=None, telefono=None):
            if id_propietario is not None:
                  if nombre_completo is not None and email is not None and telefono is not None:
                        self.execute_write(crear_propietario,id_propietario, nombre_completo, email, telefono)
                        print("Creacion de nodo correctamente")
                  else:
                        self.execute_write(crear_propietario,id_propietario, nombre_completo, email, telefono)
                        print("Se creo nodo zona con datos faltante")
            else:
                  print("Se necesita Id_propietario como minimo para crear un Propietario")

      def crear_nodo_empleado(self,*,id_empleado=None, nombre_empleado=None, email=None, telefono=None):
            if id_empleado is not None:
                  if nombre_empleado is not None and email is not None and telefono is not None:
                        self.execute_write(crear_empleado,id_empleado, nombre_empleado, email, telefono)
                  else:
                        self.execute_write(crear_empleado,id_empleado, nombre_empleado, email, telefono)
            else:
                  print("Se necesita Id_empleado como minimo para crear un nodo Empleado")

      def crear_nodo_cliente(self,*,id_cliente=None, nombre_completo=None, email=None, telefono=None, presupuesto=None)
            if id_cliente is not None:
                  if nombre_completo is not None and email is not None and telefono is not None and presupuesto is not None:
                        self.execute_write(crear_cliente,id_cliente, nombre_completo, email, telefono, presupuesto)
                  else:
                        self.execute_write(crear_cliente,id_cliente, nombre_completo, email, telefono, presupuesto)
            else:
                  print("Se necesita como minimo id_cliente para crear un nodo Cliente")

      def relacion_empleado_zona(self,*,id_empleado=None,id_zona=None):
            if id_empleado is not None and id_zona is not None:
                  self.execute_write(asignar_empleado_zona,id_empleado,id_zona)
                  print("Relacion realisada")
            else:
                  print("Se necesita id_empleado y id_zona para realisar una relacion")

      def relacion_zona_provincia(self,*,id_zona=None, id_provincia=None):
            if id_zona is not None and id_provincia is not None:
                  self.execute_write(asociar_zona_provincia,id_zona,id_provincia)
                  print("Relacion realisada")
            else:
                  print("Se necesita id_zona y id_provincia para realisar una relacion")

      def relacion_terreno_zona(self,*,id_terreno=None, id_zona=None):
            if id_terreno is not None and id_zona is not None:
                  self.execute_write(asociar_terreno_zona,id_terreno,id_zona)
                  print("Relacion realisada")
            else:
                  print("Se necesita id_terreno y id_zona para realisar una relacion")


      def relacion_terreno_propietario(self,*,id_terreno=None, id_propietario=None):
            if id_terreno is not None and id_propietario is not None:
                  self.execute_write(vincular_terreno_propietario,id_terreno,id_propietario)
                  print("Relacion realisada")
            else:
                  print("Se necesita id_terreno y id_propietario para realisar una relacion")


      def relacion_cliente_terreno(self,*,id_cliente=None, id_terreno=None):
            if id_cliente is not None and id_terreno is not None:
                  self.execute_write(cliente_interesado_en_terreno,id_cliente,id_terreno)
                  print("Relacion realisada")
            else:
                  print("Se necesita id_cliente y id_terreno para realisar una relacion")


      def relacion_cliente_empleado(self,*,id_cliente=None, id_empleado=None):
            if id_cliente is not None and id_empleado is not None:
                  self.execute_write(cliente_interactua_empleado,id_cliente,id_empleado)
                  print("Relacion realisada")
            else:
                  print("Se necesita id_cliente y id_empleado para realisar una relacion")

