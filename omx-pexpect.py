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

import os
import pexpect
import time
import glob
import random



def player_lista (mp3):
    global proc
    global song
    global musica

    for song in mp3:
        musica = song.split("/", 4)[-1]
        song = song.replace(" ","\ ")
        os.system('cls||clear')
        print '\nReproduciendo ==> ', musica.split("/", 4)[-1]
        print '\nElige un numero y presiona ENTER (control de reproduccion):'
        print ('\n  1 - Play/Pausa\n  2 - Siguiente cancion\n  3 - Quit/Salir')
        
        proc = pexpect.spawn('omxplayer %s' %song) 
        proc.expect_exact('nice day', timeout=None)
        time.sleep (1)
    proc.close()
    print "\nPlayList finalizada\n\nTenga un excelente dia ;-)"
    time.sleep(5)
    os.system('cls||clear')
    os._exit(1)
 
def archivos ():
    global lista
    global i2
    
    os.system('cls||clear')
    """ Comienza la reproduccion NORMAL de los archivos mp3 en la ruta (variable path).
    Al llegar al final de la lista de archivos mp3, la reproduccion se detiene.
    """
    path ='/ruta/a/Musica'
    
    lista = []
    i = 0
    print '\nGenerando lista' # - Reproduccion aleatoria'
    with open('lista.txt', 'r+') as file:

        for infile in glob.glob(os.path.join(path, "*.mp3")):
            file.write('%s %s\n' % (i,infile))
            i += 1

            lista.append(infile)
            time.sleep(0.5)
    random.shuffle(lista)
    i2 = len(lista)
    print ('\nTotal de canciones %s' % i2)
    time.sleep(4)


if __name__ == '__main__':
    
   

    t = threading.Thread(name='non-daemon', target=archivos)

    t.start()
    t.join()
    d = threading.Thread(name='daemon', target=player_lista, args=(lista,))
    d.setDaemon(True)
    d.start()

    while i2 > 0:
        time.sleep(3)

        tipo=''
        while tipo not in [1, 2, 3]:

            try:
                tipo = int(raw_input('\n __? '))
                
                if tipo > 3 or tipo < 1:
                    os.system('cls||clear')
                    print '--- Solo  1, 2 o 3 ---'
                    print ('\n  1 - Play/Pausa\n  2 - Siguiente cancion\n  3 - Quit/Salir')
                    time.sleep(3)

            except ValueError:
                
                os.system('cls||clear')
                print ('\n*** SOLO NUMEROS 1, 2 o 3 POR FAVOR ***')
                print ('\n  1 - Play/Pausa\n  2 - Siguiente cancion\n  3 - Quit/Salir')
                time.sleep(3)
                continue
        #tipo = tipo.lower()
    
        if tipo == 1:
            print '\nPausado\n'
            proc.send('p')
            #player_lista(lista)
    
        elif tipo == 2:
            print ('\nSiguiente\n')
            os.system('cls||clear')
            proc.send('q')
            i2 -= 1
            #print i2
            
        elif tipo == 3:
            proc.close()
            time.sleep(1)
            print "\nSaliendo. Tenga un exelente dia ;-) "
            time.sleep(3)
            os.system('cls||clear')
            exit()
    
    d.join()


