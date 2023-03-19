class Vector:
    def __inint__ (self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__ (self):
        Cadena = "("+ str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"
        return Cadena
    
    def __mul__(self, seg):
        if type(self)==type(seg):
            resultado = (self.x*seg.x + self.y*seg.y + self.z*seg.z)
            return resultado
        else:
            resultado=Vector( self.x*seg , self.y*seg , self.z*seg )
            return resultado
#pido definir los vectores
print("defina el vector:")
x_1 = float(input("x="))
y_1 = float(input("y="))
z_1 = float(input("z="))

vector_1 = ( x_1 , y_1 , z_1 )

print(vector_1)