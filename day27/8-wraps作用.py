# 作者: 王道 龙哥
# 2022年06月29日11时48分36秒
from functools import wraps

def my_decorator(func):
    @wraps(func) #让函数名和备注称为原有的函数的
    def wper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)

    return wper


@my_decorator
def example():
    """example的doc"""
    print('Called example function')


print(example.__name__, example.__doc__)
example()