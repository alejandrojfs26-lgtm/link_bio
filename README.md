# link_bio

Pagina web personal tipo link-in-bio hecha con [Reflex](https://reflex.dev/).

## Que hace

- Muestra mis perfiles (GitHub, LinkedIn) y proyectos destacados
- Detecta si estoy en vivo en Twitch y muestra el horario del siguiente stream
- Traductor de texto a varios idiomas con reproduccion de audio
- Chat basico (conecta a un modelo externo para responder)

## Como funciona

**Frontend:** Reflex genera HTML/CSS/JS desde Python y lo despliega en Vercel.

**Backend:** La API corre en Railway dentro de un contenedor Docker. Maneja las llamadas a Twitch, Supabase y el chat.

**Integraciones:**
- Twitch API — estado en vivo
- Supabase — contenido destacado
- ConfigCat — horarios del stream
- Groq — respuestas del chat

## Correr local

```bash
git clone https://github.com/alejandrojfs26-lgtm/link_bio.git
cd link_bio
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
reflex run
```

## Variables de entorno

| Variable | Descripcion |
|---|---|
| `TWITCH_CLIENT_ID` | Client ID de Twitch |
| `TWITCH_CLIENT_SECRET` | Client Secret de Twitch |
| `SUPABASE_URL` | URL de Supabase |
| `SUPABASE_PUBLISHABLE_KEY` | Key de Supabase |
| `CONFIGCAT_API_KEY` | Key de ConfigCat |
| `GROQ_API_KEY` | Para el chat (opcional) |

## Deploy

El frontend se despliega solo en Vercel via GitHub Actions. El backend esta en Railway con Dockerfile.

## Licencia

MIT
