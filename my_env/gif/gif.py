# Importra librerías
import os
import imageio

# Ubicación de la base de datos
path = '/home/javier/Documentos/manual/manualUsuario/my_env/gif/imgFEM/'
archivos = sorted(os.listdir(path))
img_array = []

#Leer todos los archivos formato imagen desde path
for x in range(0, len(archivos)):
    nomArchivo = archivos[x]
    dirArchivo = path + str(nomArchivo)
    
    #Asignar a variable leer_imagen, el nombre de cada imagen
    leer_imagen = imageio.imread(dirArchivo)
    
    # añadir imágenes al arreglo img_array
    img_array.append(leer_imagen)
    
#Guardar Gif
imageio.mimwrite('K.gif', img_array, 'GIF', duration=0.5)


