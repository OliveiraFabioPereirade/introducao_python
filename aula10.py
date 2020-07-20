from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual) # ano (4 dígitos), mês e dia separados por traço
    print(data_atual.strftime('%d/%m/%y')) # dia do mês, número do mês e ano (2 dígitos) separados por barra
    print(data_atual.strftime('%d %m %Y')) # dia do mês, número do mês e ano (4 dígitos) separados por espaço
    data_atual_str = data_atual.strftime('%A %B %Y') # dia do mês, nome do mês e ano (4 dígitos) separados por espaço
    print(data_atual_str)
    print(type(data_atual))     # tipo datatime.date
    print(type(data_atual_str)) # tipo string

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(type(horario)) # tipo datatime.date
    horas = horario.strftime('%H|%M|%S') # hora, minuto e segundo separador por |
    print(horas)
    print(type(horas)) # tipo string

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%H:%M:%S %d/%m/%y'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.month)
    print(data_atual.year)
    print(data_atual.hour)
    print(data_atual.minute)
    print(data_atual.second)
    print(data_atual.weekday())
    dia_semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(dia_semana[data_atual.weekday()])
    mes_ano = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    print(mes_ano[data_atual.month-1])
    data_criada = datetime(2020, 7, 20, 12, 59, 15) # cria data
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2020 12:20:02'    # converte string em data
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(type(data_convertida))
    nova_data = data_convertida - timedelta(days=365, hours=2) # obtém data um ano e 2 horas anterior à data_convertida
    print(nova_data)





if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()

