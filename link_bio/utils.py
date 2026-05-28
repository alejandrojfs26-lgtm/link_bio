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


#date
def next_date(dates: dict) -> str:
    if not dates:
        return ""

    now = datetime.now().astimezone()
    current_weekday = now.weekday()
    current_time = now.timetz()

    for i in range(7):
        day = str((current_weekday + i) % 7)
        if day not in dates or not dates[day]:
            continue

        time_utc = datetime.strptime(dates[day], "%H:%M").replace(tzinfo=timezone.utc).timetz()
        event_time = datetime.combine(now.date(), time_utc).astimezone().timetz()

        if event_time > current_time or i > 0:
            next_date = now + timedelta(days=i)
            formated_date = next_date.strftime("%A %d %B")
            formated_time = event_time.strftime("%H:%M")
            return f"{formated_date} a las {formated_time} (hora de Madrid)"

    return ""
