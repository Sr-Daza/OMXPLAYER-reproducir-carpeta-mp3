#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Pograma para controlar musica con omxplayer desde telegram,
desde una ruta con archivos mp3 predefinida dentro de este modulo py.
Con pause, next, ramdom, etc

Sin garantia de ningun tipo, solo para efectos de prueba
"""


__author__ = "SrD"
__copyright__ = "Copyright 2017, A modo de prueba"
__credits__ = ["Ing. Daza"]
__license__ = "GPL"
__revision__ = "0.0.1 daza omxplayer"
__maintainer__ = "SrDaza"
__email__ = "xxxxx@xxxxxx.com"
__status__ = "Test"

# Import necessary modules
import os
import pexpect
import time
import glob
import random

from omxpope import player_lista
#import random

def gen_lista ():
    path = '/ruta/a/musica/'
    rutat = '/ruta/a/telegram/tg/bin'
    tele = pexpect.spawn("%s/telegram-cli -k tg-server.pub -W -C" % rutat)
    #tele = pexpect.spawn('telegram-cli -W')
    i = 0
    lista = []
    tipo = ''

    with open('lista.txt', 'r+') as file1:
        print 'Generando lista\n'

        for infile in glob.glob(os.path.join(path, "*.mp3")):
            tolista = infile.split("/", 5)[-1]
            file1.write('%s.-  %s\n' % (i, tolista))
            print('%s  %s' % (i, tolista))
            i += 1
            lista.append(infile)
            
            #print (infile)

    #print ((len(lista) - 1))
    item = (len(lista) - 1)  # Total de canciones menos 1
    print('\nTotal %s canciones' % len(lista))

    time.sleep(5)
    tele.sendline('send_text User /ruta/a/lista.txt')
    tele.expect_exact('>', timeout=None)
    time.sleep(1)

    with open('/ruta/a/lista.txt', 'w'):
        pass  # Borrar lista.txt

    while tipo not in [1, 2, 3]:
        print ('\nElige un numero (tipo de reproduccion):\n')
        print ('  1 - Todo - Normal\n  2 - Todo - Aleatorio\n  3 - Elegir rola')
        try:
            tipo = int(raw_input('\nNumero ? '))
            
            if tipo > 3 or tipo < 1:
                os.system('cls||clear')
                print '--- Solo numeros 1 2 o 3 ---'
                time.sleep(3)
            #elif tipo < 1:
            #   print '--- NO SE ACEPTA MENOR QUE 1 ---'
            #  time.sleep(3)
        except ValueError:
            
            os.system('cls||clear')
            print ('\n*** SOLO NUMEROS 1, 2 o 3 POR FAVOR ***\n')
            time.sleep(3)
            continue
    #tipo = tipo.lower()

    if tipo == 1:
        print '\nReproduccion Normal\n'
        player_lista(lista)

    elif tipo == 2:
        print ('\nReproduccion Aleatoria\n')
        random.shuffle(lista)
        player_lista(lista)
        
    elif tipo == 3:
        print ('\nElige una cancion')

        indice = -1

        #while indice == '':

        #   try:
        #      indice = int(raw_input('Introduce el numero de cancion\n'))
        # except ValueError:
            #    print 'Debe ingresar un numero'
            #   continue

        while indice > item or indice < 0:
            #print('imprime esto')
            try:
                indice = int(raw_input('\nIntroduce un numero - De 0 a %s\n' % item))
            except ValueError:
                continue
        arch = lista[indice]
        print arch
        print 'Reproduciendo--> ', arch.split("/", 5)[-1]
      #  player_lista(arch)
    #print ('Reproduciendo ', lista[indice])
    print('FIN Continuamos')


if __name__ == "__main__":
    gen_lista()
    
