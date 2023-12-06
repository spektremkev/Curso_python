#Maria pegou um emprestimo de 1.000.000 
#para realizar o pagamento em 5 anos.
#A data em que ela pegou o emprestimo foi
#20/02/2020 e o vencimento de cada parcela
#e no dia 20 de cada mes.
# - Crie a data do emprestimo
# - Crie a data do final do emprestimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
# documentação: https://docs.python.org/pt-br/3/library/datetime.html

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2023, 2, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_atual = data_emprestimo

while data_atual < data_final:
    data_parcelas.append(data_atual)
    data_atual += relativedelta(months=+1)


numero_parcelas = len(data_parcelas)
valor_parcelas = valor_total / numero_parcelas

for data in data_parcelas:
    print(data.strftime("%d/%m/%Y"), f'R$ {valor_parcelas:.2f}')

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcelas:,.2f}.'
)