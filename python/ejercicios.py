dato = input("ingrese el dato: ")

print (dato) 

lista = ["nico", "andy", "santi"]

if lista.count(dato) > 0: 
    print("el dato existe", dato) 
    primero = input("ingrese el primer numero:") 

    try:
        primero = int(primero)
    except:
        primero =  "contradicción" 

    segundo = input("ingrese el segundo numero:")

    try:
        segundo = int(segundo)
    except:
        segundo = "contradicción" 

    if primero == "contradicción" or segundo == "contradicción":
        print("ingresaste mal el dato")
        exit() 
    else:
    simbolo = input("ingrese operación: ")
    
    if simbolo == "+":
        print("suma", primero + segundo)        
    elif simbolo == "-":
        print("resta", primero - segundo)  
    elif simbolo == "*":
        print("multiplicación", primero * segundo)   
    elif simbolo == "/":
        print("división", primero / segundo)  
        
else: 
    print(" el dato no existe", dato)







 