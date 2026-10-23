#Repetindo tarefas com For

#n= 4
#for i in range(1,n):
# range() é uma função que gera uma sequência de números, no caso de 1 até n-1, ou seja, 1, 2 e 3.
#    print(i)

#nome =  "Daniel"
#for letra in nome:
#    print(letra)

#tecnologias = ["Python", "Java", "C#", "JavaScript"]
#for item in tecnologias:
#    print(item)

#perfil = {"nome": "Odeth", "idade": 18, "cidade": "Luanda", "profissao": "Programadora", "Data de nascimento": "26/10/2008"}
#for chave in perfil:
#    print(chave, perfil[chave])
# chave é a palavra que representa o nome do item, e perfil[chave] é o valor associado a essa chave no dicionário.
# eSscrevemos perfil[chave] para acessar o valor associado à chave no dicionário perfil.


#tecnologias = ["Python", "Java", "C#", "JavaScript"]
#for item in range(len(tecnologias)):
    #range(len(tecnologias)) gera uma sequência de números de 0 até o tamanho da lista tecnologias - 1, ou seja, 0, 1, 2 e 3.
    #len(tecnologias) retorna o tamanho da lista tecnologias, que é 4.
    #len() é uma função que retorna o tamanho de um objeto, no caso a lista tecnologias.
  #  print(tecnologias[item])


for indice in range(5):
    print("O valor do índice é:", indice)