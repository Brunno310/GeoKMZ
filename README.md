# GeoKMZ

**GeoKMZ** é um script Python simples que permite gerar arquivos **KMZ** a partir de coordenadas geográficas fornecidas pelo usuário. Ideal para quem trabalha com geolocalização, o script aceita múltiplas coordenadas de uma vez, facilitando a criação de mapas e a visualização de locais específicos.

### Funcionalidades
- **Entrada Interativa de Coordenadas:** O usuário pode inserir coordenadas de latitude e longitude separadas por vírgula, e o script irá gerar automaticamente um arquivo KMZ.
- **Suporte a Múltiplas Coordenadas:** Permite a inserção de várias coordenadas em uma única linha, separadas por ponto e vírgula.
- **Criação Personalizada de Arquivo KMZ:** O nome do arquivo KMZ pode ser definido pelo usuário antes de salvar.

### Como Usar

1. **Clonar o Repositório:**
   Se você ainda não tem o repositório clonado, use o seguinte comando

   git clone https://github.com/Brunno310/GeoKMZ.git

### Antes de rodar o script, instale as dependências necessárias. Navegue até o diretório do projeto e execute
pip3 install -r requirements.txt --break-system-packages

### Atenção: O uso de --break-system-packages pode afetar o sistema. Se preferir, use um ambiente virtual.

### Para Executar o Script: Execute o script com o seguinte comando
python GeoKMZ.py

### Forneça as Coordenadas: O script solicitará que você forneça as coordenadas de latitude e longitude. Você pode inserir várias coordenadas separadas por ponto e vírgula.

### Para Salvar o Arquivo KMZ: O script pedirá um nome para o arquivo KMZ que será gerado. O arquivo será salvo no formato .kmz

### Tecnologias Utilizadas
Python 3: O script é compatível com Python 3.
SimpleKML: Biblioteca para gerar arquivos KML e KMZ.
Colorama: Para criar uma interface colorida e interativa.
