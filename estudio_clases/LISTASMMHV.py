class Vector:
        def __init__(self, x, y, z):
            self.x=x
            self.y=y
            self.z=z
    
        def __str__(self):
            respuesta = "( "+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+" )"
            return(respuesta)
             
        def __mul__(self, sig):
            if type(self)==type(sig):
                return resultado
            else:
                resultado = Vector((self.x * sig), (self.y * sig), (self.z * sig))
                return resultado

#agregando para matrices
