tamanho_do_disco = 20 
disco = ['[ ]'] * tamanho_do_disco
disco[1] = '[X]' 
disco[2] = '[X]'
disco[5] = '[X]'

arquivos_para_salvar = [
    {'nome': 'A', 'tamanho': 3},
    {'nome': 'B', 'tamanho': 5},
    {'nome': 'C', 'tamanho': 2},
    {'nome': 'D', 'tamanho': 4}
]

def alocar_arquivos(disco, arquivos):
    print(f"espaço inicial no disco: {disco.count('[ ]')} blocos livres.")
    indices_arquivos = {}
    for arquivo in arquivos:
        nome = arquivo['nome']
        tamanho = arquivo['tamanho']
        lista_blocos = []


        print(f" tentando alocar o arquivo '{nome}' (tamanho: {tamanho} blocos)")

        espaco_livre_atual = disco.count('[ ]') 
        if tamanho > espaco_livre_atual:
            print(f"   Erro: Espaço insuficiente no disco para o arquivo '{nome}'.\n")
            continue 

        for i in range(len(disco)):
            
            if len(lista_blocos) == tamanho: 
                break
            if disco[i] == '[ ]': 
                lista_blocos.append(i)    
                disco[i] = f'[{nome}]'
            
        indices_arquivos[nome] = lista_blocos
        print(f"   arquivo '{nome}' processado.\n")
        
    print(indices_arquivos)  
    return disco

disco_atualizado = alocar_arquivos(disco, arquivos_para_salvar)

print("Mapa do Disco Final (Alocação Indexada):")
print("".join(disco_atualizado))