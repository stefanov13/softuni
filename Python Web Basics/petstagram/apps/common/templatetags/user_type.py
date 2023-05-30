from django.template import Library

register = Library()

@register.simple_tag
def get_user():
    # user = Profile.objects.first() -> това ще вземе първия обект от таблицата 'Profile', а като имаме вече потребители ще се промени малко логиката
    user = False
    return user
