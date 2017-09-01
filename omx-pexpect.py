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

from mutagen.mp3 import MP3

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


def player_lista (mp3):
    global proc
    global song
       
    for song in mp3:
        song = song.replace(" ","\ ")
        
        proc = pexpect.spawn('omxplayer %s' %song) 
        proc.expect_exact('nice', timeout=None)
        
        time.sleep (1)
    proc.close()
        
def archivos ():
    global lista
    
    path ='/ruta/Musica'
    
    lista = []
    i = 0
    print '\nGenerando lista - Reproduccion aleatoria'
   
    with open('/ruta/lista.txt', 'r+') as file:

        for infile in glob.glob(os.path.join(path, "*.mp3")):
            file.write('%s %s\n' % (i,infile))
            i += 1
            in2 = infile.replace(" ","\ ")
        
            lista.append(infile)
            time.sleep(0.5)
    random.shuffle(lista)


if __name__ == '__main__':

    t = threading.Thread(name='archivos', target=archivos)

	t.start()
    t.join()
    
    d = threading.Thread(name='playeromx', target=player_lista, args=(lista,))
    d.setDaemon(True)
    d.start()
    print 'Aqui debe comenzar la musica'
    i2 = len(lista)
    print ('Total de canciones %s' % i2)
    
    while i2 > 0:
        time.sleep(3)
        #os.system('cls||clear')
        print '\nReproduciendo >>> ', song.split("/", 5)[-1]
        
        tipo=''
        while tipo not in [1, 2, 3]:
            print ('\nElige un numero (control de reproduccion):\n')
            print ('  1 - Play/Pausa\n  2 - Siguiente cancion\n  3 - Quit/Salir')
            try:
                tipo = int(raw_input('\nNumero ? '))
                
                if tipo > 3 or tipo < 1:
                    os.system('cls||clear')
                    print '--- Solo numeros 1 2 o 3 ---'
                    time.sleep(3)
                
            except ValueError:
                
                os.system('cls||clear')
                print ('\n*** SOLO NUMEROS 1, 2 o 3 POR FAVOR ***\n')
                time.sleep(3)
                continue
    
        if tipo == 1:
            print '\nPausado\n'
            proc.send('p')
    
        elif tipo == 2:
            print ('\nSiguiente\n')
            
            proc.send('q')
            i2 -= 1
            print i2
            
        elif tipo == 3:
            print ('\nSalir')
            exit()
    
        
       
    print 'Aqui termina '
	
    d.join()
	
	
