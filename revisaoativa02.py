nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
endereco = input('Qual seu bairro? ')

print(f'Olá, {nome}! Você tem {idade} anos e mora em {endereco}.')


print('\nAgora vamos somar a sua idade com a de sua mãe/pai, ok?')
idade1 = int(input('Qual a idade do seu pai/mãe? '))
idade2 = int(input('Qual sua idade? '))
print('A soma da idade de vcs é', idade1+idade2)