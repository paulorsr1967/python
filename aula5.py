# listas
print('Olá Mundo!')
print("Olá Mundo2!")
lista = [1, 2, 3, 4, 5, 0]
lista_animal = ['cachorro', 'gato', 'papagaio']
print(lista)
print(lista_animal)

soma = 0
for x in lista:
    print(x)
    soma += x
print(f'soma: {soma}')
print('soma: {}'.format(soma))
print(sum(lista))
print(max(lista))
print(min(lista))
print(max(lista_animal))
print(min(lista_animal))
pesquisa = 'gato'
if pesquisa in lista_animal:
    print(f'Existe um {pesquisa} na lista')
else:
    print(f'Não existe um {pesquisa} na lista')
