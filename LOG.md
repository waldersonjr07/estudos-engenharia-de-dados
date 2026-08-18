# Log de estudos 

### 13/08/2026 — Dia 3 - Somente SQL

### SQL — o que estudei
Primeiro dia de SQL, sem conhecimento prévio. SQLZoo.
Fiz os dois primeiros quizzes inteiros sozinho, sem ajuda e fluiu até que bem.
No terceiro precisei de ajuda na maioria das questões.

Conteúdo: SELECT, FROM, WHERE, operadores de comparação,
AND / OR / NOT, ROUND, LENGTH.

**1. Cálculo dentro do SELECT**
Tentei colocar a expressão GDP/population fora do SELECT (usei LIKE
por engano). Qualquer expressão: divisão, soma, função vai no
SELECT, na posição da coluna.
Regra: SELECT decide O QUE aparece; WHERE decide QUAIS LINHAS aparecem.

**2. Texto precisa de aspas simples**
`WHERE continent = South America` dá erro de sintaxe: sem aspas o
banco tenta ler South como nome de coluna.
Regra: texto entre aspas simples, número sem nada.
Aspas simples e duplas não são intercambiáveis como em Python
simples delimitam texto, duplas são para nomes de coluna.

**3. Precedência de AND e OR (questão do XOR)**
`a OR b AND c` é lido como `a OR (b AND c)` — AND tem precedência
sobre OR, igual multiplicação sobre soma.
Escrevi a lógica certa mas sem parênteses no OR, e o resultado veio
errado sem dar nenhum erro. Esse é o pior tipo de bug: a query roda,
devolve tabela bonita e os números estão errados.
Regra: misturou AND com OR, use parênteses explícitos sempre.

**4. Função envelopa a coluna, não é uma linha solta**
Tentei escrever ROUND numa linha separada, depois do WHERE.
Função vai dentro do SELECT, envolvendo o cálculo:
`ROUND(population/1000000, 2)`. Tudo que ela recebe fica dentro do
mesmo par de parênteses, igual ao print() do Python.

**5. ROUND com segundo parâmetro negativo**
`ROUND(valor, 2)` → duas casas decimais.
`ROUND(valor, -3)` → arredonda para o milhar.
Positivo vai para a direita da vírgula, negativo para a esquerda.
Descobri sozinho testando.

**6. Nome de coluna x valor da célula (o que mais travou)**
Escrevi LENGTH('Brasil') e LENGTH(Brasil) tentando resolver a questão
das capitais. Nenhum dos dois funciona:
- 'Brasil' entre aspas é um texto fixo — conta 6 para toda linha
- Brasil sem aspas não existe, porque não é coluna, é conteúdo de célula
As colunas da tabela world são name, continent, capital, population,
area, gdp. LENGTH(name) faz o banco percorrer a tabela e contar as
letras de cada linha automaticamente. Não preciso citar nenhum país.

**7. Arrastar pedaço da query anterior**
Duas vezes deixei sobra da tentativa anterior (linha antiga não
apagada, e o /population vindo do exercício de GDP per capita).
Hábito a adotar: corrigir apagando e reescrevendo, não empilhando
linha nova embaixo. E antes de enviar, ler cada coluna do SELECT e
perguntar "o enunciado pediu isso?".

### Para revisar
- Refazer do zero, sem consultar, as questões 8, 9 e 13
- LIKE com % e _ (usei sem entender direito)
- Diferença entre filtrar no WHERE e calcular no SELECT

### Observação sobre o método
Enunciado do SQLZoo dá exemplo para explicar o conceito (Grécia/Atenas),
não para ser copiado na query. Perdi tempo tentando reproduzir o
exemplo em vez de resolver o caso geral.

## 13/082026 — Dia 2

Devido a agenda apertada e com uma dificuldade em familiarizar com python, estudei apenas tipos primitivos por hoje.

### O que eu estudei
- Curso em vídeo, Python Mundo 1: aula 6
- Desafio de mostrar classe de uma váriavel, utilizar os comandos "is" e entender suas funcionalidades
- Desafio foi bem sucedido mas acabei demorando mais que o planejado e precisei fazer outras coisas

### Revisar amanhã
Tipos primitivos e suas funcionalidades.


## 12/08/2026 — Dia 1, parte 2

> Uso o Claude como ferramenta de estudo: pra tirar dúvida, destravar
> erro de ambiente e saber o que estudar em seguida. O código dos
> exercícios eu escrevo.

### O que estudei
- Curso em Vídeo, Python Mundo 1: aula 4 (primeiros comandos, input, print)
- 3 desafios da aula: 2 resolvidos sozinho, 1 com pesquisa
  (conversão de tipo, ainda não ensinada até essa altura do curso)

### Terminal e ambiente
- Mover pasta pelo terminal com move "origem" "destino"
- Abrir o VS Code direto numa pasta com code <caminho>
- Rodar script pelo terminal com python arquivo.py, em vez do botão de play
- Problema resolvido: a pasta do projeto estava dentro do OneDrive,
  o que causa conflito com o Git. Movida para C:\Users\walde\dev

### O que travou
Desafio 3 (somar dois números): a soma concatenava em vez de somar
(juntava a+b, ficando ab, ao invés de a+b=c).
Causa: input() sempre retorna str, e + entre strings junta o texto.
Solução: converter com int() antes da operação.
print(type(variavel)) mostra o tipo útil para diagnosticar.

### Para revisar
- Diferença entre int() e float() na conversão
- Fazer a conversão numa linha só: int(input('mensagem'))

## 12/08/2026 — Dia 1
Configurei o ambiente: Python, VS Code, Git e autenticação SSH com o GitHub.
Primeiro repositório criado.