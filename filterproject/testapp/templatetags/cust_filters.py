from django import template
register = template.Library()

def first_five_upper(value):
    result = value[:5].upper()
    return result

def first_n_numbers(value,n):
    result = value[:n].upper()
    return result

register.filter('ffu',first_five_upper)
register.filter('fnn',first_n_numbers) 