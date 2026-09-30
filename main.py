import yt_dlp

url = "https://www.youtube.com/watch?v=6ttQziuwrAA"
destino = "pasta_video/%(title)s.%(ext)s"

ydl_opts = {
    'format': 'bv*[height<=720]+ba/b[height<=720]',
    'outtmpl': destino,
}

print("A descarregar a live (vídeo e áudio)... Por favor, aguarde.")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download concluído com sucesso!")