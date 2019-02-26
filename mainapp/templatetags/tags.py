import requests
from django import template

register = template.Library()


@register.filter(name='rubles')
def dollars_to_rubles(some_float):
    some_float = float(some_float)
    try:
        rate = (requests.get ('https://www.cbr-xml-daily.ru/daily_json.js').json ())['Valute']['USD']['Value']
    except requests.ConnectionError:
        rate = 60.00
    return f'{some_float*rate:.2f} rub'
