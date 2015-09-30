# coding:utf-8
#!/usr/bin/env python
import sys

a = [1,1,3,3,3,5,6,7,8]

def f(x, y):
    if x and x[-1] and x[-1][-1] == y:
        x[-1].append(y)
        return x
    else:
        x.append([y])
        return x


def ff(s=[[]]):
    c = s
    def f(x, y):
        if c != x:
            c[-1].append(x)
        if c[-1] and c[-1][-1] == y:
            c[-1].append(y)
            return c
        else:
            c.append([y])
            return c
    return f
print reduce(f, a, [])
#print reduce(ff(), a)


def group_sorted_data(sorted_data, key=None, equal=None):
    """
    例如：a = [1,1,3,3,3,5,6,7,8]
         group_sorted_data(a)

    返回：
         [[1, 1], [3, 3, 3], [5], [6], [7], [8]]
    """
    def _equal(val1, val2, key=None):
        if isinstance(val1, (dict,)) and isinstance(val2, (dict,)):
            return bool(val1.get(key)) and val1.get(key) == val2.get(key)
        return val1 == val2
    _eq = _equal
    if callable(equal):
        try:
            co_arg = equal.func_code.co_argcount
            if co_arg == 2:
                _eq = equal
                del _equal
        except:
            pass

    def _group(first, second):
        if first and first[-1] and _eq(first[-1][-1], second, key):
            first[-1].append(second)
            return first
        else:
            first.append([second])
            return first
    return reduce(_group, sorted_data, [])
print group_sorted_data(a)
b = [{"shop_id":2}, {"shop_id": 2}, {"shop_id": 3}]
print group_sorted_data(b, key="shop_id")


