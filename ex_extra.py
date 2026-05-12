from datetime import datetime
horaAtual = datetime.now().hour
#horaAtual = 13
def saudacao():

    if 5 <= horaAtual < 12:
        print('Bom Dia!')
    elif 12 <= horaAtual < 18:
        print('Boa Tarde!')
    else:
        print('Boa Noite!')
print(saudacao())