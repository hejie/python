import functools
import logging

func = functools.partial(int, base=10)

print(func('11111'))

logging.exception("wwwww")


def str2num(s):
    return float(s)


print(str2num('7.4'))
