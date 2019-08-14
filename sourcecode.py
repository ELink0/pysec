import urllib2

resposta = urllib2.urlopen("http://google.com.br")
cod_fonte = resposta.read()
arquivo = open("codigo.html","w")
arquivo.write(cod_fonte)
arquivo.close()
