#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : LinkSec

import requests,sys,time,os,itertools

os.system("color 0a && cls")
#os.system("clear")
def iniciar():
	print ""
	print "python pagenc.py http://www.exemplo.com/"
encontradas = []
if len(sys.argv) >=2:
	print "\n[+] Script iniciado ...\n"
	lista = ["admin.php","admin.html","index.php","login.php","login.html","administrator","admin","adminpanel","cpanel","login"]
	# lista = open("lista.txt", "r") Usar com arquivo...
	try:
		for i in lista:
			url = sys.argv[1] + i
			r = requests.get(url)
			sys.stdout.flush()
			if r.status_code == 200:
				add = encontradas.append(url)

				print "[+] ENCONTRADA : " + url
			else:
				print "[-] NÃO ENCONTRADA : " + url
		print ('\n[-] Tempo: %s' % time.strftime('%H:%M:%S'))
		print ('Encontradas: {}'.format(encontradas))
	except KeyboardInterrupt:
		print "\n[x] Script abortado"
	except:
		print "[x] Ocorreu algum erro na segmentacao ..."
else:
	iniciar()
