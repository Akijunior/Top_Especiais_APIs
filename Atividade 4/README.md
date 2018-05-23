# Avalia��o: Games API
(4� atividade)

## Considere as 3 seguintes entidades onde um usu�rio possui v�rios posts. Cada post possui v�rios coment�rios.
	� User: id, name, email, address { street, suite, city, zipcode }
	� Comment: id, name, email, body, postId
	� Post: id, title, body, userId

## Importe o JSON repassado para o seu banco de dados ou use o script �dump� do mysql e crie uma API RESTful que atenta aos seguintes requisitos:
	a) Listar usu�rios; (Feito)
	b) Listar um usu�rio individualmente; (Feito)
	c) Altere a alternativa b) para listar al�m do usu�rio os links para as suas postagens; (Feito)
	d) Listar todas as postagens; (Feito)
	e) Altere a alternativa anterior para listar as postagens e o nome de seu usu�rio; (Feito)
	f) Listar uma postagem individualmente e o nome do seu usu�rio e links para seus coment�rios; (Feito)
	g) Incluir postagens; (Feito)
	h) Altere a alternativa f) anterior para listar uma postagem individualmente, seu nome de usu�rio e seus coment�rios; (Feito)
	i) Incluir coment�rios em uma postagem; (Feito)
	j) Excluir postagens e, obviamente, seus coment�rios. (Feito)
