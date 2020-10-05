
# def run():
#     with open('Prueba.txt', 'w') as f:
#         for i in range(10):
#             f.write(str(i))
            

         
            
def runRead():
    counter=0   
    with open("aleph.txt", encoding='utf-8') as f:
        for line in f:
            counter += line.count("Beatriz")   
            
    print("se encuentra tantas {}".format(counter))        
                    


if __name__ == '__main__':
    #run()
    runRead()