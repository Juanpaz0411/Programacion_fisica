import os #de esta forma se usa la libreria
import sys
import platform

#print(os.getcwd()) # para mostrar donde esta ubicado
    #C:\Users\USUARIO WINDOWS\programacion <directorio de trabajo actual>
    #ruta absoluta del proyecto

#print(os.name)
    #nt

#print(sys.platform)
    #win32

#print(os.listdir()) #listar archivos de mi actual ubicación
    #['archivos', 'estudio', 'estudio_clases', 'miweb', 'parcial_1', 'parcial_2', 'parcial_pruebas', 'tarea_1']  lista de la carpeta programación
    #lista = os.listdir() #guardar los archivos de un directorios dentro de una lista

#print(os.path)
    #<module 'ntpath' from 'C:\\Users\\USUARIO WINDOWS\\miniconda3\\lib\\ntpath.py'>

#os.chdir('..')#"directoria al cual queremos dirigirnos" cambio de directorio
    # ".." volvemos al directorio anterior

# os.mkdir("nuevo_directorio")#podemos crear un directorio, pasamos una ruta completa o relativa

#os.remove('')#borra cosas

#os.path.exists('')#nos dice si existe un determinado directorio

'''import os
if os.path.exists("nuevo_directorio") == true:
    print("El directorio ya existe")
else:
    os.mkdir("nuevo_directorio")
    print("se creo el directorio")
'''
# os.chdir('nuevo_directorio')#cambiamos de directorio

#os.chdir('/Users/USUARIO WINDOWS/Downloads/Punto1.zip/')

'''import os
if not os.path.exists("nuevo_directorio"):
    os.mkdir("nuevo_directorio")
else:
    print("El directorio ya existe")
'''
# os.path.exists("nuevo_directorio")#verifica si un archivo o 
# directorio existe en la ruta especificada por path.


# print(os.getcwd())

# print(os.listdir())

#el modulo sys permite enlazar la ejecucion del programa con el sistema 
#operativo

# print('saliendo del programa...')
# sys.exit()#al ejecutarlo el programa termina de ejecutarlo  
# print('no mostrar esta linea')

#print(sys.getwindowsversion())

#print(sys.modules)#comprobamos si un modulo existe en nuestro programa

# print(sys.version)#version de python

# print(sys.version_info)#version de python mas simplificada

# print(platform.architecture())#arquitectura del sistema

# print(platform.machine())#modelo del procesador, arquitectura

# print(platform.processor())#mas informacion especifica del procesador

# print(platform.platform())#información de la plataforma, cadema de info de windows
    #hale lo mismo que sys.getwindowsversion() pero simple

# print(platform.system())#nombre del sistema operativo


'''un programa puede hacer una cosa u otra dependiendo del sistema operativo'''

# print(platform.uname())


