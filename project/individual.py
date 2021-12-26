#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def check_brackets(s):
    left = s.find("(")
    right = s.rfind(")")
    if left == -1 and right == -1:
        return True
    elif left == -1 or right == -1 or right < left:
        return False
    else:
        return check_brackets(s[left + 1:right])


print(check_brackets("оаоа((мм)тв)"))
print(check_brackets("яхочу(спать)очень)"))
print(check_brackets("e(g)uu)jjj("))

