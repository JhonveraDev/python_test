countries={
    'mexico':122,
    'colombia':50,
    'argentina':43,
    'chile':18,
    'peru':31
}

while True:
    country= str(input("Escribe el nombre del pais ")).lower()
    
    try:
        print("la poblacion de {} es de: {} millones".format(country,countries[country]))
        
    except KeyError:
        print("No tenemos datos de {}".format(country))    