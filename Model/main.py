from DAO import GestionDao

gestor=GestionDao()
terrenos=[]
#terrenos=gestor.get_terrenos()
#gestor.modificar_terreno(terreno_id="T1",tipo_zona="Chepes")
terrenos=gestor.get_clientes_terrenos()
print(terrenos)
