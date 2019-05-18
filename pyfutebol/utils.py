import time

def is_hh_mm_time(time_string):
    """ Função que verifica se uma string tem o formato de hora: hh:mm """
    try:
        time.strptime(time_string, '%H:%M')
    except ValueError:
        return False
    return len(time_string) == 5