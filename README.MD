# Simuladores didáticos de Sistemas Operacionais

# Descrição
Simuladores didáticos de Sistemas Operacionais via terminal. Contém a implementação do Algoritmo do Banqueiro para prevenção de deadlocks e de uma estratégia de Alocação de Blocos no Disco para sistemas de arquivos.

# Algoritmo do Banqueiro
Este projeto apresenta um simulador simples do Algoritmo do Banqueiro, desenvolvido em Python para a disciplina de Sistemas Operacionais.

O objetivo do programa é verificar se um sistema está em estado seguro ou inseguro, considerando processos, recursos disponíveis, matriz de alocação e matriz de necessidade máxima.

## Sobre o algoritmo
O Algoritmo do Banqueiro é utilizado para prevenção de deadlocks. Ele analisa se a concessão de recursos para um processo mantém o sistema em uma situação segura.

Um estado é considerado seguro quando existe pelo menos uma sequência em que todos os processos conseguem finalizar sua execução.

## Tecnologias utilizadas

- Python
- Jupyter Notebook

## Como executar

1. Abra o Jupyter Notebook.
2. Execute todas as células do arquivo `algoritmo_banqueiro.ipynb`.

## Entrada utilizada no teste

### Matriz de Alocação

```python
alocado = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]
```

### Matriz Máxima

```python
maximo = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
```

### Recursos disponíveis

```python
disponivel = [3, 3, 2]
```

## Resultado esperado

```text
Estado SEGURO
Sequência segura: P1 -> P3 -> P4 -> P0 -> P2
```

## Conclusão

Este projeto demonstra o funcionamento do Algoritmo do Banqueiro de forma prática, permitindo compreender como o sistema verifica se a alocação de recursos mantém um estado seguro e evita situações de deadlock.


# Alocação de Blocos no Disco - Indexada 
Este projeto apresenta um simulador simples de Alocação de Blocos no Disco, desenvolvido em Python para a disciplina de Sistemas Operacionais.

O objetivo do programa é demonstrar como um sistema de arquivos organiza e distribui arquivos físicos dentro dos blocos de um disco de armazenamento, gerando um mapa visual da ocupação ao final da execução.

## Sobre o Algoritmo
O algoritmo simula a Alocação Indexada (i-nodes). Nessa estratégia, os arquivos não precisam ser salvos em blocos sequenciais (contíguos). O sistema operacional mantém uma estrutura de índices (i-node) que guarda uma lista de ponteiros indicando em quais blocos físicos espalhados pelo disco aquele arquivo específico foi salvo.

## Como executar
1. Abra o terminal na pasta do projeto.
2. Execute o arquivo principal rodando o comando: 

``` bash
python aloc_bloc_disco.py 
```

## Conclusão
Este projeto demonstra o funcionamento da Alocação Indexada na prática. É possível observar que o arquivo "A" foi dividido e salvo nos blocos 0, 3 e 4, contornando os blocos que já estavam ocupados (1 e 2). Isso prova a principal vantagem dessa estratégia: o aproveitamento total do espaço fragmentado do disco sem a necessidade de realocação.

# Escalonamento de Disco

Este projeto apresenta um simulador simples de escalonamento de braço de disco, desenvolvido em Python para a disciplina de Sistemas Operacionais.

O objetivo é comparar três algoritmos de atendimento de requisições de disco:

- FCFS
- SSTF
- SCAN

O programa recebe uma posição inicial do braço do disco e uma fila de requisições de cilindros. Depois disso, calcula a ordem de atendimento e o total de cilindros percorridos por cada algoritmo.

## Algoritmos implementados

### FCFS

O algoritmo FCFS atende as requisições na mesma ordem em que elas chegam. É simples de entender, mas nem sempre gera o menor deslocamento do braço.

### SSTF

O algoritmo SSTF sempre escolhe a requisição mais próxima da posição atual do braço. Normalmente reduz o deslocamento, mas pode deixar requisições distantes esperando por mais tempo.

### SCAN

O algoritmo SCAN funciona como um elevador. O braço segue em uma direção, atende as requisições no caminho e depois retorna para atender as demais.

## Tecnologias utilizadas

- Python
- Jupyter Notebook

## Como executar

### Pelo Jupyter Notebook

1. Abra o Jupyter Notebook.
2. Execute o arquivo `escalonamento_disco.ipynb`.
3. Rode a célula principal do código.

### Pelo terminal

Execute o comando:

```bash
python escalonamento_disco.py
```

## Entrada usada no teste

```python
posicao_inicial = 53
fila_requisicoes = [98, 183, 37, 122, 14, 124, 65, 67]
tamanho_disco = 200
direcao_scan = "direita"
```

## Saída esperada

O programa mostra:

- a ordem de atendimento no FCFS;
- a ordem de atendimento no SSTF;
- a ordem de atendimento no SCAN;
- o total de cilindros percorridos em cada algoritmo;
- qual algoritmo foi mais eficiente no teste.

## Estrutura do projeto

```text
escalonamento-de-disco/
│
├── escalonamento_disco.py
├── escalonamento_disco.ipynb
├── README.md
└── Relatorio_Escalonamento_de_Disco.docx
```

## Conclusão

O simulador ajuda a visualizar a diferença entre os algoritmos de escalonamento de disco. A comparação mostra que a ordem de atendimento influencia diretamente no deslocamento do braço e no desempenho do sistema.

# Substituição por página

Este projeto apresenta um simulador simples de algoritmos de substituição de páginas na memória, desenvolvido em Python para a disciplina de Sistemas Operacionais.

O objetivo é comparar três estratégias de gerenciamento de memória virtual quando ocorre falta de página (page fault):

FIFO (First-In, First-Out)

LRU (Least Recently Used)

Clock (Segunda Chance)

O programa recebe uma sequência de acessos a páginas e a quantidade de quadros (frames) disponíveis na memória RAM. A partir disso, simula o preenchimento dos frames e calcula o total de faltas de página geradas por cada algoritmo.

## Algoritmos implementados

## Fifo
O algoritmo FIFO substitui a página que está há mais tempo na memória (a primeira que entrou). É simples de implementar, mas pode sofrer da Anomalia de Belady (onde aumentar o número de frames pode aumentar o número de falhas).

## LRU
O algoritmo LRU substitui a página que ficou mais tempo sem ser acessada no passado recente. Costuma ser muito eficiente, pois se baseia no princípio da localidade temporal.

## Clock
O algoritmo Clock (ou Segunda Chance) funciona de forma circular como um relógio. Ele reduz o custo de implementação do LRU usando um bit de referência para dar uma "segunda chance" às páginas recentemente acessadas antes de decidir pela substituição.

## Como executar

### Pelo terminal

Execute o comando:

```bash
python substituicao_paginas.py
```

## Saida esperada 
O programa mostra:

Uma tabela detalhada passo a passo para o FIFO, indicando o estado dos frames e o status (hit ou FALTA);
Uma tabela detalhada passo a passo para o LRU;
Uma tabela detalhada passo a passo para o Clock (incluindo o estado dos bits de referência);
O total de faltas de página geradas por cada algoritmo;
Um gráfico textual comparativo mostrando qual algoritmo foi mais eficiente para a sequência testada.

## Conclusão
O simulador ajuda a visualizar de forma prática o impacto das políticas de substituição de páginas no desempenho do gerenciamento de memória. A comparação detalhada deixa claro como o comportamento dos acessos pode favorecer ou penalizar diferentes estratégias de paginação.

# Estrutura do projeto

```text
S.O-TRABALHO/
│
├── algoritmo_banqueiro.ipynb
├── aloc_bloc_disco.py
├── escalonamento_disco.ipynb
├── substituicao_paginas.py
└── README.md
```
