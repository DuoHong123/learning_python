# 作者: 王道 龙哥
# 2022年06月29日11时39分10秒
from time import ctime, sleep

def timefun_arg(pre=''):
    def timefun(func):
        def wrapped_func():
            print("%s called at %s --%s" % (func.__name__, ctime(),pre))
            return func()  #一般情况下为了让装饰器更通用，加上return
        return wrapped_func
    return timefun

@timefun_arg('wangdao')
def foo():
    print('I am foo')


@timefun_arg('python')
def too():
    print('I am too')

foo()
too()