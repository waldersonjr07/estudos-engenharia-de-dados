v1 = int(input('Insira o primeiro valor '))
v2 = int(input('Insira o segundo valor '))
s = v1+v2

print(f'a soma é: {v1}+{v2}={s}') #maneira mais recente de usar um print

n = input('Digite algo: ')
print(n.isalpha()) #isalpha indêntifica se é alfabético com tipo booleano (true or false)

w = input('Digite um número: ')
print(w.isnumeric())  #isnum indêntifica se é número com tipo booleano (true or false)

x= input('Digite algo: ')
print(x.isalnum()) #isalnum é a junção de alpha e numeric

#existem vários outros tipos de 'is' além desse