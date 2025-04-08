import os
import fitz  # pip install PyMuPDF

encontrou_arquivos = False

def buscar_palavra_em_diretorio(diretorio_raiz, palavra_chave, linhas_contexto=2):
    """Busca palavra-chave em arquivos .txt e .pdf (mesmo com quebras de linha), indicando a linha de início."""
    global encontrou_arquivos
    pastas_ignoradas = {'imagens', 'documentos', '.git'}
    palavra_chave_lower = palavra_chave.lower()

    for pasta_atual, subpastas, arquivos in os.walk(diretorio_raiz):
        subpastas[:] = [p for p in subpastas if p.lower() not in pastas_ignoradas]

        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta_atual, arquivo)
            caminho_formatado = caminho_arquivo.replace(" ", "%20")
            extensao = os.path.splitext(arquivo)[1].lower()

            try:
                if extensao == '.pdf':
                    doc = fitz.open(caminho_arquivo)
                    todas_linhas = []
                    for pagina in doc:
                        texto = pagina.get_text()
                        todas_linhas.extend(texto.split('\n'))
                    doc.close()
                    verificar_janelas(todas_linhas, palavra_chave_lower, caminho_formatado, "PDF", linhas_contexto)
                else:
                    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                        linhas = f.readlines()
                        verificar_janelas(linhas, palavra_chave_lower, caminho_formatado, "TXT", linhas_contexto)
            except Exception as e:
                print(f'Erro ao processar o arquivo {caminho_arquivo}: {e}')

def verificar_janelas(linhas, palavra_chave_lower, caminho_formatado, tipo_arquivo, linhas_contexto):
    """Verifica cada linha individualmente para encontrar palavras-chave."""
    global encontrou_arquivos

    total = len(linhas)

    for i in range(total):
        linha_atual = linhas[i].strip()  # Remove espaços extras e quebras de linha
        if palavra_chave_lower in linha_atual.lower():
            encontrou_arquivos = True
            print(f'\nArquivo: file:///{caminho_formatado} \n({tipo_arquivo}) Linha {i + 1}: {linha_atual[:300]}...\n\n --- \n ---')

if __name__ == "__main__":
    diretorio = input("Digite o diretório raiz para realizar a busca (0 para usar o padrão): ")
    if diretorio == "0":
        diretorio = "C:\\Users\\pedroluiz.zampar\\Documents\\Diarios_de_Bordo"
    palavra = input("Digite a palavra-chave a ser buscada: ")
    buscar_palavra_em_diretorio(diretorio, palavra)
    if not encontrou_arquivos:
        print("\nNada foi encontrado! :(\n")
