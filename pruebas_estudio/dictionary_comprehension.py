pares=[]

for num in range(1,31):
    if num % 2 ==0:
        pares.append(num)

print(pares) 
print(range(1,31))  

cuadrados={}

for num in range(1,11):
    cuadrados[num]=num**2
    
print(cuadrados)    
    
def matching(person1, person2):
    	
	

	for key1, value1 in person1.items():
		hobbies=[]
		hobbies = value1
		matches = []
		for every in hobbies:
			for key2, value2 in person2.items():
				for hobby2 in value2:
					if every == hobby2:
						matches.append(hobby2)
					
		print('¡Hola, %s! %s y tu tienen los siguientes hobbies en común: %s' %(key1, key2, ", ".join(matches)))



if __name__ == '__main__':

	person1 = {"jenni": ["Musica", "Viajar", "Lectura"]}
	person2 = {"javier": ["Nadar", "Musica", "Viajar"]}
	matching(person1, person2)    