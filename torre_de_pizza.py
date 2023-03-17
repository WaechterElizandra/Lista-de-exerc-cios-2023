import pandas as pd
moradores = []

while True:
    elevador = input("Qual elevador você utiliza com mais frequência? (A, B ou C): ").upper()
    periodo = input("Em qual período você costuma utilizar o elevador? (M = Matutino, V = Vespertino, N = Noturno): ").upper()

    if elevador not in ["A", "B", "C"] or periodo not in ["M", "V", "N"]:
        print("Valores inválidos. Tente novamente.")
        continue

    morador = {"elevador": elevador, "periodo": periodo}
    moradores.append(morador)

    continuar = input("Deseja continuar coletando informações? (S/N): ").upper()
    if continuar == "N":
        break

# Transformando a lista DataFrame
df = pd.DataFrame(moradores)

# Contagem de ocorrências de cada elevador e período
elevador_periodo_counts = df.groupby(["elevador", "periodo"]).size() #groupby agrupar os dados para permitir execução das operações para cada grupo criado.

# Encontrando o elevador mais utilizado e em qual período se concentra o maior fluxo
elevador_mais_utilizado = elevador_periodo_counts.idxmax()#Índice de retorno da primeira ocorrência do máximo sobre o eixo solicitado.
print(f"O elevador mais utilizado é o {elevador_mais_utilizado[0]} no período {elevador_mais_utilizado[1]}.")

#período mais utilizado de todos
periodo_mais_utilizado = df["periodo"].value_counts().idxmax()
print(f"O período mais utilizado é o {periodo_mais_utilizado}.")

# Calculando a diferença porcentual entre o mais usado e o menos usado
periodo_counts = df["periodo"].value_counts()
diferenca_percentual = (periodo_counts.max() - periodo_counts.min()) / periodo_counts.min() * 100
print(f"A diferença porcentual entre o mais usado e o menos usado é de {diferenca_percentual:.2f}%.")

