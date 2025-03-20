import os

encontrou_arquivos = False

def buscar_palavra_em_diretorio(diretorio_raiz, palavra_chave):
    """Busca uma palavra-chave dentro de todos os arquivos de texto dentro de um diretório (incluindo subdiretórios), ignorando pastas específicas."""
    global encontrou_arquivos
    pastas_ignoradas = {'imagens', 'documentos', '.git'}
    
    for pasta_atual, subpastas, arquivos in os.walk(diretorio_raiz):
        # Remove pastas ignoradas da lista de subpastas para que os.walk não entre nelas
        subpastas[:] = [pasta for pasta in subpastas if pasta.lower() not in pastas_ignoradas]
        
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta_atual, arquivo)
            caminho_formatado = caminho_arquivo.replace(" ", "%20")
            try:
                with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                    linhas = file.readlines()
                    for num_linha, linha in enumerate(linhas, start=1):
                        if palavra_chave.lower() in linha.lower():
                            encontrou_arquivos = True
                            print(f'\nArquivo: file:///{caminho_formatado} \nLinha {num_linha}: {linha.strip()}\n\n --- \n ---')
            except Exception as e:
                print(f'Erro ao processar o arquivo {caminho_arquivo}: {e}')

if __name__ == "__main__":
    diretorio = input("Digite o diretório raiz para realizar a busca (0 para usar o padrão): ")
    if diretorio == "0":
        diretorio = "C:\\Users\\pedroluiz.zampar\\Documents\\Diarios_de_Bordo"
    palavra = input("Digite a palavra-chave a ser buscada: ")
    res = buscar_palavra_em_diretorio(diretorio, palavra)
    if encontrou_arquivos == False:
        print("\nNada foi encontrado! :(\n")