import datetime

def format_date(date_str):
    """
    Converte uma string de data (YYYY-MM-DD) para formato brasileiro DD/MM/YYYY
    """
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%d/%m/%Y")
    except:
        return date_str

def calculate_average(grades):
    """
    Calcula a média de uma lista de notas
    """
    if not grades:
        return 0
    return sum(grades) / len(grades)