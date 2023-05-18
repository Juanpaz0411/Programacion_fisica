import math
class Vector:
  def __init__(self, coordenada_x, coordenada_y, coordenada_z):
    self.x = coordenada_x
    self.y = coordenada_y
    self.z = coordenada_z
    self.magnitud = (self.x**2 + self.y**2 + self.z**2)**0.5

  
  def __str__(self):
    respuesta = "( "+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+" )"
    return(respuesta)


  def productovectorial(self, seg):
    return(self.y*seg.z-self.z*seg.y, \
                         self.z*seg.x-self.x*seg.z,  \
                         self.x*seg.y-self.y*seg.x)
    
  def suma(self, otro):
    return(self.x+otro.x, self.y+otro.y, self.z+otro.z )
  
  def product(self, otros):
    return( self.x*otros.y, self.y*otros.y, self.z*otros.y)

""" |i  j  k |
    |sx sy sz|=(sy*z1-y1*sz)i - (sx*z1-x1*sz)j + (sx*y1-x1*sy)k = (sy*z1-y1*sz)i + (x1*sz-sx*z1)j + (sx*y1-x1*sy)k
    |x1 y1 z1|
"""
x_1 = float(input("ingrese coordenada x_1:"))
y_1 = float(input("ingrese coordenada y_1:"))
z_1 = float(input("ingrese coordenada z_1:"))


x_2 = float(input("ingrese coordenada x_2:"))                                           
y_2 = float(input("ingrese coordenada y_2:"))
z_2 = float(input("ingrese coordenada z_2:"))

vec_1=Vector(x_1,y_1,z_1)
vec_2=Vector(x_2,y_2,z_2)

print("posicion del vector 1:",vec_1)
print("posicion del vector 2:",vec_2)
print("magnitud del vector 1:", vec_1.magnitud)
print("magnitud del vector 2:", vec_2.magnitud)
print("vector perpendicular a los dos vectores:", vec_1.productovectorial(vec_2))
print("adision de vector 1 y 2:", vec_1.suma(vec_2))



