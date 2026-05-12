titulo = 'Média das provas'
print(f'{titulo:^30}')

def funcaoMedia (n1, n2):
    media = (n1 + n2)/2
    return media

nota1 = int(input('Informe a primeira nota: '))
nota2 = int(input('Informe a segunda nota: '))
mediaGeral = funcaoMedia(nota1, nota2)
if mediaGeral >= 6:
    print(f'sua média é {mediaGeral}, APROVADO')
else:
    print(f'Sua média é {mediaGeral}, REPORVADO')



