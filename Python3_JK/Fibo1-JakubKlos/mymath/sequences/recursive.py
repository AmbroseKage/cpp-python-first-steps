#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List


def fib(n: int) -> List[int]:
    """Zwróć n pierwszych elementów ciągu Fibonacccciego.

    Parametry:
     n ---- liczba elementów ciągu do wygenerowania
    """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result 
