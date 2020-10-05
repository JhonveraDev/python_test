print("Materias para el año 2020")
print("Asignaturas Optativas: Informatica Grafica - Pruebas de Software - Usabilidad")

dato=input("Escribe la materia que quieres ver: " )

datoMIN = dato.lower()

if datoMIN in ("informatica grafica","pruebas de software", "usabilidad" ):
    
    print("Tu carrera elegida es: " + datoMIN )
    
else:
    print("No has seleccionado correctamente tu Materia")    

