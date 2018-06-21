# Avalia��o: PostsAPI
(4� atividade)

## Considere as 3 seguintes entidades onde um usu�rio possui v�rios posts. Cada post possui v�rios coment�rios.
	� User: id, name, email, address { street, suite, city, zipcode }
	� Comment: id, name, email, body, postId
	� Post: id, title, body, userId

## Quest�es
	� a) (0,25) Listar os usu�rios e permitir o GET para listar e detalhar um usu�rio:
		http://servidor/profiles
		http://servidor/profiles/1 , onde 1 � o id do usu�rio;
	  (Feito)

	� b) (0,25) Criar um end point que liste os usu�rios, suas postagens e, para cada postagem, um n�mero total de coment�rios:
		http://servidor/profile-posts/
		http://servidor/profile-posts/1/ onde 1 � o id do usu�rio;
	  (Feito)

	� c) (0,25) Criar um outro end point, para permitir listar/detalhar/incluir/alterar/excluir um usu�rio espec�fico com suas postagens da seguinte forma:
		http://servidor/profiles/3/posts, onde o 3 representar� o id do usu�rio;
		http://servidor/profiles/3/posts/1, onde 1 � o id do post;
	  (Feito)

	� d) (0,25) Criar um outro end point, para permitir listar/detalhar/incluir/alterar/excluir coment�rios de uma postagem:
		http://servidor/profiles/3/posts/1/comments , onde o 3 representar� o id do usu�rio e 1 o id da postagem;
		http://servidor/profiles/3/posts/1/comments/2 , onde 2 � o id do coment�rio.
	  (Feito)

	� e) (0,25) Permitir que, ao excluir uma postagem, postagens excluir seus coment�rios;
	  (Feito)

	� f) (0,25) Criar um end point que liste e detalhe o total de posts e coment�rios nas postagens dos usu�rios. O formato da resposta deve ser algo como:
	{
	pk: 1,
	name: �jo�o�,
	total_posts: 5,
	total_coments: 30
	}
	  (Feito)

	� g) (0,5) Alguma implementa��o diferente da proposta sobre a base, usando algo relevante e ainda n�o visto na disciplina.
	  (Feito)


# Avalia��o: Autentica��es e Permiss�es na PostsAPI
(5� atividade)


#Com base nas entidades importadas do exerc�cio anterior (Post, Comment e User) e a WEB API desenvolvida, implemente o que se pede abaixo:

## 1. (1,0) Integre a classe User da aplica��o � user do Django:
	� a. Fa�a o relacionamento com a classe django.contrib.auth.model.User;
	� b. Verifique quest�es de nomes e amenize este conflito, pois um User ter um User fica um tanto amb�guo;
	� c. Crie usu�rios no Django para os usu�rios j� importados e fa�a as associa��es necess�rias;
	� d. Refatore sua aplica��o para permitir apenas �safe methods� para a sub-API de usu�rios, ou seja, para usu�rios fica tudo somente leitura e apenas para quem estiver logado;
	� (Feito - Falta D)


## 2. (1,0) Adicione um owner para as postagens e:
	� a. Apenas usu�rios logados podem postar algo;
	� b. Apenas os donos de uma postagem podem excluir e editar seus posts e excluir coment�rios de suas postagens;
	� c. A exclus�o de um post deve ser em cascata: ao excluir um post, seus coment�rios ser�o exclu�dos;
	� (Feito)

## 3. (0,5) Implemente o mecanismo de autentica��o via token:
	� a. Crie uma implementa��o personalizada que, ao solicitar um token, retorne o id do usu�rio, seu nome e o token;
	� b. Crie um endpoint para para solicitar token via post;
	� c. Adicione uma regra via throttling para que seja poss�vel obter um token apenas de hora em hora;
	� (Feito)

## 4. (0,5) Demais regras:
	� a. Crie uma API root para essa API semelhante ao criado em sala;
	� 
b. Limite aos demais endpoints da API para acesso n�o autenticado a 20 por hora e usu�rios autenticados a 50 por hora;
	� c. Use pagina��o para as postagens e para os coment�rios. Use um tamanho de p�gina com tamanho 10;
	� d. Gere um script de requisi��es em qualquer biblioteca de python que fa�a testes na API. No teste devem ser exibidos os status codes e detalhamento das respostas.