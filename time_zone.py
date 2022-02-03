
from datetime import datetime
import pytz

def time_zone(country_time, city_country):
    country_time_zone = pytz.timezone(country_time)
    country_date = datetime.now(country_time_zone)
    print(f"{city_country}: ", country_date.strftime('%d/%m/%y, %I:%M:%S %p'))

def run():
    bogota = "America/Bogota"
    time_zone(bogota,"Bogota")

    mexico = "America/Mexico_city"
    time_zone(mexico, "Ciudad de México")

    caracas = "America/Caracas"
    time_zone(caracas, "Caracas")

if __name__=='__main__':
    run()
    