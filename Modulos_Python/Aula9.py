#Criando datas com modulos datatime
#datetime(ano, mes, dia, hora, minuto, segundo, microsegundo)
#datatime.strptime(data, formato)
#datetime.now()
#datatime.fromtimestamp(Unix timestamp)
#Para timezones 
#Instalando o pytz
#pip install pytz types-pytz


from datetime import datetime
from pytz import timezone

class Data:
    def __init__(self, ano, mes, dia, hora, minuto, segundo):
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

data = datetime.now(timezone('America/Sao_Paulo'))

print(data)


d1 = ano = 2025
d2 = mes = 4
d3 = dia = 20   
d4 = hora = 7
d5 = minuto = 49
d6 = segundo = 23

data1 = datetime(2025, 4, 20)
data2 = datetime(2024, 4, 20, 7, 49, 23)
data3 = datetime.now()
data4 = datetime.fromtimestamp(1000000000)
data5 = datetime.strptime('2025-04-20', '%Y-%m-%d')
data6 = datetime.now(timezone('Asia/Tokyo'))

print(data1)
print(data2)
print(data3)
print(data4)
print(data5)
print(data6)
print(d1, d2, d3, d4, d5, d6)


print(data1.strftime('%d/%m/%Y'))
print(data2.strftime('%d/%m/%Y'))
