def ler_avaliacoes(arquivo_path):
    with open(arquivo_path, 'avaliacoes.txt', encoding='utf-8') as f:
        linhas = f.readlines()

    avaliacoes = {}
    nome_atual = None

    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue

        if linha.endswith('{'):
            nome_atual = linha[:-1].strip()
        elif linha.startswith('Funcionalidade'):
            funcionalidade = int(linha.split(':')[1])
        elif linha.startswith('Logica'):
            logica = int(linha.split(':')[1])
        elif linha.startswith('Clareza'):
            clareza = int(linha.split(':')[1])
        elif linha == '}':
            if nome_atual:
                if nome_atual not in avaliacoes:
                    avaliacoes[nome_atual] = []

                avaliacoes[nome_atual].append({
                    'Funcionalidade': funcionalidade,
                    'Logica': logica,
                    'Clareza': clareza
                })

    return avaliacoes


def calcular_media(avaliacoes):
    medias = {}

    for nome, avals in avaliacoes.items():
        total_func = sum(a['Funcionalidade'] for a in avals)
        total_log = sum(a['Logica'] for a in avals)
        total_cla = sum(a['Clareza'] for a in avals)
        n = len(avals)

        media_total = (total_func + total_log + total_cla) / (3 * n)

        medias[nome] = {
            'Media Geral': round(media_total, 2),
            'Media Funcionalidade': round(total_func / n, 2),
            'Media Logica': round(total_log / n, 2),
            'Media Clareza': round(total_cla / n, 2)
        }

    return medias


def exibir_ranking(medias):
    ranking = sorted(medias.items(), key=lambda x: x[1]['Media Geral'], reverse=True)

    print("🏆 Ranking dos Alunos:")
    for i, (nome, dados) in enumerate(ranking, start=1):
        print(f"{i}º lugar: {nome} - Média Geral: {dados['Media Geral']}")


# Caminho do arquivo
caminho_arquivo = 'avaliacoes.txt'

avaliacoes = ler_avaliacoes(caminho_arquivo)
medias = calcular_media(avaliacoes)
exibir_ranking(medias)
