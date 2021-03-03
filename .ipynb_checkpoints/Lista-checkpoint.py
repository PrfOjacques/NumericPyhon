class No:
  def __init__(self, carga=None, proximo=None): #constructor 
    self.carga = carga
    self.proximo = proximo

  def __str__(self): #para utilizar com print
    return str(self.carga)


def imprimeLista(no):
  while no:
    print(no)
    no = no.proximo
  print("")

def imprimeDeTrasParaFrente(lista):
  if lista == None : return
  cabeca = lista
  rabo = lista.proximo
  imprimeDeTrasParaFrente(rabo)
  print(cabeca)

no = No("teste") #instancia um variavel no do tipo No

no1 = No(1)
no2 = No(2)
no3 = No(3)

#Ligando os nós

no1.proximo = no2
no2.proximo = no3

imprimeLista(no1)



