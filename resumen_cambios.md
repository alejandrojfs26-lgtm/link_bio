# Resumen de Cambios — link_bio

> Desde el último análisis técnico (`link_bio_analisis_tecnico.pdf`).

---

## 1. Navbar

### Logo
- **Antes:** "Alejandro" + "Fuentes" en dos `rx.text.span`
- **Ahora:** "AF" en un solo `rx.heading` — más limpio y compacto

### Altura
- Reducida de `56px` → `44px` tanto en desktop como mobile
- Tamaño del logo: `Size.LARGE` (1.5em) → `Size.DEFAULT` (1em)
- Botón hamburguesa: de `2.5rem` → `2rem`, SVG de `20x20` → `18x18`

### Fondo oscuro permanente
- **Antes:** fondo `transparent` cuando no hay scroll, `rgba(5,5,8,0.9)` al scrollear
- **Ahora:** siempre `rgba(5,5,8,0.85)` con `backdrop-filter: blur(12px)` — evita que textos/íconos se solapen con el fondo animado

### Archivos modificados
- `link_bio/components/navbar.py` — logo "AF", altura 44px, fondo oscuro fijo

---

## 2. Chat con IA

### Mecanismo de escritura (typing)

#### Problema original
El typing usaba `reflex.call('chat_state.typing_tick')` desde JavaScript vía `setInterval`. **`reflex.call` no existe en Reflex 0.9.x**, por lo que el método `typing_tick` nunca se ejecutaba. La IA respondía pero el mensaje quedaba vacío y `loading` se quedaba atascado en `True`.

#### Solución
Reemplazado por un **async generator**:
- `async def send_message()` con `yield` para enviar actualizaciones de estado
- `await asyncio.to_thread(CHAT_API.chat, api_messages)` — ejecuta la llamada a la API en un hilo separado sin bloquear el event loop
- Bucle `for i in range(len(response))` con `await asyncio.sleep(0.015)` + `yield` para revelar caracteres uno a uno desde el backend
- Se eliminó `typing_tick()`, `typing_pos`, y todo el código JS de intervalos

### Loader ("La IA está pensando")
- **Antes:** aparecía debajo del input de texto
- **Ahora:** aparece en el header del chat, al lado del botón **Limpiar**, solo cuando `loading=True`
- `transform-origin` del `.chat-loader` cambiado de `top left` → `center` para alineación vertical

### Typewriter CSS
Agregada animación de **cursor naranja parpadeante** al final del texto del asistente:
- Clase `.typewriter` aplicada con `rx.cond(~is_user, "typewriter", "")`
- `border-right: .15em solid orange` + `animation: blink-caret .75s step-end infinite`
- `display: inline` para que el cursor quede justo después del último carácter
- Sin `white-space: nowrap` ni `letter-spacing` excesivo — el texto salta de línea normalmente

### Chat input simplificado
- Eliminado `rx.vstack` y `rx.cond(ChatState.loading, ...)` del input (el loader ahora está arriba)
- El formulario quedó como un `rx.hstack` directo con input + botón enviar

### Archivos modificados
- `link_bio/state/chat_state.py` — `async def send_message` con `asyncio` + typing backend-driven
- `link_bio/pages/chat.py` — loader en header, typewriter en mensajes
- `assets/css/styles.css` — clase `.typewriter`

---

## 3. Fondo animado (beams)

### Problemas originales
1. **No aparecía siempre** — el canvas no se inicializaba en todos los casos
2. **Dejaba de funcionar al navegar** — clicks en el navbar (SPA) no reactivaban el canvas
3. **Overlay con `backdropFilter: blur(50px)`** causaba problemas de renderizado

### Soluciones
- **Inicialización robusta:** variable global `window._bgBeams` en vez de `canvas.dataset`; reintento cada 100ms hasta 20 veces
- **Navegación SPA:** `MutationObserver` que solo reacciona cuando se agrega un nuevo `<canvas id="bg-beams">` al DOM (ignora otras mutaciones como cambios en inputs). También listener `popstate`
- **Overlay simplificado:** se reemplazó el blur de 50px por un fondo semitransparente `rgba(5,5,8,0.4)` — más confiable
- **Rendimiento:** beams reducidos de 30 → 20, blur de 35px → 30px

### Archivos modificados
- `link_bio/components/animated_background.py`

---

## 4. Tecnologías (tech marquee)

### Color Railway
- **Antes:** `#0B0D0E` (casi negro) — no se veía contra el fondo oscuro
- **Ahora:** `#E0E0E0` (gris claro) — visible

### Archivos modificados
- `link_bio/components/tech_marquee.py`

---

## 5. Paleta de colores

Se unificó la paleta a tonos **púrpura / navy**:
- `PRIMARY`: `#101366` (azul profundo)
- `SECONDARY`: `#1A1D7A`
- `BACKGROUND`: `#050508` (casi negro)
- `CONTENT`: `#0D0D14`
- `BORDER`: `#1E1E30`
- `PURPLE`: `#9146ff` (Twitch)
- Gradientes: `#6a4cf5`, `#d44df0`, `#ff7a3d`, `#ff5577`

### Archivos modificados
- `link_bio/styles/colors.py`

---

## 6. CI/CD y despliegue

### Workflow de GitHub Actions
- Se agregó `pip install --upgrade pip` antes de instalar dependencias
- Versión de Reflex: `>=0.9.2.post1` → `>=0.9.3,<0.10.0` (0.9.2.post1 no siempre está disponible en PyPI)
- Frontend se despliega a Vercel automáticamente al hacer push a `main`

### Archivos modificados
- `requirements.txt` — reflex version bump
- `.github/workflows/deploy.yml` — upgrade pip

---

## 7. Reglas aprendidas (Reflex 0.9+)

| Regla | Explicación |
|---|---|
| `reflex.call()` **no existe** | En Reflex 0.9+ no hay función global `reflex.call`. Para efectos de typing usar async generators con `asyncio.sleep` |
| `MutationObserver` con `subtree:true` | Dispara en cada cambio del DOM (incluyendo inputs). Filtrar solo por `addedNodes` con el id específico |
| `rx.text` es bloque | Para que `border-right` quede al final del texto, usar `display: inline` |
| `display: inline-block` + letter-spacing | No usar `white-space: nowrap` en texto multilínea |

---

## Archivos modificados (resumen)

| Archivo | Cambio |
|---|---|
| `link_bio/components/navbar.py` | Logo "AF", altura 44px, fondo oscuro permanente |
| `link_bio/components/animated_background.py` | MutationObserver selectivo, global state, sin blur overlay |
| `link_bio/components/tech_marquee.py` | Railway `#0B0D0E` → `#E0E0E0` |
| `link_bio/state/chat_state.py` | Async generator typing, eliminado `reflex.call` |
| `link_bio/pages/chat.py` | Loader en header, typewriter class, input simplificado |
| `link_bio/styles/colors.py` | Paleta púrpura/navy unificada |
| `assets/css/styles.css` | `.typewriter` cursor naranja, `.chat-loader` transform-origin |
| `requirements.txt` | reflex `>=0.9.3,<0.10.0` |
| `.github/workflows/deploy.yml` | `pip install --upgrade pip` |
