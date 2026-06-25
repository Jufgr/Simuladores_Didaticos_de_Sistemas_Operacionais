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

# Estrutura do projeto

```text
S.O-TRABALHO/
│
├── algoritmo_banqueiro.ipynb
├── aloc_bloc_disco.py
└── README.md
```
