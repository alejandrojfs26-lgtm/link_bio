# Alejandro Fuentes — Link in Bio

Página web personal tipo link-in-bio construida con [Reflex](https://reflex.dev/) (Python), que muestra enlaces a mis perfiles profesionales, proyectos destacados y más.

## Tecnologías

- **Reflex** — Framework web Python para frontend y backend
- **Supabase** — Base de datos para contenido dinámico
- **Twitch API** — Detección de estado en vivo
- **ConfigCat** — Feature flags para horarios dinámicos
- **Vercel** — Deploy del frontend
- **Railway** — Deploy del backend

## Características

- Enlaces a redes sociales y perfiles profesionales
- Detección de live en Twitch
- Sección de contenido destacado desde Supabase
- Horarios dinámicos con countdown
- Diseño responsive

## Desarrollo local

```bash
# Clonar
git clone https://github.com/alejandrojfs26-lgtm/link_bio.git
cd link_bio

# Entorno virtual
python -m venv .venv
source .venv/bin/activate

# Dependencias
pip install -r requirements.txt

# Variables de entorno (crear .env)
cp .env.example .env

# Iniciar servidor de desarrollo
reflex run
```

## Variables de entorno

| Variable | Descripción |
|---|---|
| `TWITCH_CLIENT_ID` | Client ID de Twitch API |
| `TWITCH_CLIENT_SECRET` | Client Secret de Twitch API |
| `SUPABASE_URL` | URL de Supabase |
| `SUPABASE_PUBLISHABLE_KEY` | API Key de Supabase |
| `CONFIGCAT_API_KEY` | API Key de ConfigCat |

## Deploy

```bash
reflex deploy
```

O manualmente a Vercel (frontend) y Railway (backend).

## Licencia

MIT
