#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def dict1(func):

    def wrapper(*args, **kwargs):
        dic = func(*args, **kwargs)
        return dict(zip(*dic))
    return wrapper


@dict1
def func1(c, v):
    return c.split(), v.split()


if __name__ == "__main__":
    s = 'Москва Питербург Воронеж'
    t = '2000 2500 800'
    x = func1(s, t)
    print(x)
