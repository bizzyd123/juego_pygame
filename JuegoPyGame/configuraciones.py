import pygame


def reescalar_imagenes (lista_imagenes, tamaño):
    for i in range (len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)

def girar_imagenes(lista,flip_x,flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen,flip_x, flip_y))
    return lista_girada
        
#definimos los fotogramas de cada animacion

def reproducir_sonido(ruta_sonido, volumen=1.0):
    pygame.mixer.init()
    sonido = pygame.mixer.Sound(ruta_sonido)
    sonido.set_volume(volumen)
    sonido.play()

