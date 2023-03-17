# Definição de valores das horas
salario_minimo = 1320.00
valor_hora_gerente_noturno = salario_minimo * 0.1
valor_hora_gerente_matutino_vespertino = salario_minimo * 0.15
valor_hora_operario_noturno = salario_minimo * 0.09
valor_hora_operario_matutino_vespertino = salario_minimo * 0.14

# Definição da lista de funcionários
funcionarios = []

# Loop para coletar informações dos funcionários
while True:
    nome = input("Digite o nome do funcionário (ou digite 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break

    while True:
        horas_trabalhadas = input("Digite a quantidade de horas trabalhadas no mês: ")
        if horas_trabalhadas.isdigit():
            horas_trabalhadas = int(horas_trabalhadas)
            break
        else:
            print("Valor inválido. Digite um valor inteiro.")

    while True:
        turno = input("Digite o turno de trabalho (M = Matutino, V = Vespertino, N = Noturno): ")
        if turno.upper() in ["M", "V", "N"]:
            turno = turno.upper()
            break
        else:
            print("Turno inválido. Digite M, V ou N.")

    while True:
        categoria = input("Digite a categoria do funcionário (G = Gerente, O = Operário): ")
        if categoria.upper() in ["G", "O"]:
            categoria = categoria.upper()
            break
        else:
            print("Categoria inválida. Digite G ou O.")

    # Cálculo do valor da hora trabalhada
    if categoria == "G":
        if turno == "N":
            valor_hora = valor_hora_gerente_noturno
        else:
            valor_hora = valor_hora_gerente_matutino_vespertino
    else:
        if turno == "N":
            valor_hora = valor_hora_operario_noturno
        else:
            valor_hora = valor_hora_operario_matutino_vespertino

    # Cálculo do salário do funcionário
    salario = valor_hora * horas_trabalhadas / 30

    # Adicionando informações do funcionário à lista
    funcionario = {"nome": nome, "horas_trabalhadas": horas_trabalhadas, "turno": turno, "categoria": categoria, "valor_hora": valor_hora, "salario": salario}
    funcionarios.append(funcionario)

# Impressão dos salários dos funcionários
for funcionario in funcionarios:
    print(f"Nome: {funcionario['nome'].upper()} - Salário: R$ {funcionario['salario']:.2f}")

