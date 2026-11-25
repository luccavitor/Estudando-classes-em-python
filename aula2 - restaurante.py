class Restaurante:
  # Fazendo uma lista dos restaurantes
  restaurantes = []

  #Adicionar o init: todo restaurante terá esses atributos
  def __init__(self,nome,categoria):
    self.nome = nome
    self.categoria = categoria
    self.ativo = False
    #Pegar a lista dos restaurantes e toda vez que criar um objeto colocar dentro da lista
    #Nesse caso todo restaurante novo é para colocar dentro da classe Restaurante
    Restaurante.restaurantes.append(self)

  #Para mostrar esse objeto em forma de texto sem usar o var ou o dir(biblioteca)
  def __str__(self):
    return f'{self.nome} | {self.categoria}'
  
  #Listar todos os restaurantes que está na lista
  def listar_restaurantes():
    for restaurante in Restaurante.restaurantes:
      print(f'{restaurante.nome}  | {restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restaurante('Praca','Gourmet')
restaurante_pizza = Restaurante('Pizza Express','Italiana')

#Classe Restaurante para listar os restaurantes que tem dentro dela
Restaurante.listar_restaurantes()


