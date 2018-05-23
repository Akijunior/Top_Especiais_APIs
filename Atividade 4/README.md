# Avaliação: Games API
(4ª atividade)

## Considere as 3 seguintes entidades onde um usuário possui vários posts. Cada post possui vários comentários.
	• User: id, name, email, address { street, suite, city, zipcode }
	• Comment: id, name, email, body, postId
	• Post: id, title, body, userId

## Importe o JSON repassado para o seu banco de dados ou use o script “dump” do mysql e crie uma API RESTful que atenta aos seguintes requisitos:
	a) Listar usuários; (Feito)
	b) Listar um usuário individualmente; (Feito)
	c) Altere a alternativa b) para listar além do usuário os links para as suas postagens; (Feito)
	d) Listar todas as postagens; (Feito)
	e) Altere a alternativa anterior para listar as postagens e o nome de seu usuário; (Feito)
	f) Listar uma postagem individualmente e o nome do seu usuário e links para seus comentários; (Feito)
	g) Incluir postagens; (Feito)
	h) Altere a alternativa f) anterior para listar uma postagem individualmente, seu nome de usuário e seus comentários; (Feito)
	i) Incluir comentários em uma postagem; (Feito)
	j) Excluir postagens e, obviamente, seus comentários. (Feito)
