arquivo = open(r'C:\Users\ACADEMICO\Desktop\2903.txt', 'w')
alunos = []
avaliacao = []

# Depois de cada entrada, escrevê-la no artigo
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
avaliacao.append([nota1, nota2, nota3])
arquivo.write( str(avaliacao[0]))

# No final do programa, pule uma linha e feche o arquivo
arquivo.write('\n')