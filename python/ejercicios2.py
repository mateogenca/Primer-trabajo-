a = 4
b = 8 
resultado = 0

for x in range(a):
    resultado += b
print(resultado)

nombre = "carlos"
apellido = "martinez"

concatenación = nombre + "" + apellido

print(concatenación[::-1])

#lista (1, 2, 3, 6 , -2, 232, 323232, 4)
#menor = "init"

#for x in lista:
 #  if menor == "init":
 #       menor = x
 #   else:
 #        menor = x if x < menor else menor
         
#print ("menor", menor)
  
def calculaVolumen(r):
    return 4 / 3 * 3.14 * r ** 3

resultado = calculaVolumen(6)
print(resultado)

def esMayor (usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self,edad):
        self.edad = edad
        
usuario = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esMayor(usuario)            
resultado2 = esMayor(usuario2) 

print(resultado1, resultado2)

#escribir una función que indique si un nímero es par o impar 

def esPar(n):
    return n % 2 == 0


resultado = esPar(10)
print(resultado)

# escribir una funcion que indique cuantas vocales tiene una palabra 
palabra = "cuadriplejico"
vocales = 0
for x in palabra:
    vocales += 1 if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" else 0

print(vocales)

#escribir una app que reciba una cant infinita de numero hasta que dija basta, luego vuelva a la suma de los numeros ingresados

lista = []
print("ingrese un numero y para salir escriba basta")
while True:
    valor = input("ingrese valor:")
    if valor == "basta":
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print("dato invalido")
            exit()

resultado = 0
for x in lista:
    resultado += x 
    
print(resultado)        