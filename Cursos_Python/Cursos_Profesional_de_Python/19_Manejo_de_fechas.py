from datetime import datetime

my_time = datetime.utcnow()
print(my_time)

print(f'El año de hoy es: {my_time.year}')
print(f'El dia de hoy es: {my_time.day}')
print(f'El mes de hoy es: {my_time.month}')

# FORMATEO DE FECHAS

my_format1 = my_time.strftime('%Y/%m/%d')
my_format2 = my_time.strftime('%H:%M:%S') 
print(my_format1 + "\n" + my_format2)
