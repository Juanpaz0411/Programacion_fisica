from scipy.stats import pearsonr

class shooter:
    '''
    clase shooter referente a videojuegos de 'armas'.
    '''
    def __init__(self, nombre):
        '''
        constructor de la clase, recibe como argumento a 'nombre' es una clase básica.
        '''
        self.nombre = nombre

    def __str__(self):
        '''
        indica que retorna un objeto de la clase y en que formato.
        '''
        return f"videojuego: {self.nombre}"

    def jugar(self):
        '''
        imprime el mensaje "Esta jugando un shooter"
        '''
        print("Esta jugando un shooter")

    def tilt(self):
        '''
        imprime el mensaje 'Esta tilteado por un videojuego xd'
        '''
        print('Esta tilteado por un videojuego xd')

class valorant(shooter):
    '''
    una subclase de la clase shooter, un videojuego especifico entre todos los videojuegos de armas.
    '''
    def __init__(self, nombre, **kwargs):
        '''
        el constructor de la subclase, usa como argumento el nombre, invocado de la clase base shooter
        y agrega un nuevo argumento para los personajes.
        '''
        super().__init__(nombre)
        self.personajes = {}

        if len(kwargs) < 3:
            print("Debe proporcionar al menos 3 personajes con sus poderes")
            exit()
        else:
            self.personajes = kwargs

    def __str__(self):
        '''
        dice en que formato se va a imprimir los datos ingresados, al ser un diccionario el argumento se imprime una
        cadena bajo un formato específico que indica el personaje y su poder.
        '''
        personajes_poderes = [f"{personaje}: {poder}\n" for personaje, poder in self.personajes.items()]
        return f"\n{super().__str__()}\nPersonajes con sus poderes:\n {''.join(personajes_poderes)}"

    def jugar(self):
        '''
        agrega al jugar() de la clase base un nuevo mensaje especifico al juego valorant:
        'Estas jugando Valorant'
        '''
        super().jugar()
        print("Estas jugando Valorant\n")

    def tilt(self):
        '''
        agrega al tilt() de la clase base un nuevo mensaje especifico al juego valorant:
        'Estas enojado con Riot Games'.
        '''
        super().tilt()
        print('Estas enojado con Riot Games\n')

    def ingresar_estadisticas(self):
        '''
        Pide al usuario los datos kill y muerte para cada personaje ingresado y se ejecuta la funcion imprimir_estadisticas 
        que imprime los datos ingresados en formato de tabla.
        '''
        estadisticas = {}
        for personaje in self.personajes:
            habilidad = self.personajes[personaje]
            kills = int(input(f"\nIngrese el número de kills para {personaje}: "))
            muertes = int(input(f"Ingrese el número de muertes para {personaje}: "))
            estadisticas[personaje] = {'habilidad': habilidad, 'kills': kills, 'muertes': muertes}

        self.imprimir_estadisticas(estadisticas)

    def imprimir_estadisticas(self, estadisticas):
        '''
        imprime las estadisticas en una tabla con los datos: nombre, habilida, kill, muertes; asocia los valores de las
        key de un diccionario a las columnas de la tabla
        '''
        print("\nEstadísticas de los personajes")
        print("Nombre\t\tHabilidad\tKills\tMuertes")
        for personaje, stats in estadisticas.items():
            habilidad = stats['habilidad']
            kills = stats['kills']
            muertes = stats['muertes']
            print(f"{personaje}\t\t{habilidad}\t\t{kills}\t{muertes}")

        # Calcular coeficiente de correlación de Pearson
        kills_data = [stats['kills'] for stats in estadisticas.values()]
        muertes_data = [stats['muertes'] for stats in estadisticas.values()]

        coef, _ = pearsonr(kills_data, muertes_data)
        print(f"\nCoeficiente de correlación de Pearson para kills-muertes: {coef:.2f}")


clase = int(input('Hay 3 clases, ¿cuál quiere correr? 1[shooter], 2 [valorant]: ').strip())

if clase == 1:
    videojuego = input('Ingrese el nombre del shooter que estás jugando: ')
    Vg = shooter(videojuego)
    print(Vg)
    Vg.jugar()
    Vg.tilt()

elif clase == 2:
    m = input('¿Está jugando Valorant? [s/n]: ')
    
    if m.lower() == 's':
        personajes = input('Ingrese el nombre del personaje usado separado por comas:\n').split(',')
        poderes = input('Ingrese el poder del personaje usado en orden separado por comas:\n').split(',')
        M = 'Valorant'
        
        if len(personajes) != len(poderes):
            print("La cantidad de personajes y poderes no coincide.")

        else:
            kw = dict(zip(personajes, poderes))
            val = valorant(M, **kw)
            print(val)
            val.jugar()
            val.tilt()
            val.ingresar_estadisticas()
    else:
        pass
else:
    print('Entrada incorrecta.')

