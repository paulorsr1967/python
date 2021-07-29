pares = [0, 2, 4, 8, 10]
pares.insert(3, 6)
print(pares)  # resultado: [0, 2, 4, 6, 8, 10]

aprovados = ['Mario', 'Peach', 'Luigi']
reprovados = ['Wario', 'Bowser']

print('Candidatos aprovados:')
for nome in aprovados:
    print('\t', nome)

print('Candidatos reprovados:')
for nome in reprovados:
    print('\t', nome)

frase = "Estou escrevendo"
print(frase)
frase = 'Não ' + frase.lower()
print(frase)

lista = [1, 2, 3, 4, 5, 6]
for elemento in lista:
    print(elemento)

print('Teste 1')
n = 8
for i in range(1, n + 1, 2):
    print(i)

print('Teste 2')
# from sys import stdin, stdout
# tea = int(input())
tea = 1
correct = 0
# for guess in list(stdin.readline().split()):
for guess in list([1, 2, 3, 4, 1, 5]):
    if int(guess) == tea:
        correct = correct + 1
# stdout.write(str(correct))
print(str(correct))

print('Teste 3')
# d = [int(x) for x in input().split()]
# r = [int(x) for x in input().split()]
d = [int(x) for x in [80, 20, 30]]
r = [int(x) for x in [35, 28, 41]]
dif = 0
for x in range(0, len(d)):
    if d[x] < r[x]:
        dif += r[x] - d[x]
print(dif)

print('Exercício 1')
lista = [1, 2, 3, 4, 5, 6]
for elemento in lista:
    print(elemento)

print('Exercício 2')
lista = [1, 2, 3, 4, 5, 6]
indice = 0
tamanho = len(lista)
while indice < tamanho:
    print(lista[indice])
    indice += 1

print('Exercício 3')
lista = []
# numero = int(input('Informe o número : '))
numero = 8
for indice in range(0, numero):
    lista.append(indice)
print(lista)

print('Exercício 4')
lista = [1, 2, 3, 4, 5, 6, 7]
par = 0
for numero in lista:
    if numero % 2 == 0:
        par += 1
print('A lista contem ', par, ' números pares')

print('Exercício 5')
lista = [1, 2, 3, 4, 5, 6, 7]
maior = lista[0]
for numero in lista:
    if numero > maior:
        maior = numero
print('O maior número da lista é : ', maior)

print('Exercício 6')
lista = [1, 2, 3, 4, 5, 6, 7]
numero1 = max(lista)
lista.remove(numero1)
numero2 = max(lista)
lista.remove(numero2)
numero3 = max(lista)
lista.remove(numero3)
print('Os três maiores números da lista são : ', numero1, ',', numero2, ', ', numero3)

print('Exercício 7')
lista1 = [1, 4, 5]
lista2 = [2, 2, 3]
lista3 = []
tamanho = len(lista1)
for indice in range(0, tamanho):
    lista3.append(lista1[indice] + lista2[indice])
print(lista3)

print('Exercício 8')
lista1 = [1, 4, 5]
lista2 = [2, 2, 3]
lista3 = []
tamanho = len(lista1)
for indice in range(0, tamanho):
    lista3.append(lista1[indice] * lista2[indice])
print(lista3)

print('Exercício 9 e 10')
lista = []
for indice in range(0, 5):
    numero = input('Informe um número : ')
    lista.append(numero)
print(lista)
for indice in range(0, len(lista)):
    lista[indice] = float(lista[indice])
print(lista)

print('Exercício 11')
lista = []
for indice in range(0, 4):
    numero = float(input('Informe a nota : '))
    lista.append(numero)
soma = 0
for numero in lista:
    soma += numero
print('A média é ', soma / len(lista))

print('Exercício 12')
import random

lista = []
for indice in range(0, 10):
    lista.append(random.randrange(0, 101))
print(lista)
primeiros4 = lista[:4]
print(primeiros4)
ultimos5 = lista[-5:]
print(ultimos5)
posicaoPar = lista[::2]
print(posicaoPar)
posicaoImpar = lista[1::2]
print(posicaoImpar)
inversa = lista
inversa.reverse()
print(inversa)
inversaPrimeiros5 = lista[:5]
inversaPrimeiros5.reverse()
print(inversaPrimeiros5)
inversaUltimos5 = lista[5:]
inversaUltimos5.reverse()
print(inversaUltimos5)

print('Exercício 13')
import random

lista = []
for indice in range(0, 10):
    lista.append(random.randrange(0, 101))
print(lista)
maior50 = 0
for numero in lista:
    if numero > 50:
        maior50 += 1
print(maior50, ' numeros são maiores que 50')

print('Exercício 14')
import random

lista = []
for indice in range(0, 10):
    lista.append(random.randrange(0, 101))
print(lista)
print('O maior número sorteado : ', max(lista))
print('O menor número sorteado : ', min(lista))
soma = 0
for numero in lista:
    soma += numero
print('A média dos números sorteados : ', soma / len(lista))
print('A soma dos números sorteados : ', soma)

print('Desafio 1')
nome = input('Informe o nome do aluno : ')
idade = int(input('Informe a idade do aluno : '))
qtd = int(input('Quantas provas o aluno fez ? '))
lista = []
lista.append(nome)
lista.append(idade)
notas = []
for indice in (range(0, qtd)):
    nota = float(input('Informe a nota : '))
    notas.append(nota)
lista.append(notas)
soma = 0
for nota in notas:
    soma += nota
media = soma / qtd
lista.append(media)
if media > 5:
    lista.append(True)
else:
    lista.append(False)
print(lista)

print('Desafio 2')
nome = input('Informe o nome do aluno : ')
idade = int(input('Informe a idade do aluno : '))
continua = True
while continua:
    qtd = int(input('Quantas provas o aluno fez (mais de 2) ? '))
    if qtd > 2:
        continua = False
lista = []
lista.append(nome)
lista.append(idade)
notas = []
for indice in (range(0, qtd)):
    nota = float(input('Informe a nota : '))
    notas.append(nota)
notas_original = notas
notas.sort()
notas.pop(0)
notas.pop(qtd - 2)
lista.append(notas)
soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)
lista.append(media)
if media > 5:
    lista.append(True)
else:
    lista.append(False)
print(lista)

print('Desafio 3')
cpf = input('Informe o CPF (somente números : ')
soma1 = 0
soma2 = 0
valido = False
for indice in range(10, 1, -1):
    soma1 += indice * int(cpf[10 - indice])
if soma1 * 10 % 11 == int(cpf[9]):
    valido = True
    for indice in range(11, 1, -1):
        soma2 += indice * int(cpf[11 - indice])
    if soma2 * 10 % 11 == int(cpf[10]):
        valido = True
    else:
        valido = False
print('O CPF ', cpf, ' � ', valido)

print('Exercício String 01')
palavra = input('Digite uma palavra : ')
for letra in palavra:
    print(letra)

print('Exercício String 02')
palavra = input('Digite uma palavra : ')
novaString = ""
for letra in palavra:
    novaString += letra
print(novaString)

print('Exercício String 03')
palavra = input('Digite uma palavra : ')
novaString = ""
maiuscula = True
for letra in palavra:
    if maiuscula:
        novaString += letra.upper()
    else:
        novaString += letra.lower()
    maiuscula = not maiuscula
print(novaString)

print('Exercício String 04')
palavra = input('Digite uma palavra : ')
novaString = ""
for letra in palavra:
    novaString += letra
    novaString += ' '
print(novaString)

print('Exercício String 05')
def substitui(texto):
    novoTexto = texto
    novoTexto = novoTexto.replace('a', '4')
    novoTexto = novoTexto.replace('e', '3')
    novoTexto = novoTexto.replace('I', '1')
    novoTexto = novoTexto.replace('t', '7')
    return novoTexto

palavra = input('Digite uma palavra : ')
novaString = substitui(palavra)
print(novaString)

print('Exercício String 06')
def inverte(texto):
    lista = list(texto)
    lista.reverse()
    novoTexto = "".join(lista)
    return novoTexto

palavra = input('Digite uma palavra : ')
novaString = inverte(palavra)
print(novaString)

print('Exercício String 07')
def inverte(texto):
    lista = list(texto)
    lista.reverse()
    novoTexto = "".join(lista)
    return novoTexto

def ehPolindroma(texto):
    if texto == inverte(texto):
        return True
    else:
        return False
palavra = input('Digite uma palavra : ')
if ehPolindroma(palavra):
    print(palavra, ' é polindroma')
else:
    print(palavra, ' não é polindroma')

print('Exercício String 08')
def textoInscrito(texto, palavra):
    return (palavra in texto)
palavra = input('Digite uma palavra : ')
texto = input('Digite o texto : ')
if textoInscrito(texto, palavra):
    print('A palavra ', palavra, ' está dentro do texto \n', texto)
else:
    print('A palavra ', palavra, ' não está dentro do texto \n', texto)

print('Exercício String 09')
def separaTexto(texto):
    letras = ''
    numeros = ''
    for letra in texto:
        if letra.isdigit():
            numeros += letra
        elif letra.isalpha():
            letras += letra
    print('Letras : ', letras)
    print('Números : ', numeros)

texto = input('Digite o texto : ')
separaTexto(texto)

print('Exercício String 10')
def infoTexto1(texto, letra):
    print('A letra ', letra, ' aparece ', texto.count(letra), ' vezes na string \n', texto)
    lista = []
    for indice in range(0, len(texto)):
        if texto[indice] == letra:
            lista.append(indice)
    print('As posições em que a letra aparece na string é : ', lista)
    distancia = lista[-1] - lista[0]
    print('A distância entre a primeira e a ultima letra é ', distancia)

texto = input('Digite o texto : ')
letra = input('Digite a letra : ')
infoTexto1(texto, letra)

print('Exercício String 11')
def criptografa(texto):
    letras = 'abcdefghijklmnopqrstuvwxyz'
    novoTexto = ''
    max = len(letras) - 1
    for letra in texto:
        if letra == ' ':
            novoTexto += letra
        else:
            novoTexto += letras[max - letras.find(letra.lower())]
    return novoTexto
texto = input('Digite o texto : ')
novoTexto = criptografa(texto)
print(texto)
print(novoTexto)
