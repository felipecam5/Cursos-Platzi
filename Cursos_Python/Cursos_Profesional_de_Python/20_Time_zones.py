# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)

print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

vienna_timezone = pytz.timezone("Europe/Vienna")
vienna_date = datetime.now(vienna_timezone)
print(f'La fecha en vienna es {vienna_date.strftime("%d/%m/%Y, %H:%M:%S")}')