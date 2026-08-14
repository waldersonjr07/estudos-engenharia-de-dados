# Log de estudos 

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