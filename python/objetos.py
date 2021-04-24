#class Usuario:
 #   def __init__(self, nombre, apellido):
 #       self.nombre = nombre 
 #       self.apellido = apellido 
    
#    def saludo(self):
#        print("¿CUAL ES MI NOMBRE?", self.nombre, self.apellido)
    
#class Admin(Usuario):
#    def supersaludo(self):
#        print("Hola me llamo", usuario.nombre, "y quiero ser piola")    
        
#usuario = Usuario("PETER","rikinder")
#usuario.saludo()        
#usuario.nombre = "vbrian"
#usuario.saludo()


#admin = Admin("super", "capo")
#admin.saludo()
#admin.supersaludo() 

class Gato:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre 
        self.onomatopeya = onomatopeya
        
    def saludo(self):
        print("HOLA CHAMACO", self.onomatopeya) 
gato = Gato("CANTINA", "lasly") 
gato.saludo()
