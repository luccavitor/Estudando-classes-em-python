class Música:
  
  #Criando uma lista com as música:
  musicas = []

  #Atributos de toda música criada:
  def __init__(self,nome,artista,duracao):
    self.nome = nome
    self.artista = artista
    self.duracao = duracao
    #Adicionar uma nova música na lista
    Música.musicas.append(self)

  #Para mostrar esse objeto em forma de texto sem usar o var ou o dir(biblioteca)
  def __str__(self):
    return f'{self.nome} | {self.artista} | {self.duracao}'

  #Listas as músicas
  def listar_musicas():
    for musica in Música.musicas:
      print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica_aurora = Música('Aurora','Jão','180')
musica_ausencia = Música('Ausência','Veigh','180')

Música.listar_musicas()
