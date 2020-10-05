import sqlite3

miConexion=sqlite3.connect("gestor_productos") #crea la base de datos 

miCursor=miConexion.cursor() #Crea el cursor que realizar el CRUD de Sqlite

# miCursor.execute('''
                 
#     CREATE TABLE PRODUCTOS(
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,  
#     NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#     PRECIO INTEGER,
#     SECCION VARCHAR (20))
                 
#     ''')

# #Gestion de auto incremento en campo clave (Linea 9)

# productos=[
#     ("pelota", 20, "jugeteria"),
#     ("pantalón", 15, "confección"),
#     ("destornillador", 25, "ferretería"),
#     ("jarrón", 45, "cerámica"),
#     ("pantalones", 13, "confección")
# ]

#----------------- BSUQUEDA DE DATO EN ESPECIFICO READ------------
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección' ")

productos = miCursor.fetchall() #Es para realizar la lectura de la tabla
print(productos)

#----------------- ACTUALIZACION DE DATO EN ESPECIFICO UPDATE------------
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=222 WHERE NOMBRE_ARTICULO='pelota' ")


#----------------- BORRAR DE DATO EN ESPECIFICO DELETE------------
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5") #Tener demasiado cuidado con esta sentencia, un DELETE mal ejecutado puede borrar completamente toda la informacion de la base de datos



# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)
#Clausula UNIQUE para evitar duplicacion sin ser necesariamente un primary key
#Null, realiza la lectura del campo clave auto incrementable
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','tren',15,'jugueteria')")

miConexion.commit()
miConexion.close()
