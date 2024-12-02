from simplekml import Kml
from colorama import Fore, Style, init

# Inicializar o colorama
init()

# Função para solicitar coordenadas
def pedir_coordenadas():
    coordenadas = []
    print(Fore.YELLOW + "Bem-vindo ao GeoKMZ! " + Style.RESET_ALL)
    print(Fore.GREEN + "Digite várias coordenadas no formato: latitude,longitude (separadas por ponto e vírgula)" + Style.RESET_ALL)
    print(Fore.CYAN + "Digite 'sair' para finalizar.\n" + Style.RESET_ALL)
    
    while True:
        entrada = input(Fore.BLUE + "→ Coordenadas: " + Style.RESET_ALL)
        if entrada.lower() == 'sair':
            print(Fore.MAGENTA + "\nFinalizando entrada de coordenadas..." + Style.RESET_ALL)
            break
        try:
            # Separar as coordenadas inseridas por ponto e vírgula
            coordenadas_input = entrada.split(';')
            for coord in coordenadas_input:
                lat, lon = map(float, coord.split(','))
                coordenadas.append((lat, lon))
                print(Fore.GREEN + f"Adicionado: Latitude {lat}, Longitude {lon}" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Formato inválido! Por favor, insira as coordenadas no formato: latitude,longitude (separadas por ponto e vírgula)" + Style.RESET_ALL)
    return coordenadas

# Pedir o nome do arquivo
def pedir_nome_arquivo():
    while True:
        nome_arquivo = input(Fore.YELLOW + "\nDigite o nome do arquivo (sem extensão): " + Style.RESET_ALL)
        if nome_arquivo.strip():
            return nome_arquivo.strip() + ".kmz"
        else:
            print(Fore.RED + "O nome do arquivo não pode estar vazio!" + Style.RESET_ALL)

# Criar o KML
kml = Kml()

# Pedir as coordenadas
coordenadas = pedir_coordenadas()

if coordenadas:
    # Adicionar as coordenadas ao KML
    for i, (lat, lon) in enumerate(coordenadas):
        kml.newpoint(name=f"Local {i+1}", coords=[(lon, lat)])
    
    # Solicitar o nome do arquivo
    nome_arquivo = pedir_nome_arquivo()
    
    # Salvar como KMZ
    kml.savekmz(nome_arquivo)
    print(Fore.GREEN + f"\nArquivo KMZ criado com sucesso: {nome_arquivo}" + Style.RESET_ALL)
else:
    print(Fore.RED + "\nNenhuma coordenada fornecida. Arquivo KMZ não foi gerado." + Style.RESET_ALL)
