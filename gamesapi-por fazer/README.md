# Avalia��o: Games API
(2� atividade)

## Quest�es:


### Pesquise qual o melhor padr�o para valida��es extras em no DRF. Na pr�pria view ou no serializer?


	Quando feita no Serializer, a valida��o � gen�rica, o que gera limita��es quando comparada as valida��es por View, onde � poss�vel criar algo mais espec�fico ao que � desejado.


### Fa�a as seguintes valida��es na API proposta:


	- [POST, PUT]: Jogos n�o podem ter campos vazios;

	- [POST, PUT]: Jogos n�o podem ter nomes repetidos;

	- [DELETE]: Somente jogos que ainda n�o foram lan�ados podem ser exclu�dos;



Feito

### Que status codes voc� usaria? Ou usaria os mesmos? Pesquise e implemente;

	

	Usaria os mesmos, pois h� recomenda��o no uso do 400 para alertar quanto a acessos ou movimentos indevidos.




### Retorne tamb�m uma informa��o descritiva ao retornar um erro de valida��o.

	
Feito