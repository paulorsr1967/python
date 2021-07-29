print('Exercício 01')
#Crie uma classe Bola cujos atributos são cor e raio. Crie um método que imprime a cor da bola.
# Crie um método para calcular a área dessa bola. Crie um método para calcular o volume da bola.
# Crie um objeto dessa classe e calcule a área e o volume, imprimindo ambos em seguida.
#Obs.:
#Área da esfera = 4*3.14*r*r;
#Volume da esfera = 4*3.14*r*r*r/3

class Bola:

    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def imprimirCor(self):
        print(self.cor)

    def calculaArea(self):
        return 4 * 3.14 * self.raio * self.raio

    def calculaVolume(self):
        return 4 * 3.14 * self.raio * self.raio * self.raio / 3

bola = Bola('Azul', 1)
bola.imprimirCor()
print(bola.calculaArea())
print(bola.calculaVolume())

print('Exercício 02')
class Retangulo:

    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def calculaArea(self):
        return self.lado_a * self.lado_b

retangulo = Retangulo(2, 1)
print(retangulo.calculaArea())

print('Exercício 03')

class Funcionario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.ht = {}
        self.salario_hora = {}

    def gravaHoraTrabalhada(self, mes, ht):
        self.ht[mes] = ht

    def calculaSalario(self, mes, valor_hora):
        self.salario_hora[mes] = valor_hora

    def mostraSalario(self, mes):
        return self.ht[mes] * self.salario_hora[mes]

fun1 = Funcionario('Paulo', 'paulorsr@hotmail.com')
fun1.gravaHoraTrabalhada('Julho', 40)
fun1.calculaSalario('Julho', 40)
print(fun1.mostraSalario('Julho'))

print('Exercício 04')
#Crie uma classe Televisor cujos atributos são:
#a. fabricante;
#b. modelo;
#c. canal atual;
#d. lista de canais; e
#e. volume.
#Faça métodos para aumentar/diminuir volume, trocar o canal e sintonizar um novo canal,
# que adiciona um novo canal à lista de canais (somente se esse canal não estiver nessa lista).
# No atributo lista de canais, devem estar armazenados todos os canais já sintonizados dessa TV.
#Obs.: O volume não pode ser menor que zero e maior que cem; só se pode trocar para um canal que já esteja na lista de canais.

class Televisor:

    def __init__(self, fabricante, modelo, canal_atual, lista_de_canais, volume):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = canal_atual
        self.lista_de_canais = lista_de_canais
        self.volume = volume
        if canal_atual not in lista_de_canais:
            self.lista_de_canais.append(canal_atual)
        print('Lista de Canais : ', self.lista_de_canais)
        print('Canal Atual : ', self.canal_atual)

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        print('Volume Atual : ', self.volume)

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        print('Volume Atual : ', self.volume)

    def anteriorCanal(self):
        iCanal = self.lista_de_canais.index(self.canal_atual)
        if iCanal > 0:
            self.canal_atual = self.lista_de_canais[iCanal - 1]
        print('Canal Atual : ', self.canal_atual)

    def proximoCanal(self):
        iCanal = self.lista_de_canais.index(self.canal_atual)
        if iCanal < len(self.lista_de_canais) - 1:
            self.canal_atual = self.lista_de_canais[iCanal + 1]
        print('Canal Atual : ', self.canal_atual)

    def novoCanal(self, canal):
        self.canal_atual = canal
        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)
        print('Lista de Canais : ', self.lista_de_canais)
        print('Canal Atual : ', self.canal_atual)

tv = Televisor('Samsung', '50TV01', 'Globo', [], 50)
tv.aumentarVolume()
tv.diminuirVolume()
tv.novoCanal('Band')
tv.novoCanal('Record')
tv.anteriorCanal()
tv.anteriorCanal()
tv.proximoCanal()

print('Exercício 05')
#Crie uma classe ControleRemoto cujo atributo é televisão (isso é, recebe um objeto da classe do exercício 4).
# Crie métodos para aumentar/diminuir volume, trocar o canal e sintonizar um novo canal,
# que adiciona um novo canal à lista de canais (somente se esse canal não estiver nessa lista).

class Televisor:

    def __init__(self, fabricante, modelo, canal_atual, lista_de_canais, volume):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = canal_atual
        self.lista_de_canais = lista_de_canais
        self.volume = volume
        if canal_atual not in lista_de_canais:
            self.lista_de_canais.append(canal_atual)
        print('Lista de Canais : ', self.lista_de_canais)
        print('Canal Atual : ', self.canal_atual)

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        print('Volume Atual : ', self.volume)

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        print('Volume Atual : ', self.volume)

    def anteriorCanal(self):
        iCanal = self.lista_de_canais.index(self.canal_atual)
        if iCanal > 0:
            self.canal_atual = self.lista_de_canais[iCanal - 1]
        print('Lista de Canais : ', self.lista_de_canais)
        print('Canal Atual : ', self.canal_atual)

    def proximoCanal(self):
        iCanal = self.lista_de_canais.index(self.canal_atual)
        if iCanal < len(self.lista_de_canais) - 1:
            self.canal_atual = self.lista_de_canais[iCanal + 1]
        print('Lista de Canais : ', self.lista_de_canais)
        print('Canal Atual : ', self.canal_atual)

    def novoCanal(self, canal):
        self.canal_atual = canal
        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)
        print('Lista de Canais : ', self.lista_de_canais)
        print('Canal Atual : ', self.canal_atual)

class ControleRemoto:
    def __init__(self, Televisor):
        self.Televisor = Televisor

    def aumentarVolume(self):
        self.Televisor.aumentarVolume()

    def diminuirVolume(self):
        self.Televisor.diminuirVolume()

    def anteriorCanal(self):
        self.Televisor.anteriorCanal()

    def proximoCanal(self):
        self.Televisor.proximoCanal()

    def novoCanal(self, canal):
        self.Televisor.novoCanal()


tv = Televisor('Samsung', '50TV01', 'Globo', [], 50)
tv.aumentarVolume()
tv.diminuirVolume()
tv.novoCanal('Band')
tv.novoCanal('Record')
tv.anteriorCanal()
tv.anteriorCanal()
tv.proximoCanal()
cr = ControleRemoto(tv)
cr.aumentarVolume()
cr.proximoCanal()

print('Exercício 06')
#O módulo time possui a função time.sleep(x), que faz seu programa “dormir” por x segundos.
# Utilizando essa função, crie uma classe Cronômetro e faça um programa que cronometre o tempo.

from datetime import datetime
from time import sleep

class Cronometro:

    def __init__(self):
        self.inicio = 0

    def iniciar(self):
        self.inicio = datetime.now()
        print('Inicio : ', self.inicio)

    def parar(self):
        termino = datetime.now()
        print('Termino : ', termino)
        print('Tempo decorrido : ', termino - self.inicio)

cr = Cronometro()
cr.iniciar()
sleep(10)
cr.parar()

print('Exercício 07')
#Crie uma modelagem de classes para uma agenda capaz de armazenar contatos.
# Através dessa agenda é possível incluir, remover, buscar e listar contatos já cadastrados.

class Agenda:

    def __init__(self):
        self.contatos = []

    def incluir(self, contato):
        if contato not in self.contatos:
            self.contatos.append(contato)
        print('Contatos : ', self.contatos)

    def remover(self, pessoa):
        self.contatos.remove(pessoa)
        print('Contatos : ', self.contatos)

    def listar(self):
        for contato in self.contatos:
            print('Nome : ', contato)

    def buscar(self):
        for contato in self.contatos:
            print('Nome : ', contato)


ag = Agenda()
ag.incluir('Paulo')
ag.incluir('Roberto')
ag.incluir('de')
ag.incluir('Sá')
ag.remover('de')
ag.incluir('Rodrigues')
ag.incluir('Paulo')
ag.listar()

print('Exercício 08')
#Crie uma classe Cliente cujos atributos são nome, idade e e-mail. Construa um método que imprima as informações
# tal como abaixo:
#Nome: Fulano de Tal
#Idade: 40
#E-mail: fulano@mail.com

class Cliente:

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def imprimir(self):
        print('Nome:', self.nome)
        print('Idade:', self.idade)
        print('E-mail:', self.email)

print('Exercício 09')
#Com base no exercício anterior, crie um sistema de cadastro e a classe Cliente.
# Seu programa deve perguntar se o usuário quer cadastrar um novo cliente, alterar um cadastro ou sair.
#Dica: Você pode fazer esse exercício criando uma classe Sistema, que irá controlar o sistema de cadastros.
# Essa classe deve ter o atributo cadastro e os métodos para imprimir os cadastrados, cadastrar um novo cliente,
# alterar um cadastro ou sair.

class Cliente:

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def imprimir(self):
        print('Nome:', self.nome)
        print('Idade:', self.idade)
        print('E-mail:', self.email)

print('Exercício 10')
#Crie uma classe ContaCorrente com os atributos cliente (que deve ser um objeto da classe Cliente) e saldo.
# Crie métodos para depósito, saque e transferência.
# Os métodos de saque e transferência devem verificar se é possível realizar a transação.

class Cliente:

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def imprimir(self):
        print('Nome:', self.nome)
        print('Idade:', self.idade)
        print('E-mail:', self.email)

class ContaCorrente:

    def __init__(self, Cliente, saldo):
        self.Cliente = Cliente
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print('Saldo Insuficiente ')
            return False

    def transferencia(self, Cliente, valor):
        if self.saque(valor):
            Cliente.deposito(valor)

cli1 = Cliente('Paulo', 53, 'paulorsr@hotmail.com')
cc1 = ContaCorrente(cli1, 0)
print('Nome:', cc1.Cliente.nome)
print('Saldo:', cc1.saldo)
cc1.deposito(100.00)
print('Saldo:', cc1.saldo)
cc1.deposito(50.00)
print('Saldo:', cc1.saldo)
cc1.saque(170.00)
print('Saldo:', cc1.saldo)
cc1.saque(20.00)
print('Saldo:', cc1.saldo)
cli2 = Cliente('Roberto', 53, 'paulorsr@hotmail.com')
cc2 = ContaCorrente(cli2, 0)
print('Nome:', cc2.Cliente.nome)
print('Saldo:', cc2.saldo)
cc1.transferencia(cc2, 150)
print('Nome:', cc1.Cliente.nome)
print('Saldo:', cc1.saldo)
print('Nome:', cc2.Cliente.nome)
print('Saldo:', cc2.saldo)
cc1.transferencia(cc2, 100)
print('Nome:', cc1.Cliente.nome)
print('Saldo:', cc1.saldo)
print('Nome:', cc2.Cliente.nome)
print('Saldo:', cc2.saldo)

print('Exercício 11')
#Crie uma classe Fração cujos atributos são numerador (número de cima) e denominador (número de baixo).
#Implemente os métodos de adição, subtração, multiplicação, divisão que retornam objetos do tipo Fração.
#Implemente também o método _ repr _.
#Implemente métodos para comparação: igualdade (==) e desigualdades (!=, <=, >=, < e >).

class Fracao:

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        self.valor = numerador / denominador

    def __repr__(self):
        rep = 'Fração(' + str(self.numerador) + ' / ' + str(self.denominador) + ')'
        return rep

    def compara(self, outra):
        if self.valor == outra.valor:
            print('As frações são iguais')
        elif self.valor > outra.valor:
            print('Minha fração é maior')
        else:
            print('A outra fração é maior')

    def multiplica(self, outra):
        return Fracao(self.numerador * outra.numerador, self.denominador * outra.denominador)

    def divide(self, outra):
        return Fracao(self.numerador * outra.denominador, self.denominador * outra.numerador)

    def soma(self, outra):
        return Fracao(self.numerador * outra.denominador + outra.numerador * self.denominador, self.denominador * outra.denominador)

    def subtrai(self, outra):
        return Fracao(self.numerador * outra.denominador - outra.numerador * self.denominador, self.denominador * outra.denominador)

fracao1 = Fracao(1, 7)
fracao2 = Fracao(1, 9)
print(repr(fracao1))
print(fracao1.compara(fracao2))
print('Multiplica :', fracao1.multiplica(fracao2))
print('Divide :', fracao1.divide(fracao2))
print('Soma :', fracao1.soma(fracao2))
print('Subtrai :', fracao1.subtrai(fracao2))

print('Exercício 12')
#Crie uma classe Data cujos atributos são dia, mês e ano.
# Implemente métodos _ repr _ e para comparação: igualdade (==) e desigualdades (!=, <=, >=, < e >).

import datetime

class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.diamesano = datetime.datetime(ano, mes, dia)

    def __repr__(self):
        rep = 'Data(' + str(self.dia) + ' / ' + str(self.mes) + ' / ' + str(self.ano) + ')'
        return rep

    def compara(self, outra):
        if self.diamesano == outra.diamesano:
            print('As datas são iguais')
        elif self.diamesano > outra.diamesano:
            print('Minha data é maior')
        else:
            print('A outra data é maior')

data1 = Data(19, 7, 2021)
data2 = Data(19, 7, 2020)
print(repr(data1))
print(data1.compara(data2))

print('Exercício 13')
#Nos exercícios 1, 2, 3, 4 e 6, implemente o método _ repr _ para exibir as informações desejadas de cada uma das classes.

class Bola:

    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def __repr__(self):
        rep = 'Bola(' + self.cor + ', ' + str(self.raio) + ')'
        return rep

class Retangulo:

    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def __repr__(self):
        rep = 'Retangulo(' + str(self.lado_a) + ', ' + str(self.lado_b) + ')'
        return rep

class Funcionario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.ht = {}
        self.salario_hora = {}

    def __repr__(self):
        rep = 'Funcionário(' + self.nome + ', ' + self.email + ', ' + str(self.ht) + ', ' + str(self.salario_hora) + ')'
        return rep

class Televisor:

    def __init__(self, fabricante, modelo, canal_atual, lista_de_canais, volume):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = canal_atual
        self.lista_de_canais = lista_de_canais
        self.volume = volume
        if canal_atual not in lista_de_canais:
            self.lista_de_canais.append(canal_atual)

    def __repr__(self):
        rep = 'Televisor(' + self.fabricante + ', ' + self.modelo + ', ' + str(self.canal_atual) + ', ' + str(self.lista_de_canais) + ', ' + str(self.volume) + ')'
        return rep

class Cronometro:

    def __init__(self):
        self.inicio = 0

    def __repr__(self):
        rep = 'Cronometro(' + str(self.inicio) + ')'
        return rep

bola = Bola('Azul', 2)
print(repr(bola))
retangulo = Retangulo(2, 1)
print(repr(retangulo))
funcionario = Funcionario('Paulo', 'paulorsr@hotmail.com')
print(repr(funcionario))
tv = Televisor('Samsung', '50TV01', 'Globo', [], 50)
print(repr(tv))
cr = Cronometro()
print(repr(cr))

print('Exercício 14')
#Faça uma classe ContaVip que difere da ContaCorrente por ter cheque especial (novo atributo) e é
# filha da classe ContaCorrente. Você precisa implementar os métodos para saque, transferência ou depósito?

class Cliente:

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def imprimir(self):
        print('Nome:', self.nome)
        print('Idade:', self.idade)
        print('E-mail:', self.email)

class ContaCorrente:

    def __init__(self, Cliente, saldo):
        self.Cliente = Cliente
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print('Saldo Insuficiente ')
            return False

    def transferencia(self, Cliente, valor):
        if self.saque(valor):
            Cliente.deposito(valor)

class ContaVip(ContaCorrente):

    def __init__(self, Cliente, saldo, cheque_especial):
        self.cheque_especial = cheque_especial
        ContaCorrente.__init__(self, Cliente, (saldo + cheque_especial))

cli1 = Cliente('Paulo', 53, 'paulorsr@hotmail.com')
cc1 = ContaCorrente(cli1, 0)
print('Nome:', cc1.Cliente.nome)
print('Saldo:', cc1.saldo)
cc1.deposito(100.00)
print('Saldo:', cc1.saldo)
cc1.deposito(50.00)
print('Saldo:', cc1.saldo)
cc1.saque(170.00)
print('Saldo:', cc1.saldo)
cc1.saque(20.00)
print('Saldo:', cc1.saldo)
cli2 = Cliente('Roberto', 53, 'paulorsr@hotmail.com')
cc2 = ContaCorrente(cli2, 0)
print('Nome:', cc1.Cliente.nome)
print('Saldo:', cc1.saldo)
print('Nome:', cc2.Cliente.nome)
print('Saldo:', cc2.saldo)
cli3 = Cliente('Sandra', 49, 'sandra@hotmail.com')
cc3 = ContaVip(cli3, 0.0, 5000.0)
print('Nome:', cc3.Cliente.nome)
print('Saldo:', cc3.saldo)

print('Exercício 15')
#Crie uma classe Quadrado, filha da classe Retângulo do exercício 2.

class Retangulo:

    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def calculaArea(self):
        return self.lado_a * self.lado_b

class Quadrado(Retangulo):

    def __init__(self, lado):
        Retangulo.__init__(self, lado, lado)

retangulo = Retangulo(2, 1)
print(retangulo.calculaArea())

quadrado = Quadrado(2)
print(quadrado.calculaArea())
