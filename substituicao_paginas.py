

from collections import deque, OrderedDict


SEQUENCIA = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]   
N_FRAMES  = 3                                          



RESET = "\033[0m"
BOLD  = "\033[1m"
RED   = "\033[91m"
GREEN = "\033[92m"
CYAN  = "\033[96m"
WHITE = "\033[97m"
BLUE  = "\033[94m"
GREY  = "\033[90m"
YELLOW = "\033[93m"


def cor(texto, *estilos):
    return "".join(estilos) + str(texto) + RESET


def linha(char="─", n=70):
    return char * n




def fifo(sequencia, n_frames):
    frames = []
    fila   = deque()
    faults = 0
    historico = []

    for pagina in sequencia:
        fault = False
        if pagina not in frames:
            fault = True
            faults += 1
            if len(frames) < n_frames:
                frames.append(pagina)
                fila.append(pagina)
            else:
                vitima = fila.popleft()
                frames[frames.index(vitima)] = pagina
                fila.append(pagina)
        historico.append((list(frames), pagina, fault, None))

    return historico, faults


def lru(sequencia, n_frames):
    cache  = OrderedDict()
    faults = 0
    historico = []

    for pagina in sequencia:
        fault = False
        if pagina not in cache:
            fault = True
            faults += 1
            if len(cache) >= n_frames:
                cache.popitem(last=False)
            cache[pagina] = True
        else:
            cache.move_to_end(pagina)
        historico.append((list(cache.keys()), pagina, fault, None))

    return historico, faults


def clock(sequencia, n_frames):
    frames   = [None] * n_frames
    bits     = [0]    * n_frames
    ponteiro = 0
    faults   = 0
    historico = []

    for pagina in sequencia:
        fault = False
        if pagina in frames:
            bits[frames.index(pagina)] = 1
        else:
            fault = True
            faults += 1
            while True:
                if bits[ponteiro] == 0:
                    frames[ponteiro] = pagina
                    bits[ponteiro]   = 1
                    ponteiro = (ponteiro + 1) % n_frames
                    break
                else:
                    bits[ponteiro] = 0
                    ponteiro = (ponteiro + 1) % n_frames
        historico.append((list(frames), pagina, fault, list(bits)))

    return historico, faults


def imprimir_tabela(historico, n_frames, faults, algoritmo):
    print()
    print(cor(f"  Algoritmo: {algoritmo}", BOLD, CYAN))
    print(cor(linha(), GREY))

    header = " | ".join(f" F{i+1} " for i in range(n_frames))
    print(f"  {'Pág':^6}  │  {cor(header, BOLD)}  │  Status")
    print(cor(linha(), GREY))

    for frames_atual, pagina, fault, bits in historico:
        celulas = []
        for i in range(n_frames):
            v = frames_atual[i] if i < len(frames_atual) else None
            if v is not None:
                celulas.append(cor(str(v).center(4), YELLOW, BOLD))
            else:
                celulas.append(cor(" -- ", GREY))

        pg_str     = cor(str(pagina).center(4), WHITE, BOLD)
        frames_str = " | ".join(celulas)
        status     = cor("   FALTA", RED, BOLD) if fault else cor("   hit  ", GREEN)
        bit_str    = ""
        if bits is not None:
            bit_str = "  bits:[" + cor(",".join(str(b) for b in bits), BLUE) + "]"

        print(f"  pág {pg_str}  │  {frames_str}  │{status}{bit_str}")

    print(cor(linha(), GREY))
    print(f"  {cor('Total de faltas de página:', BOLD)} {cor(faults, RED, BOLD)}\n")


def resumo(resultados):
    print()
    print(cor(linha("-"), CYAN, BOLD))
    print(cor("   Comparativo Final", CYAN, BOLD))
    print(cor(linha("═"), CYAN, BOLD))
    print()

    melhor = min(resultados, key=lambda x: x[1])
    largura = max(len(r[0]) for r in resultados)

    for nome, faults in resultados:
        barra = "|" * faults
        marca = cor("  -> menor", GREEN, BOLD) if nome == melhor[0] else ""
        print(f"  {nome:<{largura}}  {cor(str(faults).rjust(3), YELLOW, BOLD)} faltas  {cor(barra, RED)}{marca}")

    print()
    print(cor(linha(), GREY))
    print(f"  {cor('Melhor para essa sequência:', BOLD)} {cor(melhor[0], GREEN, BOLD)}")
    print(cor(linha(), GREY))
    print()


def main():
    print()
    print(cor(linha("-"), CYAN, BOLD))
    print(cor("    Simulador de Substituição de Páginas", CYAN, BOLD))
    print(cor(linha("═"), CYAN, BOLD))
    print(f"\n  {cor('Sequência:', BOLD)} {SEQUENCIA}")
    print(f"  {cor('Frames:   ', BOLD)} {N_FRAMES}\n")

    algoritmos = [
        ("FIFO",  fifo),
        ("LRU",   lru),
        ("Clock", clock),
    ]

    resultados = []
    for nome, func in algoritmos:
        historico, faults = func(SEQUENCIA, N_FRAMES)
        imprimir_tabela(historico, N_FRAMES, faults, nome)
        resultados.append((nome, faults))

    resumo(resultados)


if __name__ == "__main__":
    main()
