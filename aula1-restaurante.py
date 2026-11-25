#classe no python: Essa clase irá representar um restaurante
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

# Criar um restaurante(Objeto) novo através de uma classe:
restaurante_praca = Restaurante()
restaurante_lucca = Restaurante()

# Para definir as informações desse restaurante
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'
restaurante_praca.ativo = False

restaurante_lucca.nome = 'Lucca'
restaurante_lucca.categoria = 'Italiana'
restaurante_lucca.ativo = True

# Para visualizar esses restaurantes: Irá aparecer no terminal como objeto
restaurantes = [restaurante_praca, restaurante_lucca]
print(restaurantes)

# Função dir: Para ver os atributos do objeto
# Ela retorna uma lista ordenada de nomes(atributos, métodos e variáveis)
# disponíveis em um objeto ou no escopo atual
print(dir(restaurante_praca))
print(dir(restaurante_lucca))


# Para ver o dicionário de um objeto (O que tem dentro dele):
print(vars(restaurante_praca))

# Exercício:
class música:
    nome = ''
    artista = ''
    duracao = int

musica_pop = música()
musica_pop.nome = 'pop'
musica_pop.artista = 'Artista da música pop'
musica_pop.duracao = 180
print(vars(musica_pop))


#Exerciío:
#1 - Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca.categoria = 'Italiana'

#2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
nome_do_restaurante = restaurante_praca.nome

#3 - Imprima o valor do atributo ativo da instância restaurante_praca da classe Restaurante.
if restaurante_praca.ativo:
  print('O restaurante está ativo.')
else:
  print('O restaurante não está ativo.')

#4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante.
categoria = Restaurante.categoria

#5 - Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistrô'

#6 -Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza place'
restaurante_pizza.categoria = 'Fast Food'

#7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
  print('A categoria é Fast Food.')
else:
  print('A categoria não é Fast Food.')

#8 - Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

#9 - Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')
