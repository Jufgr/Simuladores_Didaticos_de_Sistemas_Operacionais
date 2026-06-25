tamanho_do_disco = 20 
disco = ['[ ]'] * tamanho_do_disco
disco[1] = '[X]' #índices ocupados para simular a estratégia de Alocação indexada (i-node)
disco[2] = '[X]'
disco[5] = '[X]'
# vai simular a fila de arquivos que o usuário quer salvar 
arquivos_para_salvar = [
    {'nome': 'A', 'tamanho': 3},
    {'nome': 'B', 'tamanho': 5},
    {'nome': 'C', 'tamanho': 2},
    {'nome': 'D', 'tamanho': 4}
]

# esqueleto da alocação:
# receber os dados;
# percorrer a lista de arquivos; 
# ver se ha espaço total disponivel e
# preparar o laço de repeticao

# metade do que o programa faz
def alocar_arquivos(disco, arquivos):
    print(f"espaço inicial no disco: {disco.count('[ ]')} blocos livres.") # vai contar quantos espaços existem na lista disco para mostrar para o usuário 
    indices_arquivos = {}
    # gerenciar a iteração sobre os arquivos de entrada, vai pegar um arquivo por vez
    for arquivo in arquivos:
        nome = arquivo['nome']
        tamanho = arquivo['tamanho']
        lista_blocos = []


        print(f" tentando alocar o arquivo '{nome}' (tamanho: {tamanho} blocos)")

        # minha parte do que o programa faz: Verificação básica de segurança
        # se o arquivo for maior que o espaço restante, vou bloquear.
        espaco_livre_atual = disco.count('[ ]') # cada vez que tenta salvar um arquivo, ele vai contar pra ver quantos blocos vazios sobraram 
        if tamanho > espaco_livre_atual:
            print(f"   Erro: Espaço insuficiente no disco para o arquivo '{nome}'.\n")
            continue # pula para o próximo arquivo
        
        # Estratégia escolhida: Alocação indexada (i-node)

        for i in range(len(disco)):
            
            if len(lista_blocos) == tamanho: #se o tamanho da lista de blocos encontrados for igual ao tamanho dos arquivos o código termina
                break
            if disco[i] == '[ ]': #se o índice do disco for igual a '[]' adiciona o bloco na lista de blocos encontrados
                lista_blocos.append(i)    
                disco[i] = f'[{nome}]'
            
        indices_arquivos[nome] = lista_blocos
            
        
        # so mudar o '[ ]' para f'[{nome}]' nos índices 
        #print("   (só colocar a lógica de alocação para rodar aqui)")

        print(f"   arquivo '{nome}' processado.\n")
        
    print(indices_arquivos)  
    return disco

# executando a estrutura:
disco_atualizado = alocar_arquivos(disco, arquivos_para_salvar)

# saida esperada 
print("Mapa do Disco Final (Alocação Indexada):")
print("".join(disco_atualizado))