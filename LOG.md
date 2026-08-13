# Log de estudos 

## 12/08/2026 — Dia 1, parte 2

> Uso o Claude como ferramenta de estudo: pra tirar dúvida, destravar
> erro de ambiente e saber o que estudar em seguida. O código dos
> exercícios eu escrevo.

### O que estudei
- Curso em Vídeo, Python Mundo 1: aula 4 (primeiros comandos,
  tipos primitivos, input, print e operadores)
- 3 desafios da aula: 2 resolvidos sozinho, 1 com pesquisa
  (conversão de tipo, ainda não ensinada até essa altura do curso)

### Terminal e ambiente
- Mover pasta pelo terminal com `move "origem" "destino"`
- Abrir o VS Code direto numa pasta com `code <caminho>`
- Rodar script pelo terminal com `python arquivo.py`, em vez do botão de play
- Problema resolvido: a pasta do projeto estava dentro do OneDrive,
  o que causa conflito com o Git. Movida para C:\Users\walde\dev

### O que travou
Desafio 3 (somar dois números): a soma concatenava em vez de somar
(juntava a+b, ficando ab, ao invés de a+b=c).
Causa: `input()` sempre retorna `str`, e `+` entre strings junta o texto.
Solução: converter com `int()` antes da operação.
`print(type(variavel))` mostra o tipo — útil para diagnosticar.

### Para revisar
- Diferença entre `int()` e `float()` na conversão
- Operadores `//`, `%` e `**`
- Fazer a conversão numa linha só: `int(input('mensagem'))`

## 12/08/2026 — Dia 1
Configurei o ambiente: Python, VS Code, Git e autenticação SSH com o GitHub.
Primeiro repositório criado.