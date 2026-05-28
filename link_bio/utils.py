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
#calculate next date a partir de la actual 
def next_date(dates:dict) -> str:
    
    if len(dates) == 0:
        return ""

    now = datetime.now()
    current_weekday = now.weekday()
    current_time = now.astimezone().timetz()
    
    for i in range(7):
        day = str((current_weekday + i) % 7)
        if day not in dates or dates[day] == "":
            continue
        
    time_utc = datetime.strptime(dates[day], "%H:%M").replace(tzinfo=timezone.utc).timetz()
    
    time = datetime.combine(now.date(), time_utc).astimezone().timetz()
    if time > current_time or i > 0:
        
        next_date = now + timedelta(days=i)
        
        formated_date = next_date.strftime("%A %d %B") if i == 0 else next_date.strftime("%A %d %B")
        
        formated_time = time.strftime("%H:%M")
        
        return f"{day} - {formated_date} a las {formated_time} (hora de Madrid)"
    
    return ""
