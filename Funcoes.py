#Funções
#Para organizar o código
#Para reaproveitamento
#Primo pobre do mecroserviço

#Sintaxe
#def nome_funcao(parametros separados por virgula):
#   instruções
#   return expressões

#Primeiro passo é a definição da função
#Segundo passo é o uso

#Primeiro passo
def olaMundo ():
    print('Olá Mundo')

#Segundo passo
olaMundo()

#Função com parametros
#Definimos o parametro apenas dizendo seu nome
#Não precisamos definir o tipo do parametro
def soma (p1, p2):
    total = p1 + p2
    print(total)

print('O total é:', end=' ')
soma(5,6)

print('\nFunção com parametro e uso nomeado')
def subtracao (p1, p2):
    total = p1 - p2
    print(total)
print('O total é:', end=' ')
subtracao(p2=8, p1=5)

#Escopo
#No python e em qualquer linguagem há uma discussao sobre escopo
#O escopo é a VISIBILIDADE da variavel
#Existe variaveis de ESCOPO GLOBAL e variaveis e ESCOPO LOCAL
#No escopo GLOBAL as variaveis são definidas no programa principal
clima = 'inverno'
def mostrarClima ():
#Percebemos que mesmo DENTRO DA FUNÇÃO conseguimos accesar o valor da variavel clima
    print(f'O clima de hoje é de {clima}')

mostrarClima()
#A unica regra é que variavel NÃO PODE estar definida depois da função

#E se nós tivessemos um variavel que fosse definida dentro da função?
#Ou seja ESCOPO LOCAL
#Será que conseguiriamos ver o valor dela no programa principal

def mostrarTemperatura():
    temperatura = 13
    print(f'A temperatura hoje é de {temperatura} graus')

mostrarTemperatura()

print('\nRetorno da Função')

def soma2(p1, p2):
    total = p1 + p2
    return total

#O def permite que usemos direto em otras funções
n1 = 8
n2 = 9
print(f'A soma de {n1} e {n2} é {soma2(n1, n2)}')

def saudacao(nome):
    return 'Bom dia ' + nome + '!'
print(saudacao(input('Informe seu nome: ')))