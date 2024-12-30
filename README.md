# YouTube Playlist Downloader

Este projeto permite baixar playlists do YouTube como arquivos MP3 usando `yt-dlp`.

## Requisitos

1. **Python**: Certifique-se de que o Python 3.6 ou superior esteja instalado em sua máquina.
2. **FFmpeg**: É necessário para a conversão de áudio para MP3.

### Instalando o FFmpeg no macOS

Se estiver utilizando o macOS, você pode instalar o FFmpeg usando o Homebrew:

```bash
brew install ffmpeg
```
Para verificar se o FFmpeg foi instalado corretamente, execute:

```bash
ffmpeg -version
```
### Instale as dependências:

```bash
pip install -r requirements.txt
```
## Utilização
Certifique-se de ter o arquivo cookies.txt necessário para autenticação no YouTube. (Isso pode ser exportado usando extensões como Cookies.txt Exporter).

Execute o script:
```bash
python download_playlist.py
```
Insira as informações solicitadas:
* URL da playlist do YouTube
* Caminho para o arquivo cookies.txt
* Diretório onde deseja salvar os arquivos MP3

Os arquivos MP3 serão salvos no diretório especificado.

### Problemas Conhecidos
Caso o FFmpeg não esteja instalado ou configurado corretamente, o script não conseguirá converter os arquivos de áudio para MP3. Siga as instruções acima para garantir que o FFmpeg está funcional.

# Se precisar de algo mais, é só avisar!
