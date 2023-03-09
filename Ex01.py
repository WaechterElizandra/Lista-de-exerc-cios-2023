#Salve as informações dos funcionários em uma lista, não permitindo que sejam
#informados turnos e categorias inexistentes e não aceitar valores vazios e/ou nulos.

#coletando informações
for c in range (5):
    nome = str(input('Informe o nome'))
    horas = float(input('Informe as horas trabalhadas: '))
    print('**'*20,'INFORME APENAS NÚMEROS', '**'*20)
    turno = int(input('Informe o turno de trabalho: 1(Matutino) 2(Vespertino) 3(Noturno)'))
    categoria = int(input('Informe a categoria: 1(Gerente) 2(Operário)'))

print(nome)
print(horas)
print(turno)
print(categoria)