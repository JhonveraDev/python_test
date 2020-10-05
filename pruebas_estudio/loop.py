def my_func(x):
    respuesta = 0
    for i in range(20):
        print(i)
        respuesta += 1
        
    return respuesta


if __name__ == '__main__':
    my_func(5)