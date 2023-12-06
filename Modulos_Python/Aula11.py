#Usando calendar para calendarios e datas
#
#Calendar e usando para coisas genericas de calendarios e datas
#Com calendar, e possivel saber coisas como:
# - o dia de hoje
# - o dia de um determinado mes
# - o dia de um determinado ano
# - Criar um calendario em si
# - trabalhar com coisas especificas de um calendario 
# por padrao dia da semana começa em 0 ate 6 
# 0 - segunda-feira | 1 - terça-feira | 2 - quarta-feira | 3 - quinta-feira | 4 - sexta-feira | 5 - sabado | 6 - domingo

import calendar
import locale

locale.setlocale(locale.LC_ALL, '')

print(calendar.calendar(2023))
print(calendar.month(2023, 2))
print(calendar.monthcalendar(2023, 2))
print(calendar.day_name[0])
print(calendar.monthrange(2023, 2))
print(calendar.weekday(2020, 2, 20))
print(calendar.Calendar(6).monthdayscalendar(2023, 2))