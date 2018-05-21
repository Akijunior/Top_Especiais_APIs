# Avaliação: Games API
(2ª atividade)

## Questões:


### Pesquise qual o melhor padrão para validações extras em no DRF. Na própria view ou no serializer?


	Quando feita no Serializer, a validação é genérica, o que gera limitações quando comparada as validações por View, onde é possível criar algo mais específico ao que é desejado.


### Faça as seguintes validações na API proposta:


	- [POST, PUT]: Jogos não podem ter campos vazios;

	- [POST, PUT]: Jogos não podem ter nomes repetidos;

	- [DELETE]: Somente jogos que ainda não foram lançados podem ser excluídos;



Feito

### Que status codes você usaria? Ou usaria os mesmos? Pesquise e implemente;

	

	Usaria os mesmos, pois há recomendação no uso do 400 para alertar quanto a acessos ou movimentos indevidos.




### Retorne também uma informação descritiva ao retornar um erro de validação.

	
Feito