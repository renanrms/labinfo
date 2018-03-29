# labinfo

Software pra obtenção e registro de especificações de computadores em um contexto de multiplos laboratórios de informática.
Este é um software em fase de projeto/desenvolvimento que surge das necessidades do Laboratório de Informática para a Educação na Universidade Federal do Rio de Janeiro - LIpE/UFRJ.

O projeto é dividido em duas partes que precisam se encaixar:
* Um programa para obter as informações dos computadores a ser utilizado nos laboratórios, em campo. (módulo campo)
* Um programa para gerenciamento das informações obtidas, utilizado em um computador central. (módulo central)

Este software se destina essencialmente para sistemas Linux, porém com diferentes distribuições.

A seguir serão descritos brevemente ambos os módulos, inclusive para guiar a implementação...

## Módulo campo

Requisitos:
* Portabilidade em diferentes distribuições Linux
* Obter as informações de hardware mais importantes do computador em questão. A saber:
	* Placa-mãe
		* modelo
		* número de slots de memória
		* número de portas SATA
	* Memória RAM
		* Tamanho
		* Frequência de operação
		* Tamanho de cada pente
		* Frequência máxima de cada pente

## Módulo central

## Método de implementação

