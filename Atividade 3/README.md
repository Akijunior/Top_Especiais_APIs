# Atividade 3

## Fazer valida��o em serializers

## 1. Proponha valida��es do modelo na entidade
Score, usando prioritariamente valida��es nos
serializers:
	� Player e game n�o selecionado;
	� Score negativo ou n�o preenchido;
	� Data do score no futuro.
	Feito!

## 2. � poss�vel simplificar mais ainda as views
usando o DRF, visto que o c�digo ficou
repetitivo? Proponha uma alternativa.

	- Fazer uso do GenericAPIView para as classes, assim podendo evitar a repeti��o continua de c�digos.