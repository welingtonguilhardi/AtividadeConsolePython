global codigo
codigo = 0 #varialvel responsavel por denominar codigo de cada peça
global lista
lista = [] #varialvel responsavel por armazenar informações dentro de uma lista 
global lista_info
lista_info = {} #varialvel responsavel por preencher informações das peças cadastradas 




def cadastrarPeca(codigo):
    codigo += 1
    print (f'Código da Peça: {codigo}')
    lista_info['Codigo da peça: '] = codigo
    lista_info['Nome da peça: '] = input("Nome da peça: ") #varialvel responsavel por armazenar o nome da peça
    lista_info['Fabricante da peça: '] = input("Fabricante da peça: ") #varialvel responsavel por armazenar o fabricante da peça
    lista_info['Valor da peça: '] = float(input("Valor da peça: ")) #varialvel responsavel por armazenar o valor da peça
    lista.append(lista_info.copy()) #copia das informações das peças armazenando tudo em um dicionario dentro de uma lista




def consultarPeca ():
 while True:
  print ('\nVocê escolheu a opção Consultar peças ')
  pergunta = int(input('Escolha a opção desejada: \n1-Consultar Todas as Peças\n2-Consultar Peças por Código\n3-Consultar Peças por Fabricante\n4-Retornar\n '))

  if pergunta == 1:
   for e in lista:
    print('\n')
    for i,j in e.items():
        print (f'{i} {j}')


  if pergunta == 2:
    busca_codigo = int(input('Qual codigo deseja buscar?')) #varialvel responsavel por armazenar codigo desejado para busca  
    for x in lista: 
      print('\n')
      if x["Codigo da peça: "] == busca_codigo: #verificação se codigo existe na lista 
       for i,j in x.items():
          print (f'{i} {j}')   
  
  if pergunta == 3:
      busca_fabricante = input('Qual fabricante da peça desejada ?') #varialvel responsavel por armazenar o fabricante desejado para busca
      for x in lista: 
       print('\n')
       if x["Fabricante da peça: "] == busca_fabricante: #verificação se fabricante existe na lista
        for i,j in x.items():
           print (f'{i} {j}')
  
  if pergunta == 4:
    break

def removerPeca():
  print ('Você escolheu a opção Remover peças ')
  excluir_codigo = int(input('Qual codigo do produto que deseja excluir? ')) #varialvel responsavel por armazenar codigo desejado para busca e exclusão
  for x in lista: 
    if x["Codigo da peça: "] == excluir_codigo: #verificação se codigo existe na lista 
       x.pop('Codigo da peça: ')  #função responsavel pela exclusão do codigo da peça
       x.pop('Nome da peça: ') #função responsavel pela exclusão do nome da peça
       x.pop('Fabricante da peça: ') #função responsavel pela exclusão do fabricante da peça
       x.pop('Valor da peça: ') #função responsavel pela exclusão do valor da peça
    
    
    



print('Bem vindo ao controle de estoque da bicicletaria do Welington Guilhardi')






while True:
    
    
    
    print ('Escolha a opção desejada:\n1-Cadastrar peças\n2-Consultar peças\n3-Remover peças\n4-sair')
    opcao = int(input('')) #varialvel responsavel por armazenar opção do usuario 
    

    if opcao == 4:
       print ('Você escolheu a opção Sair') 
       break
    elif opcao == 1:
      print ('Você escolheu a opção Cadastrar peças ')
      cadastrarPeca(codigo)
      codigo += 1

    elif opcao == 2:
      consultarPeca ()
      

    elif opcao == 3:
      removerPeca()
