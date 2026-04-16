matrix = []

n = int(input("Digite o numero de linhas da matriz: "))
for i in range(n):
    nome = input(f"Digite o nome do aluno{i+1}: ")
    idade = int(input(f"Digite a idade do aluno{i+1}: "))
    matrix.append([nome, idade])

    matrix.sort(key=lambda p: p[1])
    print(matrix[0][0])

    
