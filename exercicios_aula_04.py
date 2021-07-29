print('Exercício 1')
def dobro(numero):
    print(numero*2)

dobro(2)

print('Exercício 2')
def circunferencia(raio):
    return 2*3.1415*raio

print(circunferencia(2))

print('Exercício 3')
def soma(numero1, numero2):
    return(numero1 + numero2)
def subtracao(numero1, numero2):
    return(numero1 - numero2)
def multiplicacao(numero1, numero2):
    return(numero1 * numero2)
def divisao(numero1, numero2):
    return(numero1 / numero2)

print(soma(3, 5))
print(subtracao(8,2))
print(multiplicacao(2,5))
print(divisao(20,4))

print('Exercício 4')
def ola(nome):
    print(f"olá, {nome}")

ola('Paulo')

print('Exercício 5')
def ola2(nome, hora):
    if hora < 12:
        print(f"Bom dia, {nome}")
    elif hora < 18:
        print(f"Boa Tarde, {nome}")
    else:
        print(f"Boa noite, {nome}")

ola2('Paulo', 10)
ola2('Paulo', 15)
ola2('Paulo', 20)

print('Exercício 6')
def par(numero):
    return numero % 2 == 0

print(par(6))

print('Exercício 7')
def maior():
    import random

    maior = 0
    for indice in range(0, 10):
        numero = random.randrange(0, 101)
        if numero > maior:
            maior = numero
    return maior

print(maior())

print('Exercício 8')
def media(qtd):
    import random

    soma = 0
    for indice in range(0, qtd + 1):
        soma += random.randrange(0, 101)
    return soma / qtd

print(media(5))

print('Exercício 9')
def caixaAlta(lista):
    for indice in range(0, len(lista)):
        lista[indice] = lista[indice].upper()
    return lista

print(caixaAlta(['o', 'rato', 'roeu', 'a', 'roupa']))

print('Exercício 10')
def somaLista(lista1, lista2):
    lista3 = []
    for indice in range(0, len(lista1)):
        lista3.append(lista1[indice] + lista2[indice])
    return lista3

print(somaLista([1, 4, 3], [3, 5, 1]))

print('Exercício 11')
def produtoLista(lista1, lista2):
    lista3 = []
    for indice in range(0, len(lista1)):
        lista3.append(lista1[indice] * lista2[indice])
    return lista3

print(produtoLista([1, 4, 3], [3, 5, 1]))

print('Exercício 12')
def produtoLista2(numero, lista):
    for indice in range(0, len(lista)):
        lista[indice] *= numero
    return lista

print(produtoLista2(5, [3, 5, 1]))

print('Exercício 13')
def somaLista2(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

print(somaLista2([3, 5, 1]))

print('Exercício 14')
def mediaLista2(lista):
    return sum(lista) / len(lista)

print(mediaLista2([3, 5, 1]))

print('Desafio 1')
def fatorial(numero):
    fat = 1
    for indice in range(1, numero + 1):
        fat *= indice
    return fat

print(fatorial(4))

print('Desafio 2')
def fatorial2(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial2(numero - 1)

print(fatorial2(5))

print('Desafio 3')
def fibonacci(numero):
    if numero == 1 or numero == 2:
        return 1
    else:
        indice = 2
        lista = [1, 1]
        while indice < numero:
            lista.append(lista[indice-1] + lista[indice-2])
            indice += 1
        return lista[numero-1]

print(fibonacci(500))

print('Desafio 4')
def validar(valor, tipo):
    valido = False
    if tipo == 'idade':
        if valor > 0 and valor <= 150:
            valido = True
    elif tipo == 'salario':
        if valor > 0:
            valido = True
    elif tipo == 'sexo':
        if valor == 'M' or valor == 'F' or valor == 'Outro':
            valido = True
    else:
        valido = False
    return valido

print(validar('a', 'sexo'))

print('Desafio 5')
def criaBaralho():
    baralho = []
    nipe = ['Ouros', 'Espadas', 'Copas', 'Paus']
    for indiceN in range(0, len(nipe)):
        baralho.append(['A' + ' de ' + nipe[indiceN], 1])
        for carta in range(2, 11):
            baralho.append([str(carta) + ' de ' + nipe[indiceN], carta])
        baralho.append(['J' + ' de ' + nipe[indiceN], 10])
        baralho.append(['Q' + ' de ' + nipe[indiceN], 10])
        baralho.append(['K' + ' de ' + nipe[indiceN], 10])
    return baralho

def sortear(baralho):
    import random
    if len(baralho) == 0:
        baralho = criaBaralho()
    indice = random.randrange(0, len(baralho))
    ponto = baralho[indice][1]
    carta = baralho[indice][0]
    baralho.pop(indice)
    return [baralho, ponto, carta]

def verifica(jogadores):
    maiorponto = 0
    for indice in range(0, len(jogadores)):
        print(jogadores[indice])
        if jogadores[indice][2] <= 21 and jogadores[indice][2] > maiorponto:
            maiores = []
            maiores.append(jogadores[indice][0])
            maiorponto = jogadores[indice][2]
        elif jogadores[indice][2] <= 21 and jogadores[indice][2] == maiorponto:
            maiores.append(jogadores[indice][0])
    if len(maiores) == 0:
        print('A banca venceu !!!')
    elif len(maiores) == 1:
        print('O vencedor foi o ' + maiores[0] + ' com ' + str(maiorponto) + ' pontos')
    else:
        print('Os vencedores foram : ')
        for indice in range(0, len(maiores)):
            print(maiores[indice] + ' com ' + str(maiorponto) + ' pontos')

def jogar21():
    jogadores = []
    qtd = int(input('Quantos Jogadores ? '))
    for indice in range(0, qtd):
        jogador = []
        nome = input('Qual o seu nome jogador N. ' + str(indice + 1) + ' ? ')
        jogador.append(nome)
#        jogador.append('Jogador N. ' + str(indice + 1))
        jogador.append([])
        jogador.append(0)
        jogador.append(True)
        jogadores.append(jogador)
    baralho = criaBaralho()
    for indice in range(0, qtd):
        while jogadores[indice][3] and jogadores[indice][2] <= 21:
            print('Jogador ' + jogadores[indice][0])
            print('Você tem ' + str(jogadores[indice][2]) + ' pontos')
            print('Sua cartas são : ')
            print(jogadores[indice][1])
            opcao = input('Você quer mais uma carta (s/n) ? ')
            if opcao == 's':
                sorteado = sortear(baralho)
                baralho = sorteado[0]
                jogadores[indice][2] += sorteado[1]
                print('Sua nova carta é ' + sorteado[2])
                jogadores[indice][1].append(sorteado[2])
                if jogadores[indice][2] > 21:
                    print('Você ultrapassou 21 pontos')
                    jogadores[indice][3] = False
            else:
                jogadores[indice][3] = False
    verifica(jogadores)

jogar21()

print('Desafio 6')
def procuraCliente(clientes):
    cpf = input('Qual o CPF pra procurar ? ')
    achou = False
    if len(clientes) > 0:
        for cliente in clientes:
            if cliente[1] == cpf:
                achou = True
                return cliente
    if not achou:
        print('Não encontrado')

def novoCliente():
    nome = input('Nome do cliente : ')
    cpf = input('CPF do Cliente : ')
    email = input('E-Mail do Cliente : ')
    return [nome, cpf, email]
def listarClientes(clientes):
    print('Nome \tCPF \tE-Mail ')
    print('----------------------------------')
    for indice in range(0, len(clientes)):
        print(clientes[indice][0] + '\t' + clientes[indice][1] + '\t' + clientes[indice][2])

clientes = []
opcao = 9
while opcao != 0:
    print('1 - Novo Cliente')
    print('2 - Procurar CPF')
    print('3 - Listar Clientes Cadastrados')
    print('0 - Fim')
    opcao = int(input('Qual a sua opção ? '))
    if opcao == 0:
        print('Obrigado por utilizar nosso sistema !!!')
    elif opcao == 1:
        clientes.append(novoCliente())
    elif opcao == 2:
        cliente = procuraCliente(clientes)
        print(cliente)
    elif opcao == 3:
        listarClientes(clientes)
    else:
        print('Opção inválida')

print('Exercícios Arquivo 01')
arquivo = open('alunos.csv', 'r')
for linha in arquivo:
    print(linha.strip('\n'))
arquivo.close()

import csv
with open('alunos.csv', encoding='utf-8') as arquivo:
  for linha in csv.reader(arquivo, delimiter=','):
    print(linha)
arquivo.close()

print('Exercícios Arquivo 02')
import csv
arquivoNovo = open('alunos_copia.csv', 'w')

with open('alunos.csv', encoding='utf-8') as arquivo:
    for linha in csv.reader(arquivo, delimiter=','):
        print(linha)
        separador = ','
        arquivoNovo.write(separador.join(linha) + '\n')
arquivo.close()
arquivoNovo.close()

print('Exercícios Arquivo 03')
import csv
with open('alunos.csv', encoding='utf-8') as arquivo:
    for linha in csv.reader(arquivo, delimiter=','):
        print(linha[1])
arquivo.close()

print('Exercícios Arquivo 04')
import csv
arquivoMedia = open('alunos_media.csv', 'w')
reader = True
with open('alunos.csv', encoding='utf-8') as arquivo:
    for linha in csv.reader(arquivo, delimiter=','):
        if reader:
            linha.append('Media')
            reader = False
        else:
            media = str((float(linha[3]) + float(linha[4]) + float(linha[5]) + float(linha[6])) / 4)
            linha.append(media)
        print(linha)
        separador = ','
        arquivoMedia.write(separador.join(linha) + '\n')
arquivo.close()
arquivoMedia.close()

print('Exercícios Arquivo 05')

import csv
reader = True
with open('alunos.csv', encoding='utf-8') as arquivo:
    for linha in csv.reader(arquivo, delimiter=','):
        if reader:
            linha.append('Media')
            reader = False
        else:
            media = str((float(linha[3]) + float(linha[4]) + float(linha[5]) + float(linha[6])) / 4)
            linha.append(media)
        print(linha[1] + ' : ' + linha[7])
arquivo.close()

print('Exercícios Arquivo 06')
import csv
arquivoMedia = open('media.csv', 'w')
reader = True

with open('alunos.csv', encoding='utf-8') as arquivo:
    for linha in csv.reader(arquivo, delimiter=','):
        linhaMedia = []
        if reader:
            linhaMedia.append(linha[0])
            linhaMedia.append('Media')
            reader = False
        else:
            media = str((float(linha[3]) + float(linha[4]) + float(linha[5]) + float(linha[6])) / 4)
            linhaMedia.append(linha[0])
            linhaMedia.append(media)
        print(linhaMedia)
        separador = ','
        arquivoMedia.write(separador.join(linhaMedia) + '\n')
arquivo.close()
arquivoMedia.close()

