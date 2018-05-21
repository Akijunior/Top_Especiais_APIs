import requests
import json

# 1) Nome da API: Oxford Dictionaries
# 2) Utilidade: Consulta informações gramaticais de uma palavra em uma dada linguagem.
# 3) Link ou endpoint: https://developer.oxforddictionaries.com/
# 4) Possíveis recursos: Buscar informações sobre a palavra escolhida, com ou sem filtros, traduções,
#    busca de palavras similares, categorias, sentenças, utilidade
# 5) Métodos suportados: get
# 6) Exemplo(s) em python do método get
# 7) Exemplo(s) em python do método post: não tem

# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install


# Ex 1
app_id = ''
app_key = ''

language = 'en'
word_id = 'Changed'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/inflections/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))

# Ex 2
source_language = 'en'
target_language = 'pt'
word_id = 'Ace'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' +\
      source_language + '/' + word_id.lower() + '/translations=' + target_language

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))

# Ex 3
language = 'en'
word_id = 'Ace'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + '/synonyms;antonyms'

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))
