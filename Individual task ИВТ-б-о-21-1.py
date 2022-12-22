#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def dict1(func):

    def pnk(a, b):
        dic = func(a, b)
        return dict(zip(*dic))
    return pnk


@dict1
def wrapper(c, v):
    return c.split(), v.split()


if __name__ == "__main__":
    s = 'Москва Питербург Воронеж'
    t = '2000 2500 800'
    x = wrapper(s, t)
    print(x)
