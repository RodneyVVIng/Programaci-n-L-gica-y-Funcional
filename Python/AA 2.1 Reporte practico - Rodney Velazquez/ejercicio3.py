#// Programa  que simula el lanzamiento de una moneda
#import random 
#num= random.randint(0, 1)
#if num ==0:
 #   print('Cara')
#else:
 #   print('Cruz')

#// Programa que simula la bola magica 
import random 
pregunta = input('pregunta:                 ')
numero_aleatorio = random.randint(1, 9)

if numero_aleatorio == 1:
    respuesta = 'sí - definitivamente'

elif numero_aleatorio ==2:
    respuesta = 'está decidido'
elif numero_aleatorio ==3:
    respuesta= 'Sin duda'

elif numero_aleatorio == 4:
    respuesta = 'respuesta confusa, intenta de nuevo'
elif numero_aleatorio == 5:
    respuesta= 'pregunta más tarde'
elif numero_aleatorio==6:
    respuesta = 'mejor no te digo'
elif numero_aleatorio ==7:
    respuesta=  'mis fuentes dicen que no'
elif numero_aleatorio ==8:
    respuesta= 'no parece bueno'
elif numero_aleatorio ==9:
    respuesta= 'muy dudoso'
else:
     respuesta= 'error'
print ('bola mágica: '+respuesta)