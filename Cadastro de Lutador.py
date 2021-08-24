
def dados_lutador():
    # dados de entrada
    nome_lutador = input('Qual é o nome do lutador?')
    peso = float(input('Qual o peso do lutador?'))  # float converter para real


    # inserindo condicional:
    # if e elif para colocar os intervalos da tabela
    if peso < 65.0:
        categoria = 'Pena'

    elif peso >= 65.0 and peso < 72.0:
        categoria = 'Leve'

    elif peso >= 72.0 and peso < 79.0:
        categoria = 'Ligeiro'

    elif peso >= 79.0 and peso < 86.0:
        categoria = 'Meio-médio'

    elif peso >= 86.0 and peso < 93.0:
        categoria = 'Médio'

    elif peso >= 93.0 and peso < 100.0:
        categoria = 'Meio-pesado'

    elif peso >= 100.0:
        categoria = 'Pesado'

    # saídas:
    print('Nome fornecido: {} '.format(nome_lutador))
    print('Peso fornecido: {}'.format(peso))
    print('O lutador {} pesa {} kg e se enquadra na categoria {}.'.format(nome_lutador, peso, categoria))

# Estrutura de repetição enquanto o usuário não degitar 2 que é a forma de sair o programa continuará repetindo
while True:
    dados_lutador()
    sair = int(input('Deseja fazer uma nova consulta?\n1-Sim\n2-Não\n'))
    if sair == 2:
        print('Saindo...')
        break

