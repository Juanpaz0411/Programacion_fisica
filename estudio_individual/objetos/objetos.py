'''
al pensar en algo como un concepto podemos pensar en todos los datos que definen este 
objeto para hacer una definicion de este, definiendo asi su clase, definiendo en esta
clase las caracteristicas de los objetos o conceptos asociadas a esta clase.

una clase es un conjunto de variables y funciones(metodos) que agrupadas definen este objeto.

ejemplo
clase
{
cohce :
    variables:#las variables definen los objetos de esta clase
        marca: str
        modelo: str
        color: str
        matricula: str
    métodos:
        arrancar()
        parar()
        frenar()
        acelerar()
}

con esta clase creada podemos crear diferentes objetos.

objetos
{
Marca = renault
modelo = laguna
color = plateado

marca = testa
modelo = model 3
color = gris

marca = simca
modelo = 1000
color = hueso
}

la clase coche nos dice con que definimos coche, un coche especifico lo da cada objeto.

la programacion orientada a objetos es un paradigma que permite crear metodos y variables
pero tambien objetos que interactuan entre ellos.

la programacion orientada a objetos tiene ventajas.
    ENCAPSULACION
        nos asegura que nuetra clase controla tanto los datos que hay dentro como 
        los metodos para interactuar con estos.

            ejemplo:
                si en coche se le agregan variables como velocidad y aceleracion.
                si para aumentar velocidad se hace atraves de aceleracion, permite controlar 
                esta interacción.
                    def acelerar(tiempo):
                        velocidad += aceleracion * tiempo
        
        nos ayuda a proteger los datos de forma tal que solo a través de metodos en esta clase
        modifique e se interactue con los objetos.

    ABSTRACCION
        se puede llamar un método para que se efectue una acción sin importar los detalles
        del funcionamiento.

    HERENCIA
        clases que vienen de otras clases. a partir de objetos particulares se usa una clase
        para particularizar añadiendo mas metodos a la clase.
    
    POLIMORFISMO
        nuestro codigo en cualquier parte donde tengamos que pasar un objeto de clase a otra
        siempre y cuando sea entre clases heredadas.

            

'''
