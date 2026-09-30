# Python YouTube Downloader (`yt-dlp`)

Um script simples, porém poderoso, desenvolvido em Python para descarregar vídeos e áudios do YouTube em alta qualidade utilizando a biblioteca `yt-dlp`.

---

## 🚀 Funcionalidades

- **Download Direto:** Descarrega vídeos diretamente através do link do YouTube.
- **Controlo de Qualidade:** Configurado para obter formatos otimizados (como resoluções até $720p$).
- **Organização Automática:** Guarda os ficheiros descarregados numa pasta designada (`pasta_video`).
- **Combinação de Formatos:** Une automaticamente faixas separadas de vídeo e áudio utilizando o FFmpeg para garantir a melhor qualidade disponível.

---

## 🛠️ Requisitos e Pré-requisitos

Certifica-te de que tens o seguinte instalado no teu sistema:
- **Python** (versão 3.8 ou superior)
- **FFmpeg** (necessário para o `yt-dlp` juntar os fluxos de vídeo e áudio)

---

## 📦 Instalação e Configuração

1. **Clona o repositório:**
   ```bash
   git clone <URL_DO_TEU_REPOSITORIO>
   cd pythonVideosDow
   ```

2. **Cria e ativa um ambiente virtual:**
   ```bash
   python -m venv .env
   # No Windows (PowerShell):
   .env\Scripts\Activate
   ```

3. **Instala as dependências necessárias:**
   ```bash
   pip install yt-dlp
   ```

---

## 💻 Como Utilizar

1. Abre o ficheiro `main.py`.
2. Altera a variável `url` com o link do vídeo do YouTube que pretendes descarregar:
   ```python
   url = "O_TEU_LINK_AQUI"
   ```
3. Executa o script no terminal do teu editor:
   ```bash
   python main.py
   ```
4. Os ficheiros serão guardados automaticamente dentro da pasta `pasta_video/`.

---

## 🛡️ Notas

- Este projeto foi desenvolvido para fins educacionais e de uso pessoal. Respeita sempre os termos de serviço do YouTube e os direitos de autor dos criadores de conteúdos.