import reflex as rx
from datetime import datetime, timedelta, timezone


#comun 

def lang() -> rx.Component:  
    return rx.script("document.documentElement.lang='es'")

#index


index_title="Alejandro | Page"
index_description="Hola, mi nombre es Alejandro y te enseño programación e IA"


courses_title="Alejandro | Cursos"
courses_description="Hola, mi nombre es Alejandro y te enseño programación e IA"


from zoneinfo import ZoneInfo


LOCALE_MAP = {
    "es-ES": "España", "en-US": "EE.UU.", "en-GB": "Reino Unido",
    "en-CA": "Canadá", "fr-FR": "Francia", "de-DE": "Alemania",
    "it-IT": "Italia", "pt-PT": "Portugal", "pt-BR": "Brasil",
    "nl-NL": "Países Bajos", "be-BY": "Bélgica", "ch-DE": "Suiza",
    "at-DE": "Austria", "se-SE": "Suecia", "no-NO": "Noruega",
    "dk-DK": "Dinamarca", "fi-FI": "Finlandia", "pl-PL": "Polonia",
    "cz-CZ": "República Checa", "sk-SK": "Eslovaquia", "hu-HU": "Hungría",
    "ro-RO": "Rumanía", "bg-BG": "Bulgaria", "gr-GR": "Grecia",
    "tr-TR": "Turquía", "ru-RU": "Rusia", "jp-JP": "Japón",
    "cn-CN": "China", "kr-KR": "Corea del Sur", "in-IN": "India",
    "au-AU": "Australia", "nz-NZ": "Nueva Zelanda", "mx-MX": "México",
    "ar-AR": "Argentina", "cl-CL": "Chile", "co-CO": "Colombia",
    "pe-PE": "Perú", "ve-VE": "Venezuela", "cu-CU": "Cuba",
    "do-DO": "República Dominicana", "uy-UY": "Uruguay",
    "py-PY": "Paraguay", "bo-BO": "Bolivia", "ec-EC": "Ecuador",
    "cr-CR": "Costa Rica", "pa-PA": "Panamá", "gt-GT": "Guatemala",
    "sv-SV": "El Salvador", "hn-HN": "Honduras", "ni-NI": "Nicaragua",
    "ie-IE": "Irlanda", "za-ZA": "Sudáfrica", "eg-EG": "Egipto",
    "ma-MA": "Marruecos", "ng-NG": "Nigeria", "il-IL": "Israel",
    "sa-SA": "Arabia Saudí", "ae-AE": "Emiratos Árabes",
}


def _country_from_locale(locale: str) -> str:
    if locale in LOCALE_MAP:
        return LOCALE_MAP[locale]
    parts = locale.split("-")
    if len(parts) >= 2:
        return parts[1].upper()
    return "tu ubicación"


def next_date(dates: dict, user_tz: str = "Europe/Madrid", locale: str = "es-ES") -> str:
    if not dates:
        return ""

    madrid_tz = ZoneInfo("Europe/Madrid")
    now_madrid = datetime.now(madrid_tz)
    current_weekday = now_madrid.weekday()

    for i in range(7):
        day = str((current_weekday + i) % 7)
        if day not in dates or not dates[day]:
            continue

        hour, minute = map(int, dates[day].split(":"))
        event_madrid = now_madrid.replace(hour=hour, minute=minute, second=0, microsecond=0)
        event_madrid += timedelta(days=i)

        if i == 0 and event_madrid <= now_madrid:
            continue

        formated_date = event_madrid.strftime("%A %d %B")
        if user_tz and user_tz != "Europe/Madrid":
            user_zone = ZoneInfo(user_tz)
            event_user = event_madrid.astimezone(user_zone)
            formated_time = event_user.strftime("%H:%M")
            country = _country_from_locale(locale)
            return f"{formated_date} a las {formated_time} (hora de {country})"
        else:
            formated_time = event_madrid.strftime("%H:%M")
            return f"{formated_date} a las {formated_time} (hora de Madrid)"

    return ""
