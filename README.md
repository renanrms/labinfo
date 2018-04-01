# Labinfo

Software pra obtenção e registro de especificações de computadores em um contexto de multiplos laboratórios de informática.
Este é um software em fase de projeto/desenvolvimento que surge das necessidades do Laboratório de Informática para a Educação na Universidade Federal do Rio de Janeiro - LIpE/UFRJ.

O projeto é dividido em duas partes que precisam se encaixar:
* Um programa para obter as informações dos computadores a ser utilizado nos laboratórios, em campo. (módulo extrator)
* Um programa para gerenciamento das informações obtidas, utilizado em um computador central. (módulo central)

Este software se destina, a princípio, para sistemas Linux, devendo funcionar em diferentes distribuições.

A seguir, serão descritos ambos os módulos, inclusive para guiar a implementação...

### Módulo extrator

#### Requisitos

* Portabilidade em diferentes distribuições Linux sem pressupor instalação de programas excepcionais
* Ser capaz de funcionar apartir do pendrive
* Obter as especificações, as informações de uso e os dados de saúde do hardware mais importantes do computador em questão
* Armazenar dados extras para consulta eventual
* Armazenar informações que facilitem uma posterior organização dor registros: horário, nome do computdor e nome do laborátorio 
* Possuir uma saída legível idependentemente do módulo central, em prol da flexibilidade de utilização

Para coseguir isto, faremos o programa em Python e quando for preciso lidar com arquivos XML, usaremos a biblioteca xmltodict para converter XML em dicionário (também conhecido como mapa) e dicionário em XML.

#### Funcionamento em etapas

1. Verificar se está rodando com permissões de root e, caso contrário, abortar.
2. Obter informações a partir do usuário
	* Nome que identifique o computador de forma única (código do PC)
	* Selecionar pasta do laboratório em quastão
	* Confirmação do horário
3. Criar pasta para as informações do computador, nomeada com o seu código.
4. Armazenar as saídas dos comandos a seguir em arquivos
	* lshw -xml (nome: lshw.xml)
	* dmesg (nome: dmesg.txt)
5. Obter as informações a seguir e armazenar em um arquivo XML (nome: <codigo_pc>.xml)
	* Versão do Labinfo
	* Data com precisão de segundos em formato para ordenação (aaaammddhhss)
	* Placa-mãe
		* Modelo
		* Número de slots de memória
		* Número de portas SATA
		* Número de slots PCI
		* Número de slots PCIe
	* CPU
		* Modelo
		* Arquitetura (32 bit, 64 bits)
		* Frequência (MHz)
	* Memória RAM
		* Tamanho (MB)
		* Tecnologia (DDR, DDR2, DDR3, etc)
		* Frequência de operação (MHz)
		* Modo do canal (single chanel, dual chanel, quad chanel, flex)
		* Para cada pente:
			* Tamanho (MB)
			* Frequência máxima (MHz)
			* Slot
	* Dísco Rígido (para cada HD)
		* Modelo
		* Tamanho (GB)
		* Porta (SATA, PATA/IDE)
		* Status SMART (Parâmetros a definir)
	* Driver de CD/DVD (para cada driver)
		* Modelo
		* Capacidades (leitura/escrita CD, leitura/escrita DVD)
		* Porta (SATA, PATA/IDE)

### Módulo central

#### Requisitos

* Manter um registro com pastas por computador contendo todo o histórico de cada um.
* Manter um registro dos laboratórios existentes com histórico dos PCs pertencentes.
* Permitir a inserção de informações através de pastas com os dados atualizados dos PCs de um mesmo laboratório e incorporá-las aos registros descritos acima.
* 
