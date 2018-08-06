#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Programa para extração de informações sobre hardware e software de um computador.
# Necessita de privilégios de super-usuário!
# Use python 3.x


import lib.xmltodict as xmltodict
import os
from datetime import datetime


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

## Confirma data e hora atuais:

now = datetime.now()

answer = input ("A informação de data e hora do sistema (" + now.strftime("%d/%m/%Y %H:%M") + ") está correta? (S/N) ")

if not (answer == "S" or answer == "s"):
	print ("")
	print ("A data e a hora são importantes para o registro.")
	print ("Acerte-as primeiro e rode o programa novamente.")
	exit ()

## Solicita a pasta do laboratório onde registrar o computador:

print ("Agora informe a pasta onde registrar o computador.")
print ("Por padrão, o computador será registrado em uma pasta 'Labinfo - dados', ao lado da pasta deste programa.")
print ("Dica: use a mesma pasta para os computadores de um mesmo laboratório.")

### Imprime as pastas já existentes dentro do diretório padrão informado:

if not (os.path.exists("../Labinfo - dados/")):
	os.mkdir("../Labinfo - dados/")

entrieList = os.listdir("../Labinfo - dados/")  # listagem do diretório.

folderList = []
for entrie in entrieList:
	if (os.path.isdir(entrie)):
		folderList += [entrie]

if (folderList != []):
	print ("OBS.: Já existem pastas dentro na 'Labinfo - dados':")
	for folderName in folderList:
		print (folderName)

### Finalmente, solicita o nome da pasta ao usuário e a cria se preciso:

labFolder = input ("Nome da pasta: ")  ### Encontrar uma forma de ter um autocompletar (tecla TAB) relativo à pasta padrão do registro e não à pasta do programa.

if (labFolder[0] != "/"):
	labFolder = "../Labinfo - dados/" + labFolder

if not (os.path.exists(labFolder)):
	os.mkdir(labFolder)

## Solicita o código de registro do computador:

computerCode = input ("Digite o código deste computador (formato XX.XX.XXX): ")

### INSERIR O TRATAMENTO DO DADO INPUTADO ###

computerFolder = labFolder + "/" + computerCode

if not (os.path.exists(computerFolder)):
	os.mkdir(computerFolder)

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
