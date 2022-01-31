import re


def c(text, chars=" !?"):
    rx = re.compile(f'{chars}')
    text = rx.sub(r'-', text)
    print(text)


a = 'dsf !?#'
c(a)
