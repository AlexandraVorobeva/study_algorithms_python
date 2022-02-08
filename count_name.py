# Напишите программу, которая принимает на вход произвольные слова
# (по одному слову в каждой строке, последовательность заканчивается строкой, состоящей из одной точки),
# формирует список тех же слов в нижнем регистре, упорядоченных по убыванию количества вхождений и
# лексикографически при одинаковом количестве вхождений, и печатает первые три элемента этого списка.


from collections import Counter
import itertools


def solution():
    all_names = []
    n = input().lower()
    while n != '.':
        all_names.append(n)
        n = input().lower()
    top = dict(Counter(all_names))
    d = {}
    for key, val in top.items():
        if val in d:
            d[val].append(key)
        else:
            d[val] = [key]
    res = []
    list_keys = list(d.keys())
    list_keys.sort(reverse=True)
    for i in list_keys:
        d[i].sort()
        res.append(d[i])
    res = itertools.chain(*res)
    res = list(res)[:3]
    for re in res:
        print(re, end='\n')


solution()