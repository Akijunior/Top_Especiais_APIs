# Avaliação: Games API
(4ª atividade)

## Considere as 3 seguintes entidades onde um usuário possui vários posts. Cada post possui vários comentários.
	• User: id, name, email, address { street, suite, city, zipcode }
	• Comment: id, name, email, body, postId
	• Post: id, title, body, userId

## Questões
	• a) (0,25) Listar os usuários e permitir o GET para listar e detalhar um usuário:
		http://servidor/profiles
		http://servidor/profiles/1 , onde 1 é o id do usuário;
	  (Feito)

	• b) (0,25) Criar um end point que liste os usuários, suas postagens e, para cada postagem, um número total de comentários:
		http://servidor/profile-posts/
		http://servidor/profile-posts/1/ onde 1 é o id do usuário;
	  (Feito)

	• c) (0,25) Criar um outro end point, para permitir listar/detalhar/incluir/alterar/excluir um usuário específico com suas postagens da seguinte forma:
		http://servidor/profiles/3/posts, onde o 3 representará o id do usuário;
		http://servidor/profiles/3/posts/1, onde 1 é o id do post;
	  (Feito)

	• d) (0,25) Criar um outro end point, para permitir listar/detalhar/incluir/alterar/excluir comentários de uma postagem:
		http://servidor/profiles/3/posts/1/comments , onde o 3 representará o id do usuário e 1 o id da postagem;
		http://servidor/profiles/3/posts/1/comments/2 , onde 2 é o id do comentário.
	  (Feito)

	• e) (0,25) Permitir que, ao excluir uma postagem, postagens excluir seus comentários;
	  (Feito)

	• f) (0,25) Criar um end point que liste e detalhe o total de posts e comentários nas postagens dos usuários. O formato da resposta deve ser algo como:
	{
	pk: 1,
	name: “joão”,
	total_posts: 5,
	total_coments: 30
	}
	  (Feito)

	• g) (0,5) Alguma implementação diferente da proposta sobre a base, usando algo relevante e ainda não visto na disciplina.
	  (Feito)