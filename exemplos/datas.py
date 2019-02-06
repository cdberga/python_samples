from datetime import date
from datetime import time

data1 = date(2019, 1, 1)
print (data1)
print(date.today())

fim_do_ano = date(2019,12,31)
tempo_para_fim_do_ano = abs(fim_do_ano - date.today())
print("Faltam %s para o fim do ano" %tempo_para_fim_do_ano)
print(fim_do_ano.weekday())

data1 = data1.replace(day=3)
print(data1)
print(data1.strftime("%d/%m/%Y"))

tempo1 = time(12,8,5,300001)
print(tempo1.strftime("%H horas, %M minutos e %S segundos"))