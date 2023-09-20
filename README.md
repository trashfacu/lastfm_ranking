[![Github Status][github-shield]][github-url]

Esto es un bot de Discord que crea y muestra una tabla de puntuaciones basada en los scrobbles de los usuarios de LastFM en un servidor.

## Requisitos Previos

- Python 3.x instalado en tu máquina.
- Una cuenta en Discord para configurar un bot.
- Una cuenta en Last.fm para obtener una clave de API.

## Configuración

1. Clona el repositorio a tu máquina local:

```bash
git clone https://github.com/trashfacu/lastfm_ranking.git
cd lastfm_ranking
```


2. Crea un entorno virtual e instala las dependencias:

```bash
python -m virtualenv lastfm-rank-env
.\lastfm-rank-env\Scripts\activate
pip install -r requirements.txt
```


3. Crea un archivo `.env` en la raíz del proyecto y agrega tus claves de API y tokens de Discord:

```
LASTFM_API_KEY=TU_CLAVE_DE_API_DE_LASTFM
BOT_TOKEN=TU_TOKEN_DE_DISCORD_BOT
```


## Uso

1. Ejecuta el bot con el siguiente comando:

```python
python main.py
```


2. Invita al bot a tu servidor de Discord y configúralo con el prefijo `!`.

3. Usa los siguientes comandos para interactuar con el bot:

- `!set_lastfm <nombre_de_usuario_de_LastFM>`: Configura tu nombre de usuario de LastFM.
- `!ranking`: Muestra la tabla de puntuaciones basada en los scrobbles de los usuarios de LastFM en el servidor.

[github-shield]: https://img.shields.io/badge/GitHub-trashfacu-blue?logo=github&style=flat
[github-url]: https://github.com/trashfacu/RantMyGameAPI