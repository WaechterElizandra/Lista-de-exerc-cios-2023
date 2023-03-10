# criando as listas
nomes = []
horas_tarbalhadas = []
periodos = []
categorias = []

#coletando informações e armazenando dados nas listas
for c in range (2):
    nome = str(input('Informe o nome'))
    nomes.append(nome)
    horas = float(input('Informe as horas trabalhadas: '))
    horas_tarbalhadas.append(horas)
    turno = int(input('Informe o turno de trabalho: 1(Matutino) 2(Vespertino) 3(Noturno)'))
    periodos.append(turno)
    categoria = int(input('Informe a categoria: 1(Gerente) 2(Operário)'))
    categorias.append(categoria)

# Função para calcular ovalor da hora trabalhada

def calcular_valor_horas_trabalhadas(turno, horas):
    valor_hora = 0
    if turno == 3 and categoria == 1:
        valor_hora = 10/100 * 1300
    elif turno == 1 or turno == 2 and categoria == 1:
        valor_hora = 15/100 * 1300
    elif turno == 3 and categoria == 2:
        valor_hora = 9/100 * 1300
    elif turno == 1 or turno == 2 and categoria == 2:
        valor_hora = 14/100 * 1300
    else: 
        print('Turno ou categoria inválido')
    valor_total = valor_hora * horas
    return valor_total

#calculando e mostrando o salário de cada funcionário
salario = calcular_valor_horas_trabalhadas() * horas

# Apresentando resultados
print('Olá {}, você trabalhou {} horas'.format(nome, horas))
print('Seu salário é de {}'.format(salario))