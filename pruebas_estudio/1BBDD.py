import sqlite3

miConexion=sqlite3.connect("Base_Datos")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR (50), PRECIO INTEGER, SECCION VARCHAR(20))")

# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

# variosProductos=[
    
#     ("Camiseta",10,"Deportes"),
#     ("Consola",100,"Tecnologia"),
#     ("Televisor",10,"Electrodomesticos")
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos) #El Executemany permite almacenar varios elementos a la vez

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
    # print(producto)
    pass

print("Nombre del Artículo: ", producto[0],"\nNombre de la Sección: ", producto[2], "\nCon un valor de: ",producto[1])


miConexion.commit() #Esto Confirma los cambibos dentro de la base de datos

miConexion.close()