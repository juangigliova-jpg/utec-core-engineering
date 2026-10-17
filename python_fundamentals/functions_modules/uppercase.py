#!/usr/bin/env python3


def uppercase(str):
    if not isinstance(str, type("")):
        print(str)
        return
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print(result)
