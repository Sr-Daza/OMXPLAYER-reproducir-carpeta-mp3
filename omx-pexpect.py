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

#from mutagen.mp3 import MP3

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def n():
    logging.debug('Starting')
    logging.debug('Exiting')

def di():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')
    print 'pruebe d'






def player_lista (mp3):
    global proc
    global song
    global musica
    #print mp3
    fin = 1
    keyb = ''
    #os.system('cls||clear')
    
    for song in mp3:
        musica = song.split("/", 4)[-1]
        song = song.replace(" ","\ ")
        #time.sleep(1)
        #print song
        os.system('cls||clear')
        print '\nReproduciendo ==> ', musica.split("/", 4)[-1]
        print '\nElige un numero y presiona ENTER (control de reproduccion):'
        print ('\n  1 - Play/Pausa\n  2 - Siguiente cancion\n  3 - Quit/Salir')
        
        proc = pexpect.spawn('omxplayer %s' %song) 
        proc.expect_exact('nice day', timeout=None)
        #ctrol = proc.interact()
        #print '\n\Ctrol impreso', ctrol
        time.sleep (1)
    proc.close()
    print "\nPlayList finalizada\n\nTenga un excelente dia ;-)"
    time.sleep(5)
    os.system('cls||clear')
    os._exit(1)
        #if ctrol == 'n'
         #   break
        #proc = subprocess.Popen(["omxplayer", song], stdin=subprocess.PIPE)
        #proc.wait()
        #print ('valor de fin ',fin)
        #time.sleep(2)
        #print proc.os.getpid()
    """
        while True:
            while keyb not in ['p', 'n', 'q']:
                keyb = raw_input('\n\n Opciones:\n p - pause\n n - next song\n q - quit \n\n Eleccion ? ')
            
            if keyb == 'p':
                proc.stdin.write(keyb)
                keyb = raw_input('\nEsperando: p para continuar\n')
                proc.stdin.write(keyb)
                keyb = ''
            elif keyb == 'n':
                proc.stdin.write('o')
                keyb = ''
                #proc.wait()
                #time.sleep(2)
                #break
            #salida4 = os.popen(proc).read()
        #print("Salida:\n", salida4)
                #fin = proc.wait()
                
   # proc.stdin.write('q')
            elif keyb == 'q':
                proc.stdin.write(keyb)
            #salida4 = os.popen(proc).read()
        #print("Salida:\n", salida4)
                proc.wait()
                sys.exit()
                
        print fin
   """
def archivos ():
    global lista
    global i2
    
    os.system('cls||clear')
    """ Comienza la reproduccion NORMAL de los archivos mp3 en la ruta (variable path).
    Al llegar al final de la lista de archivos mp3, la reproduccion se detiene.
    """
    path ='/home/daza/Musica'
    
    lista = []
    i = 0
    print '\nGenerando lista' # - Reproduccion aleatoria'
    #while(1):
    with open('lista.txt', 'r+') as file:

        for infile in glob.glob(os.path.join(path, "*.mp3")):
            file.write('%s %s\n' % (i,infile))
            i += 1
            #in2 = infile.replace(" ","\ ")
        #print (infile)
            lista.append(infile)
            time.sleep(0.5)
    random.shuffle(lista)
    i2 = len(lista)
    print ('\nTotal de canciones %s' % i2)
    time.sleep(4)
        #player(infile)

    #print lista
        #player = pexpect.spawn ('omxplayer %s' % in2)
        #player.expect_exact(';)', timeout=None)
        #time.sleep(20)
        #player.send('q')
        #time.sleep(1)

    #player_lista(lista)
 





if __name__ == '__main__':
    
   

    t = threading.Thread(name='non-daemon', target=archivos)

	
	

	#d.start()
    t.start()
	#time.sleep(7)
    #print 'continua'
    t.join()
    d = threading.Thread(name='daemon', target=player_lista, args=(lista,))
    d.setDaemon(True)
    d.start()
    #print '\nAqui debe comenzar la musica'
    #print '\nProceso vivo', d.isAlive()
	#vivo = d.isAlive()
    #i2 = len(lista)
    #print ('\nTotal de canciones %s' % i2)
    
    while i2 > 0:
        time.sleep(3)
        #os.system('cls||clear')
        #print ('\nReproduciendo >>> %s' % musica )
        
        tipo=''
        while tipo not in [1, 2, 3]:
            #print ('\nElige un numero (control de reproduccion):\n')
            #print ('  1 - Play/Pausa\n  2 - Siguiente cancion\n  3 - Quit/Salir')
            try:
                tipo = int(raw_input('\n __? '))
                
                if tipo > 3 or tipo < 1:
                    os.system('cls||clear')
                    print '--- Solo  1, 2 o 3 ---'
                    print ('\n  1 - Play/Pausa\n  2 - Siguiente cancion\n  3 - Quit/Salir')
                    time.sleep(3)
                #elif tipo < 1:
                #   print '--- NO SE ACEPTA MENOR QUE 1 ---'
                #  time.sleep(3)
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
            #random.shuffle(lista)
            #player_lista(lista)
            proc.send('q')
            i2 -= 1
            #print i2
            
        elif tipo == 3:
            #print ('\nSalir')
            proc.close()
            time.sleep(1)
            print "\nSaliendo. Tenga un exelente dia ;-) "
            time.sleep(3)
            os.system('cls||clear')
            exit()
    
        
        #proc.send('q')
        #i2 -= 1
        #print i2
    #print 'Aqui termina raw_imput'
	
    d.join()
	
	#while  vivo == True:
     #   ctrol = raw_input('Presiona p para pusar/renudar')
      #  proc.sendline(ctrol)

	#d.join()
#song = '/home/daza/Musica/p.mp3'
#songinfo = MP3('%s' % song)

#songtime = int(songinfo.info.length)
#print 'Total %s' % songtime
#while songtime > 0:
 #   songtime -= 10
  #  print songtime
   # time.sleep(1)

