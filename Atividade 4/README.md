# Avalia��o: Games API
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