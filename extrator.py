#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programa para extração de informações sobre hardware e software de um computador.
# Necessita de privilégios de super-usuário!
# Use python 3.x


import lib.xmltodict as xmltodict
import os


# Verifica se está com privilégios de super-usuário:
###	Ver se é possível pedir a senha e obter os privilégios aqui.
### Dar boas práticas de programação no uso das cores e aplicar às outras mensagens do programa.

if (os.geteuid() != 0):
	print ("\033[1m" + "AVISO: " + "\033[31m" + "você deveria executar este programa como super-usuário." + "\033[0m")
	print ("       Sem privilégios de super-usuário algumas informações não podem ser acessadas.")
	print ("")
	print ("\033[1m" + "USO: " + "\033[0m" + "sudo python3 extrator.py")
	print ("\033[1m" + " OU: " + "\033[0m" + "su")
	print ("     python3 extrator.py")
	print ("")

# Solicita dados ao usuário:

## Solicita o código de registro do computador:

### INSERIR CÓDIGO ###

## Solicita a pasta do laboratório onde registrar o computador:

### INSERIR CÓDIGO ###

## Confirma data e hora atuais:

### INSERIR CÓDIGO ###

# Obtém informações de hardware pelo lshw:

print ("Obtendo lshw... ")
### Aqui vai um pouco de Shell Script:
### redirecionaremos a saída do comando para "lshw.xml" e a saída de erro para ".lshw_error_messages".
### redirecionar o erro é necessário para determinar quais mensagens aparecem para o usuário.
status_comando = os.system("lshw -xml > lshw.xml 2> .lshw_error_messages")
if (status_comando == 0):
    print ("OK!")
else:
    print ("Erro ao obter lshw: " + str(status_comando))

### Remove o arquivo temporário.
os.remove(".lshw_error_messages")

lshw_xml = open('lshw.xml', 'r')
texto = lshw_xml.read()
lshw_xml.close()
lshw_dict = xmltodict.parse(texto) # lshw em forma de dicionário!!

# Obtém o log do kernel pelo dmesg:

print ("Obtendo o log do kernel... ")

status_comando = os.system("dmesg > dmesg.txt")  # Verificar a possibilidade de gravar a cor de cada linha neste arquivo.
if (status_comando == 0):
    print ("OK!")
else:
    print ("Erro ao obter dmesg: " + str(status_comando))

# Agora inicializamos o dicionário e atribuímos os dados:

PCinfo = {
	"Placa-mae" : {
		"Modelo" : "" ,
	} ,
	"CPU" : {
		"Modelo" : "" ,
		"Arquitetura" : "" ,
		"Frequência" : ""
	} ,
	"RAM" : {} ,
	"Armazenamento" : {} ,
	"Driver optico" : {} ,
	"Estado" : {} ,
	"Software" : {}
}

## Obtém os dados do hardware:

PCinfo["CPU"]["largura"] = lshw_dict["list"]["node"]["width"]

### COMPLETAR CÓDIGO ###

## Obtém os dados de saúde do hardware:

### INSERIR CÓDIGO ###

## Obtém os dados sobre programas instalados:

### INSERIR CÓDIGO ###

# Transforma o dicionário em XML e grava em arquivo:

PCinfo = {"List" : PCinfo}  # O método exige que haja um nó raiz no dicionário.
PCinfo_XML = xmltodict.unparse(PCinfo, encoding='utf-8', pretty=True)

print ("Gravando informações em arquivo... ")
try:
	PCinfo_file = open("18.01.001.xml", 'w')
	PCinfo_file.write(PCinfo_XML + "\n")
	PCinfo_file.close()
	print ("OK!")
except Exception as e:
    print ("Erro: " + str(e))

# Posiciona os arquivos e altera as permissões para que usuários comuns possam mover os arquivos (chmod 666).

### INSERIR CÓDIGO ###



# Testes
#print (HWinfo)  # Visualiza o dicionário final.
#print (HWinfo_XML)  # Visualizao xml que vai para o arquivo.
#print (xmltodict.parse(HWinfo_XML))  # Visualiza o dicionário que seria obtido deste XML pelo módulo central.
