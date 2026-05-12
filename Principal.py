from faker import Faker
import Funcoes
fake = Faker('pt-BR')

nome = fake.name()
print(Funcoes.saudacao(nome))
#print(nome)
#print(saudacao(input('Informe seu nome: ')))