# Avaliação: PostsAPI
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


# Avaliação: Autenticações e Permissões na PostsAPI
(5ª atividade)


#Com base nas entidades importadas do exercício anterior (Post, Comment e User) e a WEB API desenvolvida, implemente o que se pede abaixo:

## 1. (1,0) Integre a classe User da aplicação à user do Django:
	• a. Faça o relacionamento com a classe django.contrib.auth.model.User;
	• b. Verifique questões de nomes e amenize este conflito, pois um User ter um User fica um tanto ambíguo;
	• c. Crie usuários no Django para os usuários já importados e faça as associações necessárias;
	• d. Refatore sua aplicação para permitir apenas “safe methods” para a sub-API de usuários, ou seja, para usuários fica tudo somente leitura e apenas para quem estiver logado;
	• (Feito - Falta D)


## 2. (1,0) Adicione um owner para as postagens e:
	• a. Apenas usuários logados podem postar algo;
	• b. Apenas os donos de uma postagem podem excluir e editar seus posts e excluir comentários de suas postagens;
	• c. A exclusão de um post deve ser em cascata: ao excluir um post, seus comentários serão excluídos;
	• (Feito)

## 3. (0,5) Implemente o mecanismo de autenticação via token:
	• a. Crie uma implementação personalizada que, ao solicitar um token, retorne o id do usuário, seu nome e o token;
	• b. Crie um endpoint para para solicitar token via post;
	• c. Adicione uma regra via throttling para que seja possível obter um token apenas de hora em hora;
	• (Feito)

## 4. (0,5) Demais regras:
	• a. Crie uma API root para essa API semelhante ao criado em sala;
	• 
b. Limite aos demais endpoints da API para acesso não autenticado a 20 por hora e usuários autenticados a 50 por hora;
	• c. Use paginação para as postagens e para os comentários. Use um tamanho de página com tamanho 10;
	• d. Gere um script de requisições em qualquer biblioteca de python que faça testes na API. No teste devem ser exibidos os status codes e detalhamento das respostas.