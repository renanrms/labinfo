#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulo Python para extração de informações de um computador
# Necessita de privilégios de super-uduário!
# Use python 3.x


import lib.xmltodict as xmltodict
import os


# Obtenção de informações de hardware pelo lshw:

print ("Obtendo lshw... ")
status_comando = os.system("lshw -xml > lshw.xml")
if (status_comando == 0):
    print ("OK!")
else:
    print ("Erro ao obter lshw: " + str(status_comando))

lshw_xml = open('lshw.xml', 'r')
texto = lshw_xml.read()
lshw_xml.close()
lshw_dict = xmltodict.parse(texto) # lshw em forma de dicionário!!

# Obtenção do log do kernel pelo dmesg:

print ("Obtendo dmesg... ")

status_comando = os.system("dmesg > dmesg.txt")
if (status_comando == 0):
    print ("OK!")
else:
    print ("Erro ao obter dmesg: " + str(status_comando))

HWinfo = {
	"Motherboard" : {} ,
	"CPU" : {} ,
	"RAM" : {} ,
	"Storage" : {} ,
	"Driver" : {}
}

HWinfo["CPU"]["Width"] = lshw_dict["list"]["node"]["width"]

HWinfo_XML = xmltodict.unparse({"List" : HWinfo})

print ("Gravando arquivo de informações... ")
try:
	HWinfo_file = open("18.01.001.xml", 'w')
	HWinfo_file.write(HWinfo_XML + "\n")
	HWinfo_file.close()
	print ("OK!")
except:
    print ("Erro ao gravar arquivo.")


#print (HWinfo)  # Visualiza o dicionário final.
#print (HWinfo_XML)  # Visualizao xml que vai para o arquivo.
#print (xmltodict.parse(HWinfo_XML))  # Visualiza o dicionário que seria obtido deste XML pelo módulo central.
