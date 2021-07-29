print('Exercício 01')
tupla = tuple(range(0, 101, 2))
print(tupla)

print('Exercício 02')
tupla = tuple(range(0, 10))
print(tupla)

print('Exercício 03')
def lista(*args):
    import statistics
    media = statistics.mean(args)
    desviopadrao = statistics.stdev(args)
    maximo = max(args)
    minimo = min(args)
    return minimo, media, desviopadrao, maximo

(minimo, media, desviopadrao, maximo) = lista(1, 2, 3, 4, 5)
print(f'Mínimo = {minimo}, Máximo = {maximo}, \nmedia = {media}, Desvio Padrão = {desviopadrao}')

print('Exercício 04')
def avalia(*lista):
    saoNumericos = True
    lista2 = []
    for item in lista:
        if isinstance(item, int) or isinstance(item, float):
            lista2.append(item)
        elif isinstance(item, str):
            if item.isnumeric():
                lista2.append(int(item))
            elif item.isdecimal():
                lista2.append(float(item))
            else:
                try:
                    lista2.append(float(item))
                except ValueError:
                    saoNumericos = False
        else:
            saoNumericos = False
    if saoNumericos:
        return saoNumericos, lista2
    else:
        return saoNumericos, lista


(verifica, lista) = avalia(1, '2.5', 3, 4, 5.1, 6, '7')
if verifica:
    print('A lista é numérica, ')
    print(lista)
else:
    print('A lista não é numérica, ')
    print(lista)

print('Exercício 5')
def bascara(a, b, c):
    lista = []
    delta = b ** 2 - 4 * a * c
    x_m = -b / (2 * a)
    y_m = -delta / (4 * a)
    if delta == 0:
        lista.append((-b) / (2 * a))
    elif delta > 0:
        lista.append((-b + delta ** (1/2)) / (2 * a))
        lista.append((-b - delta ** (1 / 2)) / (2 * a))
    return delta, (x_m, y_m), lista

print(bascara(7, 3, 4))

print('Exercício 6')
meses = {'janeiro':31, 'fevereiro':28, 'março':31, 'abril':30, 'maio':31, 'junho':30, 'julho':31, 'agosto':31,
         'setembro':30, 'outubro':31, 'novembro':30, 'dezembro':31}

print('Exercício 7')
meses = {'janeiro':31, 'fevereiro':28, 'março':31, 'abril':30, 'maio':31, 'junho':30, 'julho':31, 'agosto':31,
         'setembro':30, 'outubro':31, 'novembro':30, 'dezembro':31}

for mes in meses:
    print(mes.capitalize(), ' - ', meses[mes])

print('Exercício 8')
frutas = {'Banana': 3.0, 'Cebola': 4.0, 'Maçã': 5.7, 'Abacaxi': 8.0}

print('Exercício 9')
frutas = {'Banana': 3.0, 'Cebola': 4.0, 'Maçã': 5.7, 'Abacaxi': 8.0}

print(frutas)
frutas['Maçã'] = 8.6
print(frutas)

print('Exercício 10')
def montar(nome, idade, email):
    return {'nome':nome, 'idade':idade, 'email':email}

print(montar('Paulo', 52, 'paulorsr@hotmail.com'))

print('Exercício 11')
matriz = {'Maria':{'coluna A':1, 'coluna B':5}, 'Pedro':{'coluna A':0.5, 'coluna B':3}, 'João':{'coluna A':3.2, 'coluna B':1}}

print(matriz)
print(matriz['Pedro'])
print(matriz['Pedro']['coluna B'])

print('Exercício 12')
def analiza(*lista):
    dicionario = {}
    for item in lista:
        if item in dicionario:
            dicionario[item] += 1
        else:
            dicionario[item] = 1
    return dicionario

print(analiza('maça', 'banana', 'pera', 'maça', 'abacaxi', 'pera', 'laranja', 'maça', 'limão'))

print('Exercício 13')
def inserir(dicionario):
    cpf = input('Informe o CPF : ')
    if cpf in dicionario:
        print('Esse CPF já foi cadastrado')
    else:
        nome = input('Qual o nome ? ')
        idade = input('Qual a idade ? ')
        email = input('Qual o E-mail ? ')
        dicionario[cpf] = {'nome': nome, 'idade': idade, 'email': email}
    return dicionario

def listar(dicionario):
    for pessoa in dicionario:
        linha = 'CPF : ' + pessoa + '\t'
        for item in dicionario[pessoa]:
            linha += item + ' : ' + dicionario[pessoa][item] + '\t'
        print(linha)

continua = True
dicionario = {}
while continua:
    opcao = input('Digite:\n1 - Cadastrar usuário\n2 - Listar usuários\n3 - fechar\nQual a sua opção ? ')
    if opcao == '1':
        dicionario = inserir(dicionario)
    elif opcao == '2':
        listar(dicionario)
    elif opcao == '3':
        continua = False

print('Exercício 14')
def inserir(dicionario):
    cpf = input('Informe o CPF : ')
    if cpf in dicionario:
        print('Esse CPF já foi cadastrado')
    else:
        nome = input('Qual o nome ? ')
        idade = input('Qual a idade ? ')
        email = input('Qual o E-mail ? ')
        dicionario[cpf] = {'nome': nome, 'idade': idade, 'email': email}
    return dicionario

def listar(dicionario):
    for pessoa in dicionario:
        linha = 'CPF : ' + pessoa + '\t'
        for item in dicionario[pessoa]:
            linha += item + ' : ' + dicionario[pessoa][item] + '\t'
        print(linha)

def pesquisar(dicionario):
    cpf = input('Qual o CPF ? ')
    if cpf in dicionario:
        linha = ''
        for item in dicionario[cpf]:
            linha += item + ' : ' + dicionario[cpf][item] + '\t'
        print(linha)
    else:
        print('CPF não encontrado')

continua = True
dicionario = {}
while continua:
    opcao = input('Digite:\n1 - Cadastrar usuário\n2 - Listar usuários\n3 - Pesquisar CPF\n4 - fechar\nQual a sua opção ? ')
    if opcao == '1':
        dicionario = inserir(dicionario)
    elif opcao == '2':
        listar(dicionario)
    elif opcao == '3':
        pesquisar(dicionario)
    elif opcao == '4':
        continua = False

print('Exercício 15')
def analiza(texto):
    lista = texto.split(' ')
    dicionario = {}
    for item in lista:
        if item in dicionario:
            dicionario[item] += 1
        else:
            dicionario[item] = 1
    return dicionario

print(analiza('maça banana pera maça abacaxi pera laranja maça limão'))
